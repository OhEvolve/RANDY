# units.py

"""
Module to take care of everything related to units
"""

# standard libraries

# nonstandard libraries

# homegrown libraries

#--------------------------------------#
#           Main     Methods           #
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

def mol2mass(moles,mw):
    """ Inputs two strings, returns string (mass) """
    mw_unit = _get_unit(mw)         # get basic unit
    mw_dict = _unit_dict(mw_unit)    # get unit dictionary
    mw = _2list(mw)           # convert str to list

    moles_unit = _get_unit(moles)         # get basic unit
    moles_dict = _unit_dict(moles_unit)    # get unit dictionary
    moles = _2list(moles)           # convert str to list

    # check that the units make sense
    if not mw_unit in ['Da','g/mol']:
        raise KeyError('Unit unit not recognized <{}>!'.format(mw_unit))
    if not moles_unit in ['mol']:
        raise KeyError('Unit unit not recognized <{}>!'.format(moles_unit))

    # multiply the units, return formated output
    unit_count = moles[0]*mw[0]*moles_dict[moles[1]]*mw_dict[mw[1]]
    return _output([unit_count,'g'],_unit_dict('g'))

#--------------------------------------#

def mass2mol(mass,mw):
    """ Inputs two strings, returns string (mass) """
    mw_unit = _get_unit(mw)         # get basic unit
    mw_dict = _unit_dict(mw_unit)    # get unit dictionary
    mw = _2list(mw)           # convert str to list

    mass_unit = _get_unit(mass)         # get basic unit
    mass_dict = _unit_dict(mass_unit)    # get unit dictionary
    mass = _2list(mass)           # convert str to list

    # check that the units make sense
    if not mw_unit in ['Da','g/mol']:
        raise KeyError('Unit unit not recognized <{}>!'.format(mw_unit))
    if not mass_unit in ['g']:
        raise KeyError('Unit unit not recognized <{}>!'.format(mass_unit))

    # multiply the units, return formated output
    unit_count = (mass[0]*mass_dict[mass[1]])/(mw[0]*mw_dict[mw[1]])
    return _output([unit_count,'mol'],_unit_dict('mol'))

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

def _check_unit_compatibility(*args):
    """ Checks that extracted units from suffixes are all equal """
    return _check_equal_list((_get_unit(arg) for arg in args))

#--------------------------------------#

def _get_unit(unit):

    """ Get unit label from suffix """

    if isinstance(type(unit),list): # if unit is list
        unit = _2str(unit) # convert to string

    # get array of matches to known units
    known_units = ['g','M','mol','L','Da','g/mol']
    # NOTE: This is a sortof hacky way to make sure complex units are assigned first
    # i.e. g/mol is correctly assigned as g/mol, not mol (since both endwith X)
    known_units.sort(key = len,reverse=True) 
    matches =     [unit.endswith(suffix) for suffix in known_units]

    # check to see if unit makes sense
    if not any(matches):
        raise KeyError('Unit unit not recognized <{}>!'.format(unit))

    # pick unit that matches
    return [unit for unit,match in zip(known_units,matches) if match][0]

#--------------------------------------#

def _unit_dict(suffix):

    """ Makes a dictionary to match unit label """

    matched_unit = _get_unit(suffix)
    
    return {
            'f' + matched_unit : 1e-15,
            'p' + matched_unit : 1e-12,
            'n' + matched_unit :  1e-9,
            'u' + matched_unit :  1e-6,
            'm' + matched_unit :  1e-3,
            ''  + matched_unit :   1e0,
            'k'  + matched_unit :  1e3,
            'M'  + matched_unit :  1e6
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

    mw = '13 Da'
    mass = '1 ug'
    
    mols = mass2mol(mass,mw)
    new_mass = mol2mass(mols,mw)

    print mols
    print new_mass



