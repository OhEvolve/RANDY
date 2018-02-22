# cell.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 
from sequence import Sequence 
from units import Unit

""" Main Class  """

class Cell(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.species = ''                                      # species of population
        self.count = 0                                         # cell count
        self.contents = [Sequence(name='gDNA',form='genomic')] # contents of cell

        Matter.__init__(self)                                  # update with arguments

        self.update(*args,**kwargs)                            # update object attributes

        self.features += ['species','count']                   # add printed attributes

    @property
    def count(self):
        """ Number of Moles Property """
        return self._count

    @count.setter
    def count(self,value):
        """ Mass Setter Property """
        # set moles of object 
        if not isinstance(value,Unit):  
            value = Unit(value)

        self._count = value


""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH',
            'species':'E. Coli'
            }

    sample = Cell(settings)
    print sample





