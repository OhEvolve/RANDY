# mixture.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from solute import Solute
from units import add_units,subtract_units,divide_units,scale_unit

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
        return add_units(*volumes)

    @volume.setter
    def volume(self,new_volume):
        """ Setting volume changes contents! """
        # get scalar to change absolute values of contents
        scalar = divide_units(new_volume,self.volume)

        # iterate through contents and modify
        for content in self.contents:
            if hasattr(content,'volume'):
                content.volume = scale_unit(content.volume,scalar)
            elif hasattr(content,'mass'):
                content.mass = scale_unit(content.mass,scalar)
            else:
                raise AttributeError('Object missing mass/volume attributes!')

