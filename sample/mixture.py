# mixture.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from solute import Solute
from units import Unit

""" Main Class  """

class Mixture(object):

    def __init__(self):
        self.features += ['volume']

    def update_solutes(self):
        """ Update the concentrations of solutes in mixture """
        for content in self.contents:
            # check if object is solute
            if issubclass(content,Solute):
                content._concentration = divide_units, 

    @property
    def volume(self):
        """ Auto-calculate volume from contents """
        # check for contents
        if not hasattr(self,'contents'):
            raise AttributeError('Mixture object missing contents!')

        # access the volume of each component of mixture
        volumes = [content.volume for content in self.contents
                    if hasattr(content,'volume')]

        # return summed components
        self._volume = sum(volumes)
        return self._volume

    @volume.setter
    def volume(self,new_volume):
        """ Setting volume changes contents! """
        # get scalar to change absolute values of contents
        if not isinstance(new_volume,Unit):
            new_volume = Unit(new_volume)
        
        # find scalar to modify contents
        scalar = new_volume/self.volume

        # check to see if division worked correctly
        if not scalar.is_unitless():
            raise TypeError('New volume does not have compatible units!')

        # iterate through contents and modify
        for content in self.contents:
            if hasattr(content,'volume'):
                content.volume = scalar*content._volume
            elif hasattr(content,'mass'):
                content.mass = scalar*content._mass
                content.total_volume = new_volume
            elif hasattr(content,'count'):
                content.count = scalar*content._count
            else:
                raise AttributeError('Object missing mass/volume attributes!')

    def display_contents(self):
        """ Print contents of mixture """
        for i,content in enumerate(self.contents):
            print 'Component {}:\n{}'.format(i+1,content)






