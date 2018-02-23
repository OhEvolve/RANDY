
"""
Testing Grounds
"""

class Subclass:
    def __init__(self,name):
        self.name = name
        
class Myclass(object):

    def __init__(self,contents):
        self.contents = contents
        self.temp = 'mine'

####################

                    

# ... require cell to contain plasmid 
reqs = {
        'temp':'mie',
        'contents':[{'name':'A'},{'name':'B'}]
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



