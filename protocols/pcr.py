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
        
        BaseProtocol.__init__(self)


