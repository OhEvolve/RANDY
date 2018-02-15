
# standard libraries

# nonstandard libraries

# homegrown libraries

# SAMPLE MODULE
from sample.sample import Sample
from sample.matter import Matter
from sample.sequence import Sequence
from sample.cell import Cell
from sample.solute import Solute
from sample.solution import Solution
from sample.buffer import Buffer 

# DATABASE MODULE
from database.database import Database


def main():

    '''
    sequence = Sequence(sequence="ATCTAG")
    cell = Cell(species="E.Coli")
    solute = Solute(weight=(100,'g'))
    solution = Solution(volume=(10,"mL"))
    
    sample = Sample(container='10mL tube')

    sample += sequence
    sample += cell 
    sample += solute 
    sample += solution 

    print sample
    '''

    db = Database()
    db.sync_local()

    solution = db.load('dH2O',volume = (50,'uL'))
    solute   = db.load('Tris-Cl')
    cells    = db.load('DH5a')
    


    return 




""" Unit tests """

if __name__ == "__main__":

    main()

