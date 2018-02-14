# solute.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 


""" Main Class  """

class Solute(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.molecular_weight = 0.                      # molecular weight
        self.weight           = 0.                      # cell count

        Matter.__init__(self,*args,**kwargs)            # update with arguments

        self.features += ['molecular_weight','weight']  # add printed attributes

""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH',
            'molecular_weight':(15.,'g/mol'),
            'weight':(100,'g')
            }

    sample = Solute(settings)
    print sample





