# units_v2.py

"""
Module to take care of everything related to units
"""

# standard libraries
from copy import deepcopy as _copy 
# nonstandard libraries
# homegrown libraries

global _known_units
_known_units = ['g','L','mol','Da','M','m']


class Unit(object):

    def __init__(self,s):

        if isinstance(s,Unit):
            self.value = s.value
            self.units = s.units
            return None
        elif isinstance(s,(int,float)):
            s = [s]
        elif isinstance(s,str):
            s = s.split(' ') # split string
        elif s is None:
            s = [0]
        else:
            TypeError('Uncertain unit type ({})!'.format(s))

        # make numerator/denominator dictionary
        self.units = dict([(unit,0) for unit in _known_units])

        self.value = float(s[0])
    
        # if there were no units
        if len(s) == 1: return None
            
        # start analysis on units 
        if '/' in s[1]: num,den = s[1].split('/')
        else:           num,den = s[1],''

        # assign units to attibutes
        for sgn,v in zip([1,-1],[num,den]):
            for m in v.split('*'):
                if '^' in m:
                    m,degree = m.split('^')
                else:
                    degree = 1

                if m == '': continue

                matched_unit,modifier = _get_unit(m)
                self.units[matched_unit] += sgn*int(degree)
                self.value *= modifier**(sgn*int(degree))

    # ---------------------------------------- #

    def __str__(self):

        num_output = ['{}'.format(u) if d == 1 else '{}^{}'.format(u,d) if d > 1 else ''
                for u,d in self.units.items()]
        den_output = ['{}'.format(u) if d == -1 else '{}^{}'.format(u,d) if d < -1 else ''
                for u,d in self.units.items()]
        num_output = '*'.join([n for n in num_output if n != ''])
        den_output = '*'.join([n for n in den_output if n != ''])

        unit_dict = _unit_dict('')
        # decide where to put unit prefix
        if self.value == 0:
            new_value,prefix = 0,''
        elif len(num_output) > 0: # if there are units in the numerator
            acceptable_values = [(self.value/v,k) for k,v in unit_dict.items() 
                                if abs(self.value)/v > 0.1 and abs(self.value)/v <= 100]
            if len(acceptable_values) > 0:
                new_value,prefix = acceptable_values[0]
            else:
                new_value,prefix = (self.value,'')
        elif len(den_output) > 0:
            acceptable_values = [(self.value*v,k) for k,v in unit_dict.items() 
                                if abs(self.value)*v > 0.1 and abs(self.value)*v <= 100][0]
            if len(acceptable_values) > 0:
                new_value,prefix = acceptable_values[0]
            else:
                new_value,prefix = (self.value,'')
        else:
            new_value,prefix = self.value,''

        # take new value
        value_output = str(new_value)
        
        # treat output differently based on contents
        if num_output == '' and den_output == '':
            return value_output
        elif num_output == '':
            return '{} 1/{}{}'.format(value_output,prefix,den_output)
        elif den_output == '':
            return '{} {}{}'.format(value_output,prefix,num_output)
        else:
            return '{} {}{}/{}'.format(value_output,prefix,num_output,den_output)

    # ---------------------------------------- #

    def __add__(self,other):

        """ Add two units together, returns unit """

        self.unit_standard()
        other.unit_standard()

        if self.units != other.units:
            raise TypeError('Units not equal between added objects!')
       
        new_unit = _copy(self)
        new_unit.value += other.value

        return new_unit 

    def __radd__(self, other):

        """ Reverse add, compatibility for sum """

        if other == 0:
            return self
        else:
            return self.__add__(other)

    # ---------------------------------------- #

    def __sub__(self,other):

        """ Subtract two units together, returns unit """

        self.unit_standard()
        other.unit_standard()

        if self.units != other.units:
            raise TypeError('Units not equal between added objects!')

        new_unit = _copy(self)
        new_unit.value -= other.value

        return new_unit 

    # ---------------------------------------- #

    def __mul__(self,other):

        """ Multiply two units together, returns unit """

        new_unit = _copy(self)
        
        if isinstance(other,(int,float)):
            new_unit.value *= other
        else:
            new_unit.value *= other.value
            new_unit.units = _merge_dicts(new_unit.units,other.units,1)

        return new_unit 

    # ---------------------------------------- #

    def __div__(self,other):

        """ Divide two units together, returns unit """

        new_unit = _copy(self)


        if isinstance(other,(int,float)):
            other_value = other
            other_dict = {}
        else:
            other_value = other.value
            other_dict = other.units

        if other_value == 0:
            new_unit.value = float('inf')
        else:    
            new_unit.value /= other.value

        new_unit.units = _merge_dicts(new_unit.units,other_dict,-1)

        return new_unit 

    def __idiv__(self,other):

        """ Divide two units together, returns unit """

        self.value /= other.value
        self.units = _merge_dicts(self.units,other.units,-1)

        return self

    def __pow__(self,degree):

        new_unit = _copy(self)

        new_unit.value **= degree
        new_unit.units = dict([(k,v*degree) for k,v in new_unit.units.items()])

        return new_unit 

    # ---------------------------------------- #

    def unit_standard(self):

        """ Returns a standardized form of units """

        conversion = {
                'Da':'1 g/mol',
                'M':'1 mol/L'
                }

        for k,v in conversion.items():
            if self.units[k] != 0:
                self /= (Unit(v) ** -self.units[k])
                self.units[k] = 0

        return self 

    # ---------------------------------------- #

    def unit_display(self):

        """ Returns a standardized form of units """
        pass

    # ---------------------------------------- #

    def convert(self,conversions):

        """ Input object and list of tuples or dictionary """

        if isinstance(conversions,dict):
            conversions = conversions.items() 
        if isinstance(conversions,tuple):
            conversions = [conversions]

        for k,v in conversions:
            if self.units[k] != 0:
                self /= (Unit(v) ** -self.units[k])
                self.units[k] = 0

    # ---------------------------------------- #

    def is_unitless(self):
        """ Returns boolean if no units exist """
        return all([v == 0 for v in self.units.values()])

# ---------------------------------------- #
#             Internal Methods             #
# ---------------------------------------- #

def _get_unit(my_str):

    """ Get unit label from suffix """

    # 
    matches = [my_str.endswith(suffix) for suffix in _known_units]

    # check to see if unit makes sense
    if not any(matches):
        raise KeyError('Unit unit not recognized <{}>!'.format(my_str))

    # pick unit that matches, with prefix
    matched_unit = [unit for unit,match in zip(_known_units,matches) if match][0]
    unit_dict = _unit_dict(matched_unit)

    return matched_unit,unit_dict[my_str]

# ---------------------------------------- #

def _unit_dict(unit):

    """ Makes a dictionary to match unit label """

    return {
            'f' + unit : 1e-15,
            'p' + unit : 1e-12,
            'n' + unit :  1e-9,
            'u' + unit :  1e-6,
            'm' + unit :  1e-3,
            ''  + unit :   1e0,
            'k'  + unit :  1e3,
            'M'  + unit :  1e6
           }

# ---------------------------------------- #

def _merge_dicts(d1,d2,scalar=1):
    for k,v in d2.items():
        d1[k] += scalar*v
    return d1

# ---------------------------------------- #

if __name__ == '__main__':
    print Unit('5.0')
    print Unit('5.0 kg/m') / Unit('3')
    print Unit('5.0 Da') + Unit('0.05 kg/mol')
    print Unit('5.0 Da') - Unit('0.05 kg/mol')
    print Unit('3 uL')
    print Unit('5 g/mL')





