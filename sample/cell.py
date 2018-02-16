# cell.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 


""" Main Class  """

class Cell(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.species = ''                        # species of population
        self.count = 0                           # cell count

        Matter.__init__(self)     # update with arguments

        self.update(*args,**kwargs)              # update object attributes

        self.features += ['species','count']     # add printed attributes

""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH',
            'species':'E. Coli'
            }

    sample = Cell(settings)
    print sample





