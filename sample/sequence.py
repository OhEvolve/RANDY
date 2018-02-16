# sequence.py

""" Class: any sequence object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 
from solute import Solute 

# TODO:
# codon set support

""" Main Class  """

class Sequence(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.sequence      = ''                        # species of population
        self.codon_set     = 'standard'                # codon set (only supported: standard)
        self.elements      = {}                        # cell count
        self.weight        = '0 ug'                    # cell count
        self.material      = 'dsDNA'                   # dsDNA,ssDNA,dsRNA,ssRNA
        self.shape         = 'linear'                  # circular

        Matter.__init__(self)           # add class features
        Solute.__init__(self)           # add class features

        self.update(*args,**kwargs)     # update object attributes

        self.features += ['weight','material']     # add printed attributes

    def __str__(self):
        """ Return string with description """
        base_str = super(Sequence, self).__str__() # get the base string from Matter subclass
        
        # add a sequence object with a ruler to measure
        ruler = ''.join(['{: <10}'.format(i) for i in xrange(1,len(self.sequence)+1,10)])
        description  = ['','Sequence:'.center(self.cc)] 
        description += ['\n'.join([ruler[i:i+self.cc],self.sequence[i:i+self.cc],''])
                for i in xrange(0,len(self.sequence),self.cc)]

        # returns joined object
        return base_str + '\n' + '\n'.join(description)

    @property
    def molecular_weight(self):
        """ Calculate molecular weight based on stuff """

        return self._molecular_weight

    @molecular_weight.setter
    def molecular_weight(self,value):
        """ Block molecular weight changes """

        # if the sequence is empty, return nothing to prevent property calls
        if len(self.sequence) == 0: 
            return None

        # else
        



""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH',
            'sequence':'CCCCCCCCCCCCCCCCCCCCCCCCCATATATATATATATAAAAAAAAAAAAAAAAAAAAAATTTTTTTTTTTTTTTTTTTTTTTTTTTGGGGGG'
            }

    sample = Sequence(settings)
    print sample





