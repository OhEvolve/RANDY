

"""
Testing Grounds
"""

class Subclass:
    def __init__(self,name):
        self.c = name
        
class Myclass(object):

    def __init__(self,contents):
        self.contents = contents

    def __repr__(self):
        return self.name 

def _check_attributes(obj_list,attr_dict):

    """ Pass object and dictionary of attributes, recursively checks properties """

    # check whether objects are iterable containers
    if not isinstance(obj,(tuple,list)):
        obj_list = [obj_list] 

    # check that passed attribute is type dict
    if not isinstance(attr_dict,dict):
        raise TypeError('Passed non-dictionary to attribute check!')
    
    # iterate through attributes
    all([any([hasattr(obj,k) for obj in obj_list]) for k,v in attr_dict.items()])
                    

    return True

# ... require cell to contain plasmid 
reqs = {
        'contents':[{name:'A'},{name:'B'}]
       }


mc = Myclass([Subclass('A'),Subclass('B')])

print _check_attributes(mc,reqs)


'''#

class Test(object):

    def __init__(self):
        self.mw = 5.0
        self._mass = 0.
        self._mols = 0.
        self.mols = 5

    @property
    def mass(self): 
        return self._mass

    @property
    def mols(self): 
        return self._mols 

    @mass.setter
    def mass(self,value):
        self._mass = value
        self._mols = value/self.mw


test = Test()

print test.mass,test.mols

setattr(test,'mass',5)

print test.mass,test.mols

#test.mols = 10

print test.mass,test.mols

#'''#



