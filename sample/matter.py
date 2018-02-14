# matter.py

""" Class: any physical object """

# standard libraries

# nonstandard libraries

# homegrown libraries


""" Main Class  """

class Matter(object):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """
        self.name  = ''                  # name of matter
        self.id    = id(self)            # ID of matter
        self.owner = ''                  # owner of sample 
        self.cc    = 80                  # center characters (#) [DISPLAY ONLY]

        # list of features to print out on call
        self.features = ['name','owner']

        self.update(*args,**kwargs) # update with arguments

    def __str__(self):
        """ Return string with description """
        description  = ['-- {} object --'.format(type(self).__name__)]
        description += ['{}: {}'.format(f.capitalize(),getattr(self,f))
                                           for f in self.features]
        return '\n'.join(description)

    def __repr__(self):
        """ Representation of object """
        return '{}({})'.format(type(self).__name__,self.name)

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


