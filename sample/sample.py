# sample.py

""" Class: container for matter objects """

#--------------------------------------#

# standard libraries

# nonstandard libraries

# homegrown libraries
from matter import Matter
from mixture import Mixture 

#--------------------------------------#

""" Main Class  """

class Sample(Matter,Mixture):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """
        self.container = ''                  # container for sample
        self.contents  = []                  # list to fill with matter

        Matter.__init__(self)                    # update with arguments
        Mixture.__init__(self)                   # update with arguments

        self.update(*args,**kwargs)     # update object attributes

        self.volume = self.volume

        # list of features to print out on call
        self.features += ['container']

    def split(self,volume):
        """ Split sample into a new population with a certain volume """

    def __add__(self,other):
        """ Add matter to sample """ 
        # check that the added object is the Matter class

        if not issubclass(type(other),Matter):
            raise TypeError('Sample can only add Matter objects')

        self.contents.append(other)
        return self 

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
        base_str = super(Sample, self).__str__() # get the base string from Matter subclass

        description  = ['','Contents:'.center(self.cc)]
        description += [self.cc*'-']

        # list contents
        if len(self.contents) == 0:
            description += ['(empty)']
        else:
            for content in self.contents:
                description += [repr(content)]
                #description += [self.cc*'-']

        description = [d.center(self.cc) for d in description] # center each line
        
        # rejoin list
        return base_str + '\n' + '\n'.join(description)
    

#--------------------------------------#

#--------------------------------------#

""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'container':'10mL tube'
            }

    sample = Sample(settings)
    print sample



