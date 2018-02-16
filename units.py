# units.py

"""
Module to take care of everything related to units
"""

# standard libraries

# nonstandard libraries

# homegrown libraries

#--------------------------------------#
#           External Methods           #
#--------------------------------------#

def load_reagent(name):
    pass

def load_sequence(name):
    pass

def load_enzyme(name):
    pass

#--------------------------------------#

def add_units(*units):
    """ Subtract two units from each other """
    # check that units are compatible between unit/unit2
    if len(units) == 0: 
        return None
    _check_unit_compatibility(*units)

    # get unit dictionary
    unit_dict = _unit_dict(units[0])
    units = tuple(_2list(u) for u in units)

    # subtract using unit conversion
    new_unit = units[0]
    new_unit[0] += sum([u[0]*unit_dict[u[1]]/unit_dict[new_unit[1]]
        for u in units[1:]])

    # package and return string unit
    return _output(new_unit,unit_dict)

#--------------------------------------#

def subtract_units(unit1,unit2):
    """ Subtract two units from each other """
    # check that units are compatible between unit/unit2
    _check_unit_compatibility(unit1,unit2)

    # get unit dictionary
    unit_dict = _unit_dict(unit1)
    unit1,unit2 = _2list(unit1),_2list(unit2)

    # subtract using unit conversion
    unit3 = [unit1[0] - unit2[0]*unit_dict[unit2[1]]/unit_dict[unit1[1]],unit1[1]]

    # package and return string unit
    return _output(unit3,unit_dict)

#--------------------------------------#

def convert_units(unit,total):

    """ Convert volume units """

    units = _volume_units()

    if unit[1] == 'X':
        unit = (total[0]/float(unit[0]),total[1])
    else:
        assert unit[1] in units.keys(),'units not recognized ({})'.format(unit[1])

    unit_converts = [(unit[0]*units[unit[1]]/v,k) for k,v in units.items()]
    unit_converts = [(k,v) for k,v in unit_converts if k >= 0.1 and k < 100]

    if len(unit_converts) != 1: print 'Something is wrong:',unit_converts

    return unit_converts[0]

#--------------------------------------#
# TODO: consider faster alternatives (no indexing)
#--------------------------------------#


def _2list(unit):
    """ Convert unit str to list """
    if not isinstance(unit,str):
        raise TypeError('Input required as <str>!')
    unit = unit.split(' ') 
    return [float(unit[0]),unit[1]]

def _2str(unit):
    """ Convert unit list to str """
    if not isinstance(unit,list):
        raise TypeError('Input required as <list>!')
    return ' '.join([str(u) for u in unit])

def _output(unit,unit_dict):
    """ Converts unit list to usable form """
    if not isinstance(unit,list):
        raise TypeError('Input required as <list>!')
    # convert unit, and pass str out
    unit_converts = [(unit[0]*unit_dict[unit[1]]/v,k) for k,v in unit_dict.items()]
    unit_converts = [[k,v] for k,v in unit_converts if k >= 0.1 and k < 100.0]

    return _2str(unit_converts[0])

#--------------------------------------#

def _standardize_units(unit,*args):
    """ standardizes all units to the first """

    # 
    unit_dict = _unit_dict(unit)



    return unit,args 

#--------------------------------------#

def _check_unit_compatibility(*args):
    """ Checks that extracted units from suffixes are all equal """
    return _check_equal_list((_get_unit(arg) for arg in args))

#--------------------------------------#

def _get_unit(suffix):

    """ Get unit label from suffix """

    # get array of matches to known units
    known_units = ['g','M','mol','L']
    matches =     [suffix.endswith(unit) for unit in known_units]

    # check to see if suffix makes sense
    if not any(matches):
        raise KeyError('Unit suffix not recognized <{}>!'.format(suffix))

    # pick unit that matches
    return [unit for unit,match in zip(known_units,matches) if match][0]

#--------------------------------------#

def _unit_dict(suffix):

    """ Makes a dictionary to match unit label """

    matched_unit = _get_unit(suffix)
    
    return {
            'n' + matched_unit : 1e-9,
            'u' + matched_unit : 1e-6,
            'm' + matched_unit : 1e-3,
            ''  + matched_unit :  1e0,
            'k'  + matched_unit :  1e3
           }

#--------------------------------------#
#          Factory Methods             #
#--------------------------------------#


def _check_equal_list(iterator):
    """ Check that all elements in list are equal """
    return len(set(iterator)) <= 1

#--------------------------------------#
#               Testing                #
#--------------------------------------#

if __name__ == "__main__":
    print subtract_units('1 mL','10 uL')
    print add_units('1 mL','10 uL','100 uL','20 mL')

