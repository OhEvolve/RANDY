# solution.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 


""" Main Class  """

class Solution(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.reagent = ''                        # reagent label
        self.volume = '0 mL'                     # volume of reagent

        Matter.__init__(self,*args,**kwargs)     # update with arguments

        self.features += ['reagent','volume']    # add printed attributes

    def remove(self):
        pass

""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH',
            'volume':(100,'mL')
            }

    sample = Solution(settings)
    print sample





