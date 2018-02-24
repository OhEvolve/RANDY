# matter.py

""" Class: any physical object """

# standard libraries

# nonstandard libraries

# homegrown libraries
import sample

""" Main Class  """

class Matter(object):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """
        self.name  = ''                             # name of matter
        self.class_name = self.__class__.__name__   # class name
        self.id    = id(self)                       # ID of matter
        self.owner = ''                             # owner of sample 
        self.cc    = 40                             # center characters (#) [DISPLAY ONLY]

        # list of features to print out on call
        self.features = ['name','owner']

        self.update(*args,**kwargs) # update with arguments

    def __add__(self,other):
        """ Add matter to matter, returns sample object """
        # check if you are adding two things that are matter
        if not issubclass(type(other),Matter):
            raise TypeError('Sample can only add Matter objects')

        result = sample.Sample(contents=[self,other])

        return result 

    def __iadd__(self,other):
        """ Add matter to self, returns sample object """

        # check if you are adding two things that are matter
        if not issubclass(type(other),Matter):
            raise TypeError('Sample can only add Matter objects')

        result = sample.Sample(contents=[self,other])
        return result 

    def __radd__(self, other):

        """ Reverse add, compatibility for sum """

        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        """ Return string with description """
        description  = ['-- {} object --'.format(type(self).__name__)]
        description += ['{}: {}'.format(f.capitalize(),getattr(self,f))
                                           for f in self.features]
        return '\n'.join([d.center(self.cc) for d in description])

    def __repr__(self):
        """ Representation of object """
        return '{}({})'.format(type(self).__name__,self.name)

    def __call__(self,*args,**kwargs):
        """ Update objects with args/kwargs """
        self.update(*args,**kwargs) 

    def update(self,*args,**kwargs):
        """ Update objects with args/kwargs """
        for arg in args+(kwargs,): # iterate through arguments

            if not isinstance(arg,dict): # check argument is dictionary
                raise TypeError('Object passed non-<dict> argument')

            for key,value in arg.items(): # iterate through dictionary items

                if not hasattr(self,key): # ch
                    raise AttributeError('Object missing attribute ({})'.format(key)) 
                setattr(self,key,value)


""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'owner':'PVH'
            }

    sample = Matter(settings)
    print sample


