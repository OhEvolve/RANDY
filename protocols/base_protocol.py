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
        self.input_reqs     = 
                {
                'sample':{}
                }


        
    # ---------- #

    def io(self,input_dict):

        """ pass input dictionary, returns output dictionary """

        raise NotImplementedError('IO method not implemented')

    # ---------- #

    def is_valid():
        self._check_input_reqs()

    def _check_requirements(self):

        """ Checks inputs using requirements """

# -------------------- #
#   Internal Methods   #
# -------------------- #

def _check_attributes(obj_list,attr_dict):

    """ Pass object and dictionary of attributes, recursively checks properties """

    # check whether objects are iterable containers
    if not isinstance(obj,(tuple,list)):
        obj_list = [obj_list] 

    # check that passed attribute is type dict
    if not isinstance(attr_dict,dict):
        raise TypeError('Passed non-dictionary to attribute check!')
    
    # iterate through attributes
    for k,v in attr_dict.items():
        for obj in obj_list:
            if hasattr(obj,k):
                if isinstance(v,(list,tuple)):
                    pass 
                else:
                    if getattr(obj,k) == v

    return True















        


    











