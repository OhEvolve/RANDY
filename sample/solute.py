# solute.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 
from units import Unit

""" Main Class  """

class Solute(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self.molecular_weight = 0                        # molecular weight

        self._mass          = 0                          # mass of solute
        self._moles         = 0                          # mols of solute
        self._total_volume  = 0                          # hidden variable, for translating conc.

        self._concentration = 0                          # mass/volume of solute
        self._molarity      = 0                          # mols/volume of solute

        Matter.__init__(self)                            # update with arguments

        self.update(*args,**kwargs)                      # update object attributes

        # add printed attributes
        self.features += ['molecular_weight','mass','moles','concentration','molarity']  

    # ---------- #

    @property
    def total_volume(self):
        """ Mass Property """
        return self._total_volume

    @total_volume.setter
    def total_volume(self,value):
        """ Solution Volume Setter Property """
        self._total_volume = Unit(value)

        # check if any of these exist
        for key in ('moles','mass'):
            if getattr(self,key) != None:
                self.refresh_attributes(key)
                return None

    # ---------- #

    @property
    def mass(self):
        """ Mass Property """
        return self._mass

    @mass.setter
    def mass(self,value):
        """ Mass Setter Property """
        self._mass = Unit(value)
        self.refresh_attributes('mass')

    # ---------- #

    @property
    def moles(self):
        """ Number of Moles Property """
        return self._moles

    @moles.setter
    def moles(self,value):
        """ Moles Setter Property """
        self._moles = Unit(value)
        self.refresh_attributes('moles')

    # ---------- #

    @property
    def concentration(self):
        """ concentration Property """
        return self._concentration

    @concentration.setter
    def concentration(self,value):
        """ Moles Setter Property """
        self._concentration = Unit(value)
        self.refresh_attributes('concentration')

    # ---------- #

    @property
    def molarity(self):
        """ Molarity Property """
        return self._molarity

    @molarity.setter
    def molarity(self,value):
        """ Molarity Setter Property """
        self._molarity = Unit(value)
        self.refresh_attributes('molarity')

    # ---------- #

    @property
    def molecular_weight(self):
        """ Molecular Weight Property """
        return self._molecular_weight

    @molecular_weight.setter
    def molecular_weight(self,value):
        """ Molecular Weight Setter Property """
        self._molecular_weight = Unit(value) 

    # ---------- #

    def refresh_attributes(self,attr):

        """ Refreshes moles/mass/molarity/concentration attributes """

        # fill mass/molarity relationship
        if not self.molecular_weight == 0:
            if attr == 'moles':            
                self._mass  = self.moles*self.molecular_weight
            elif attr == 'mass':           
                self._moles = self.mass/self.molecular_weight
            elif attr == 'molarity':       
                self._concentration = self.molarity*self.molecular_weight
            elif attr == 'concentration':  
                self._molarity= self.concentration/self.molecular_weight

        # if volume is available, fill remaining
        if not self.total_volume == 0:
            if attr in ['moles','mass']:
                self._molarity      = self.moles/self.total_volume
                self._concentration = self.mass/self.total_volume
            elif attr in ['molarity','concentration']:
                self._moles = self.molarity*self.total_volume
                self._mass  = self.molarity*self.total_volume

        else:
            if attr in ['moles','mass']:
                self._molarity,self._concentration = 0,0
            elif attr in ['molarity','concentration']:
                self._moles,self._mass = 0,0


""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'molecular_weight':'12 g/mol'
            }

    sample = Solute(settings)





