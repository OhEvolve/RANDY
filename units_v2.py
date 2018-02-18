# units_v2.py

"""
Module to take care of everything related to units
"""

# standard libraries

# nonstandard libraries
import units.predefined

# homegrown libraries

#--------------------------------------#
#           Main     Methods           #
#--------------------------------------#

class Unit(object):
    def __init__(self,unit_str):

        # split up string
        unit_list = _2list(unit_str)

        # store value 
        value = unit_list[0]

    def __str__(self):

        if len(self.denominator) > 0:
            return '{} {}{}/{}'.format(
                    self.value,
                    '*'.join(self.numerator),
                    '*'.join(self.denominator))

        else:
            return '{} {}{}/{}'.format(
                    self.value,
                    '*'.join(self.numerator),
                    '*'.join(self.denominator))


def add_units(*args):
    """ Subtract two units from each other """
    print units.predefined.define_base_si_units('m')

#--------------------------------------#

def _get_unit(unit):

    """ Get unit label from suffix """

    if isinstance(type(unit),str): # if unit is str 
        unit = _2list(unit) # convert to string

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

def _2list(unit):
    """ Convert unit str to list """
    if not isinstance(unit,str):
        raise TypeError('Input required as <str>!')
    unit = unit.split(' ') 
    return [float(unit[0]),unit[1]]

#--------------------------------------#

def subtract_units(unit1,unit2):
    """ Subtract two units from each other """
    pass

#--------------------------------------#

def divide_units(unit1,unit2):
    """ Subtract two units from each other """
    pass

#--------------------------------------#

def scale_unit(unit,scalar):
    """ Scale a unit by a scalar """
    pass

#--------------------------------------#

def mol2mass(moles,mw):
    pass

#--------------------------------------#

def mass2mol(mass,mw):
    pass 

#--------------------------------------#
# TODO: consider faster alternatives (no indexing)
#--------------------------------------#


#--------------------------------------#
#          Factory Methods             #
#--------------------------------------#


#--------------------------------------#
#               Testing                #
#--------------------------------------#

if __name__ == "__main__":

    print add_units('1 mL','10 uL','100 uL','20 mL')
    print subtract_units('1 mL','10 uL')
    print divide_units('1 mL','15 uL')

    mw = '13 Da'
    mass = '1 ug'
    
    mols = mass2mol(mass,mw)
    new_mass = mol2mass(mols,mw)

    print mols
    print new_mass



