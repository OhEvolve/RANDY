# base_protocol.py

"""
Base Protocol
Function: Basic class for which each protocol is built from
"""


# 

class BaseProtocol(object):

    def __init__(self):

        """ initialize base protocol class """

        self.execution_time = None                   # time to execute protocol

        self.inputs         = {'sample': None}       # input dictionary
        self.outputs        = {'sample': None}       # output dictionary

        # required keys in input dictionary
        self.input_reqs     = {
                'sample':{

        
    # ---------- #

    def io(self,input_dict):

        """ pass input dictionary, returns output dictionary """

        raise NotImplementedError('IO method not implemented')

    # ---------- #

    def is_valid():
        self._check_input_reqs()
        self._check_intended_output()

    def _check_input(self):

        """ Checks inputs using requirements """

        if not all([input_req in self.inputs for input_req in self.reqs]):
            raise KeyError('Input dictionary does not contain all necessary keys!') 

    def _check_output(self):
        
        if : # include cases for improper usage
            raise Warning('Inputs missing expected contents, may not result in intended output')

    def _check_contents(self)
    





