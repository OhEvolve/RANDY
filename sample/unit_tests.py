
# standard libraries

# nonstandard libraries

# homegrown libraries
from sample import Sample

from matter import Matter

from sequence import Sequence
from cell import Cell
from solute import Solute
from solution import Solution


def main():

     
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



""" Unit tests """

if __name__ == "__main__":

    main()

