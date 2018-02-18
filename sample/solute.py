# solute.py

""" Subclass: any physical object """

# standard libraries
# nonstandard libraries
# homegrown libraries
from matter import Matter 
from units import mass2mol,mol2mass,_2str,_2list

""" Main Class  """

class Solute(Matter):
    
    def __init__(self,*args,**kwargs):
        """ Initialization of object """

        self._molecular_weight = None                    # molecular weight

        self._mass          = '0 g'                      # mass of solute
        self._moles         = '0 mol'                    # mols of solute

        self._concentration = 'unknown'                  # mass/volume of solute
        self._molarity      = 'unknown'                  # mols/volume of solute

        Matter.__init__(self)                            # update with arguments

        self.update(*args,**kwargs)                      # update object attributes

        self.features += ['molecular_weight','mass','moles','concentration','molarity']  # add printed attributes

    # ---------- #

    @property
    def mass(self):
        """ Mass Property """
        return self._mass

    @mass.setter
    def mass(self,value):
        """ Mass Setter Property """
        # set mass of object 
        self._mass = value 
        # implicitly set molarity, if possible
        if self.molecular_weight:
            self._moles = mass2mol(self._mass,self.molecular_weight)

    # ---------- #

    @property
    def moles(self):
        """ Number of Moles Property """
        return self._moles

    @moles.setter
    def moles(self,value):
        """ Mass Setter Property """
        # set moles of object 
        self._moles = value 
        # implicitly set molarity, if possible
        if self.molecular_weight:
            self._mass = mol2mass(self._moles,self.molecular_weight)

    # ---------- #

    @property
    def concentration(self):
        """ Number of Moles Property """
        return self._concentration

    # ---------- #

    @property
    def molarity(self):
        """ Number of Moles Property """
        return self._molarity

    # ---------- #

    @property
    def molecular_weight(self):
        """ Number of Moles Property """
        return self._molecular_weight

    @molecular_weight.setter
    def molecular_weight(self,value):
        """ Mass Setter Property """
        self._molecular_weight = value

    # ---------- #


""" Unit tests """

if __name__ == "__main__":

    settings = {
            'name':'sample001',
            'molecular_weight':'12 g/mol'
            }

    sample = Solute(settings)





