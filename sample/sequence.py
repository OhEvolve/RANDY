# sequence.py

""" Class: any sequence object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 

# TODO:
# codon set support

""" Main Class  """

class Sequence(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.sequence      = ''                        # species of population
        self.codon_set     = 'standard'                # codon set (only supported: standard)
        self.elements      = {}                        # cell count
        self.weight        = (0.,'ng')              # cell count
        self.material      = 'dsDNA'                   # dsDNA,ssDNA,dsRNA,ssRNA

        Matter.__init__(self,*args,**kwargs)     # update with arguments

        self.features += ['weight','material']     # add printed attributes

    def __str__(self):
        """ Return string with description """
        base_str = super(Sequence, self).__str__() # get the base string from Matter subclass
        
        # add a sequence object with a ruler to measure
        ruler = ''.join(['{: <10}'.format(i) for i in xrange(1,len(self.sequence)+1,10)])
        description  = ['\nSequence:'] 
        description += ['\n'.join([ruler[i:i+self.cc],self.sequence[i:i+self.cc],''])
                for i in xrange(0,len(self.sequence),self.cc)]

        # returns joined object
        return base_str + '\n'.join(description)


""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH',
            'sequence':'CCCCCCCCCCCCCCCCCCCCCCCCCATATATATATATATAAAAAAAAAAAAAAAAAAAAAATTTTTTTTTTTTTTTTTTTTTTTTTTTGGGGGG'
            }

    sample = Sequence(settings)
    print sample





