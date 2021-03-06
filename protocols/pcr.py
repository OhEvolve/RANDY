# pcr.py

"""
Protocol for PCR
"""

"""
Inputs:
    sample (material: ssDNA,dsDNA)

Outputs:
    sample (increased ssDNA,dsDNA conc.)
"""

# standard libraries
# nonstandard libraries
# homegrown libraries
from base_protocol import BaseProtocol

class PCR(BaseProtocol):

    def __init__(self):

        """ initalize base protocl class """
        
        BaseProtocol.__init__(self)
        self.reqs = ['sample','primers','polymerase']

    def io(self):

        """ pass input dictionary, return output dictionary """
        
        self.is_valid()

    def _check_output(self):

        if any([content in sample.contents]):
        self._check_inputs()


