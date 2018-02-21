# miniprep.py

"""
Protocol for Miniprep 
"""

"""
Inputs:
    sample (material: cells)

Outputs:
    sample (material: DNA)
"""

# standard libraries
# nonstandard libraries
# homegrown libraries
from base_protocol import BaseProtocol

class Miniprep(BaseProtocol):

    def __init__(self):

        """ initalize base protocl class """
        
        BaseProtocol.__init__(self)
        self.reqs = ['sample']

    def io(self):

        """ pass input dictionary, return output dictionary """

        self._check_inputs()
