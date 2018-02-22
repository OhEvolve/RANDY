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

        self.requirements = {}

        
        # ... require a sequence that is a plasmid
        plasmid_req = {
                'class_name':'Sequence',
                'form':'plasmid'
                }
        
        # ... require cell to contain plasmid 
        cell_req = {
                'class_name':'Cell',
                'contents':[plasmid_req]
                }

        # ... require sample to contain cell
        sample_req = {
                'contents':[cell_req]
                }

        # create final requirements
        self.requirements = {
                'sample':sample_req
                }


    def io(self):

        """ pass input dictionary, return output dictionary """

        self._check_inputs()
