

"""
Testing Grounds
"""

class Hello:

    def __init__(self,name):
        self.name = name 

    def __repr__(self):
        return self.name 


print Hello('hello')
print Hello(None)
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



