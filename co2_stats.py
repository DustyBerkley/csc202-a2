import csv
from typing import * # type: ignore
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

eh_co2_emissions : TypeAlias = Union[float, None]
eh_co2_emisssions_per_capita : TypeAlias = Union[float, None]

energy_co2_emissions: TypeAlias = Union[float, None]
energy_co2_emissions_per_capita: TypeAlias = Union[float, None]


@dataclass(frozen=True)
class Row:
    country: str
    year: int
    

@dataclass(frozen=True)
class RLNode:
    first : Row
    rest : LinkedList

def read_csv_files(filename: str) -> LinkedList:
    
class Tests(unittest.TestCase):
    pass

if (__name__ == '__main__'):
    unittest.main()
