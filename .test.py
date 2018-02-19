
"""
Testing Grounds
"""

# standard libraries
# nonstandard libraries
# homegrown libraries

global _known_units

# NOTE: This is a sortof hacky way to make sure complex units are assigned first
# i.e. g/mol is correctly assigned as g/mol, not mol (since both endwith X)
_known_units = ['g','L','mol','Da','M','m']
_known_units.sort(key = len,reverse=True) 

class Unit(object):

    def __init__(self,s):

        # make numerator/denominator dictionary
        self.units = dict([(unit,0) for unit in _known_units])

        s = s.split(' ') # split string
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

    def __str__(self):
        value_output = str(self.value)

        num_output = ['{}'.format(u) if d == 1 else '{}^{}'.format(u,d) if d > 1 else ''
                for u,d in self.units.items()]
        den_output = ['{}'.format(u) if d == -1 else '{}^{}'.format(u,d) if d < -1 else ''
                for u,d in self.units.items()]
        num_output = '*'.join([n for n in num_output if n != ''])
        den_output = '*'.join([n for n in den_output if n != ''])

        
        # treat output differently based on contents
        if num_output == '' and den_output == '':
            return value_output
        elif num_output == '':
            return '{} 1/{}'.format(value_output,den_output)
        elif den_output == '':
            return '{} {}'.format(value_output,num_output)
        else:
            return '{} {}/{}'.format(value_output,num_output,den_output)


    # unit
    def __add__(self,other):

        """ Add two units together, returns unit """

        if _standard(self.units) != _standard(other.units):
            raise TypeError('Units not equal between added objects!')
       
        self.value += other.value

        return self

    def __sub__(self,other):

        """ Subtract two units together, returns unit """

        if _standard(self.units) != _standard(other.units):
            raise TypeError('Units not equal between added objects!')

        self.value -= other.value

        return self

    def __mul__(self,other):

        """ Multiply two units together, returns unit """

        self.value *= other.value
        self.units = _merge_dicts(self.units,other.units,1)

        return self

    def __truediv__(self,other):

        """ Divide two units together, returns unit """

        self.value /= other.value
        self.units = _merge_dicts(self.units,other.units,-1)

        return self

def _standard(my_dict):

    """ Returns a standardized form of units """

    conversion = {
            'Da':(('g',1),('mol',-1)),
            'M':(('mol',1),('L',-1))
            }

    for k,v in conversion.items():
        if my_dict[k] != 0:
            for unit,degree in v:
                my_dict[unit] += my_dict[k]*degree
            my_dict[k] = 0

    return my_dict

def _

def _resolve(my_dict):
    pass

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


def _merge_dicts(d1,d2,scalar=1):
    for k,v in d2.items():
        d1[k] += scalar*v
    return d1

print Unit('5.0')
print Unit('5.0 kg/m') * Unit('3')
print Unit('5.0 Da') + Unit('0.05 kg/mol')
print Unit('5.0 Da') - Unit('0.05 kg/mol')
print Unit('3 uL')
print Unit('5 g/mL^3')


'''#

class Test(object):

    def __init__(self):
        self.mw = 5.0
        self._mass = 0.
        self._mols = 0.
        self.mols = 5

    @property
    def mass(self): 
        return self._mass

    @property
    def mols(self): 
        return self._mols 

    @mass.setter
    def mass(self,value):
        self._mass = value
        self._mols = value/self.mw


test = Test()

print test.mass,test.mols

setattr(test,'mass',5)

print test.mass,test.mols

#test.mols = 10

print test.mass,test.mols

#'''#



