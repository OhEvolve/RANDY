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

    def __init__(self,database):

        """ initalize base protocol class """
        
        BaseProtocol.__init__(self)

        self.database = None
        self.requirements = {}

        
        # ... require a sequence that is a plasmid
        plasmid_req = {
                'class_name':'Sequence',
                'form':'plasmid'
                }
        
        # ... require cell to contain plasmid 
        cell_req = {
                'class_name':'Cell',
                'species':'E. coli',
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


    def io(self,input_dict):

        """ Pass input dictionary, return output dictionary """

        # check whether input requirements are met
        self.is_valid(input_dict) 

        # pull out cells in sample
        cells = [content for content in input_dict['sample'].contents 
                        if content.class_name == 'Cell']

        # pull out plasmids of E. coli cell types
        plasmids = sum([sum([content for content in cell.content if content.form == 'plasmid']) 
                               for cell in cells if cell.species == 'E. coli'])

        # add buffer EB
        output += self.database.load('Buffer EB',volume='50 uL')

        # return final sample
        return {'sample':output}











