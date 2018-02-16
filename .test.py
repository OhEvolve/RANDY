
"""
Testing Grounds
"""

import collections

def _get_mw(sequence,material,shape):

    counter = collections.Counter(sequence) # count occurances of monomers
    base_mw = _get_mw_base(sequence,material,shape)
    _mw_dict = _get_mw_dict()
    return base_mw + sum([v*_mw_dict[material][k] for k,v in counter.items()]) # use dict to get mw

def _get_mw_dict():
    return {
            'ssDNA':
            {
                'A':313.21,
                'T':304.20,
                'C':289.18,
                'G':329.21
            },
            'dsDNA':
            {
                'A':618.39,
                'T':618.39,
                'C':617.41,
                'G':617.41
            },
            'ssRNA':
            {
                'A':313.21,
                'T':304.20,
                'C':289.18,
                'G':329.21
            }
           }

def _get_mw_base(sequence,material,shape):
    if material == 'protein':
        return 0. # TODO: fill
    if material == 'ssDNA':
        if shape == 'linear':

        return 0. # TODO: fill
    if material == 'dsDNA':
        return  # TODO: fill
    if material == 'ssRNA':
        return 159.0 # TODO: fill


            (An × 313.2) + (Tn × 304.2) + (Cn × 289.2) + (Gn × 329.2) + 79

count_occurances('ATCGAGATAGGGCGCGC')














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



