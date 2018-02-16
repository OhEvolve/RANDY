
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

# UNITS
#from units import sum_units


def main():

    '''#
    sequence = Sequence(name='Plasmid1',sequence="ATCTAG")
    cell     = Cell(name='DH5a',species="E.Coli")
    solute   = Solute(name='Tris',weight=(100,'g'))
    solution = Solution(name='dH2O',volume=(10,"mL"))
    
    buff     = Buffer(
                    name='Buffer EB',
                    volume=(10,"mL"),
                    contents=[solute,solution]
                    )

    sample  = Sample(container='10mL tube')

    sample += sequence
    sample += cell 
    sample += solute 
    sample += solution 

    print 'Cell:\n',cell
    print 'Sequence:\n',sequence
    print 'Cell+sequence:\n',cell+sequence
    print 'Buffer:\n',buff
    #'''#
    
    #'''#
    db = Database()
    db.sync_local(overwrite=True)

    solution = db.load('dH2O',volume = (50,'uL'))
    solute   = db.load('Tris-Cl')
    cells    = db.load('DH5a')

    buff  = db.load('Buffer EB')

    #'''#


    return 




""" Unit tests """

if __name__ == "__main__":

    main()

