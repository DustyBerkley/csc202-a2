import csv
from typing import * # type: ignore
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

co2_emissions : TypeAlias = Union[float, None]
LinkedList : TypeAlias = Union['RLNode', None]

@dataclass(frozen=True)
class Row:
    country: str
    year: int
    electricity_and_heat_co2_emissions: co2_emissions
    electricity_and_heat_co2_emissions_per_capita: co2_emissions
    energy_co2_emissions: co2_emissions
    energy_co2_emissions_per_capita: co2_emissions
    total_co2_emissions_excluding_lucf: co2_emissions
    total_co2_emissions_excluding_lucf_per_capita: co2_emissions
    

@dataclass(frozen=True)
class RLNode:
    first : Row
    rest : LinkedList

def read_csv_files(filename: str) -> LinkedList:
    pass


class Tests(unittest.TestCase):
    pass

if (__name__ == '__main__'):
    unittest.main()
