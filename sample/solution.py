# solution.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 
from units import Unit

""" Main Class  """

class Solution(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.volume = '0 mL'                     # volume of solution

        Matter.__init__(self,*args,**kwargs)     # update with arguments

        self.update(*args,**kwargs)              # update object attributes

        self.features += ['volume']    # add printed attributes

    @property
    def volume(self):
        """ Volume Property """
        return self._volume

    @volume.setter
    def volume(self,value):
        """ Volume Setter Property """
        # set volume of object 
        if not isinstance(value,Unit):  
            value = Unit(value)

        self._volume = value
    

""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH',
            'volume':(100,'mL')
            }

    sample = Solution(settings)
    print sample





