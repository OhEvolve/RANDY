# mixture.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from units import add_units 

""" Main Class  """

class Mixture(object):

    def __init__(self):
        self.features += ['volume']

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
        self.volume
        

