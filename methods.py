
"""

Common internal methods used throughout protocols

"""

# standard libraries

# nonstandard libraries
#import openpyxl
#from openpyxl.utils import get_column_letter

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

def subtract_volume(sample

def convert_units(unit,total):

    """ Convert volume units """

    units = _volume_units()
    units = _mass_units()

    if unit[1] == 'X':
        unit = (total[0]/float(unit[0]),total[1])
    else:
        assert unit[1] in units.keys(),'units not recognized ({})'.format(unit[1])

    unit_converts = [(unit[0]*units[unit[1]]/v,k) for k,v in units.items()]
    unit_converts = [(k,v) for k,v in unit_converts if k >= 0.1 and k < 100]

    if len(unit_converts) != 1: print 'Something is wrong:',unit_converts

    return unit_converts[0]

#--------------------------------------#

def fill_reaction(total,*args):

    """ Finds how to fill reaction to total """

    units = _volume_units()

    reagent_units = [v[0]*units[v[1]]/units[total[1]] for k,v in args]

    return (total[0] - sum(reagent_units),total[1])


#--------------------------------------#
# TODO: consider faster alternatives (no indexing)
#--------------------------------------#

def comp(seq):

    """ Complement input sequence """

    assert isinstance(seq,str),"submitted sequence is not str"
    seq_map = _seq_map()
    return ''.join(seq_map[seq[i]] for i in xrange(len(seq)))

#--------------------------------------#

def rcomp(seq):

    """ Complement input sequence """

    assert isinstance(seq,str),"submitted sequence is not str"
    seq_map = _seq_map()
    return ''.join(seq_map[seq[len(seq) - i - 1]] for i in xrange(len(seq)))

#--------------------------------------#
#           Internal Methods           #
#--------------------------------------#

def _seq_map():

    # TODO: expand mapping to include degenerative codons

    return {'A':'T','T':'A',
            'C':'G','G':'C',
            'N':'N',' ':' ',
            '|':'|','-':'-'}

#--------------------------------------#

def _volume_units():

    """ Volume units dictionary """

    return {
            'nL':1e-9,
            'uL':1e-6,
            'mL':1e-3,
            'L' : 1e0
           }

def _mass_units():

    """ Mass units dictionary """

    return {
            'ng': 1e-9,
            'ug': 1e-6,
            'mg': 1e-3,
            'g' :  1e0,
            'kg':  1e3
           }

#--------------------------------------#

def _normalize_dict(my_dict):
    new_dict = {}

    # iterate through dictionary items
    for k,v in my_dict.items():

        # check if float
        try:
            new_dict[str(k).lower()] = float(v)

            continue
        except ValueError:
            pass

        # check if list of strs 
        if v.strip(' ').startswith('[') and v.strip(' ').endswith(']'):
            try:
                new_dict[str(k).lower()] = [float(i) for i in v[1:-1].split(',')]
                continue
            except ValueError:
                new_dict[str(k).lower()] = [str(i).strip(' ') for i in v[1:-1].split(',')]
                continue
        else:
            new_dict[str(k).lower()] = str(v).strip(' ')

    # returns new dictionary
    return new_dict

#--------------------------------------#
#               Testing                #
#--------------------------------------#

if __name__ == "__main__":
    seq = 'AAATTTCCCGGGATCG'
    print seq
    print comp(seq)
    print rcomp(seq)
