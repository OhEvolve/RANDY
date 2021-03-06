# buffer.py

""" Class: container for matter objects """

#--------------------------------------#

# standard libraries

# nonstandard libraries

# homegrown libraries
from matter import Matter
from mixture import Mixture 

#--------------------------------------#

""" Main Class  """

class Buffer(Matter,Mixture):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """
        self.contents  = []                      # list to fill with matter
        self.instructions = ''                   # preparation instructions
        self.reagents = {}                       # reagents log

        Matter.__init__(self)                    # update with arguments
        Mixture.__init__(self)                   # update with arguments

        self.update(*args,**kwargs)     # update object attributes

        # list of features to print out on call
        self.features += ['instructions']

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



