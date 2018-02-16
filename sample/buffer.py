# buffer.py

""" Class: container for matter objects """

#--------------------------------------#

# standard libraries

# nonstandard libraries

# homegrown libraries
from matter import Matter

#--------------------------------------#

""" Main Class  """

class Buffer(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """
        self.contents  = []                      # list to fill with matter
        self.volume = 0.                         # volume of buffer
        self.instructions = ''                   # preparation instructions
        self.reagents = {}                       # reagents log

        Matter.__init__(self,*args,**kwargs)     # update with arguments

        # list of features to print out on call
        self.features += ['instructions','reagents']

        self.update(*args,**kwargs)              # update with arguments

    def __str__(self):
        """ Return string with description """
        base_str = super(Buffer, self).__str__() # get the base string from Matter subclass

        # add short thing
        description = '\nContents: (' + ','.join((
            repr(content) for content in self.contents)) + ')'
        
        # rejoin list
        return base_str + description



#--------------------------------------#

""" Unit tests """

if __name__ == "__main__":

    from solute import Solute
    from solution import Solution

    settings = {
            'name':'sample001',
            }

    sample = Sample(settings)
    print sample



