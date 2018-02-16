# mixture.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from methods import unit_sum

""" Main Class  """

class Mixture(object):

    @property
    def volume(self):

        """ Trigger property """
        # check for contents
        if not hasattr(self,contents):
            raise AttributeError('Mixture object missing contents!')

        # access the volume of each component of mixture
        volumes = [content.volume for content in self.contents
                    if hasattr(content,'volume')]

        # return summed components
        return sum_units(volumes)

