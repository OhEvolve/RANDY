# sequence.py

""" Class: any sequence object """

# standard libraries
# nonstandard libraries
from Bio.SeqUtils import molecular_weight

# homegrown libraries
from matter import Matter 
from solute import Solute 
from units import Unit

# TODO:
# codon set support

""" Main Class  """

class Sequence(Solute):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.sequence      = ''                        # species of population
        self.codon_set     = 'standard'                # codon set (only supported: standard)
        self.elements      = {}                        # elements to display in your sequence
        self.material      = 'dsDNA'                   # dsDNA,ssDNA,dsRNA,ssRNA
        self.shape         = 'linear'                  # linear,circular 

        Matter.__init__(self)           # add class features
        Solute.__init__(self)           # add class features

        self.update(*args,**kwargs)     # update object attributes

        self.features += ['material','total_volume']     # add printed attributes

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

        if len(self.sequence) == 0: 
            return 0 

        # get the material type
        if 'DNA' in self.material: seq_type = 'DNA'
        elif 'RNA' in self.material: seq_type = 'RNA'
        elif 'protein' in self.material: seq_type = 'protein'

        # get double stranded state
        if 'ds' in self.material: double_stranded = True 
        else: double_stranded = False

        # get circular state
        circular = (self.shape == 'circular')
    
        # find MW value
        mw = molecular_weight(
                 self.sequence,
                 seq_type=seq_type,
                 double_stranded=double_stranded,
                 circular=circular)

        # create unit object
        self._molecular_weight = Unit('{} g/mol'.format(mw))

        # return value with unit
        return self._molecular_weight
                

    @molecular_weight.setter
    def molecular_weight(self,value):
        """ Block molecular weight changes """
        pass 







""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH',
            'sequence':'CCCCCCCCCCCCCTAAAAAAAAAAAAAAAAAAAAAATTTTTTTTTTTTTTTTTTTTTTTTTTTGGGGGG'
            }

    sample = Sequence(settings)
    print sample





