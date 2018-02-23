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
        self.requirements = {
                'sample':{}
                }


        
    # ---------- #

    def io(self,input_dict):

        """ pass input dictionary, returns output dictionary """

        raise NotImplementedError('IO method not implemented')

    # ---------- #

    def is_valid(self,input_dict):

        """ Checks whether input dictionary is valid """

        # makes sure all requirements are satisfied
        if not all([_check_attributes(self,self.requirements) for k,v in self.requirements]):
            raise AttributeError('Missing atleast one required attributes in input!')

        

# -------------------- #
#   Internal Methods   #
# -------------------- #

def _check_attributes(obj_list,attr_dict):

    """ Pass object and dictionary of attributes, recursively checks properties """

    # check whether objects are iterable containers
    if not isinstance(obj_list,(tuple,list)):
        obj_list = [obj_list] 

    # check that passed attribute is type dict
    if not isinstance(attr_dict,dict):
        raise TypeError('Passed non-dictionary to attribute check!')
    
    # iterate through attributes
    for k,v in attr_dict.items():

        # check recursively through attributes, checking for compatibility
        if not any([all([_check_attributes(getattr(obj,k),i) for i in v]) if hasattr(obj,k) and isinstance(v,(list,tuple))
            else getattr(obj,k) == v if hasattr(obj,k) else False for obj in obj_list]):
            return False

    # if there are no missing attributes
    return True












        


    











