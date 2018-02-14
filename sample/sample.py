# sample.py

""" Class: container for matter objects """

#--------------------------------------#

# standard libraries

# nonstandard libraries

# homegrown libraries
from matter import Matter

#--------------------------------------#

""" Main Class  """

class Sample(object):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """
        self.name      = ''                  # name of sample 
        self.container = ''                  # container for sample
        self.contents  = []                  # list to fill with matter
        self.cc        = 80                  # center characters (#) [DISPLAY ONLY]

        # list of features to print out on call
        self.features = ['name','container']

        self.update(*args,**kwargs) # update with arguments

    def split(self,volume):
        """ Split sample into a new population with a certain volume """

    def __iadd__(self,other):
        """ Add matter to sample """ 
        # check that the added object is the Matter class
        if not issubclass(type(other),Matter):
            raise TypeError('Sample can only add Matter objects')

        # place object in contents
        self.contents.append(other)
        return self

    def __str__(self):
        """ Return string with description """
        description  = ['-- {} object --'.format(type(self).__name__)]
        description += ['{}: {}'.format(f.capitalize(),getattr(self,f))
                                           for f in self.features]
        description += ['\nContents:']
        description += [self.cc*'-']

        # list contents
        if len(self.contents) == 0:
            description += ['(empty)']
        else:
            for content in self.contents:
                description += [str(content)]
                description += [self.cc*'-']
        
        # rejoin list
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

#--------------------------------------#

""" Main Class  """

def _subtract_volume(sample,volume):

#--------------------------------------#

""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'container':'10mL tube'
            }

    sample = Sample(settings)
    print sample



