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

def add_to_list(list: LinkedList, row: Row) -> LinkedList:
    return RLNode(row, list)

def read_csv_lines(filename: str) -> LinkedList:
    expected_labels : List[str] = ['country', 
                                    'year', 
                                    'electricity_and_heat_co2_emissions',
                                    'electricity_and_heat_co2_emissions_per_capita',
                                    'energy_co2_emissions', 
                                    'energy_co2_emissions_per_capita', 
                                    'total_co2_emissions_excluding_lucf', 
                                    'total_co2_emissions_excluding_lucf_per_capita']
    
    with open(filename, newline="") as csvfile:
        iter = csv.reader(csvfile)
        topline : List[str] = next(iter)
        if not (topline == expected_labels):
            raise ValueError(f"unexpected first line: got: {topline}")
        
        data_list = None
        for line in iter:

        return item_count

def string_to_row(line: List[str]) -> Row:
    country = line[0]
    year = int(line[1])

    electricity_and_heat_co2_emissions = None
    if(line[2] != ""):
        electricity_and_heat_co2_emissions = float(line[2])

    electricity_and_heat_co2_emissions_per_capita = None
    if(line[3] != ""):
        electricity_and_heat_co2_emissions_per_capita = float(line[3])

    energy_co2_emissions = None    
    if(line[4] != ""):
        energy_co2_emissions = float(line[4])
    
    energy_co2_emissions_per_capita = None
    if(line[5] != ""):
        energy_co2_emissions_per_capita = float(line[5])
    
    total_co2_emissions_excluding_lucf = None
    if(line[6] != ""):
        total_co2_emissions_excluding_lucf = float(line[6])

    total_co2_emissions_excluding_lucf_per_capita = None
    if(line[7] != ""):
        total_co2_emissions_excluding_lucf_per_capita = float(line[7])

        

    return Row(country, year, electricity_and_heat_co2_emissions, electricity_and_heat_co2_emissions_per_capita, energy_co2_emissions, energy_co2_emissions_per_capita, total_co2_emissions_excluding_lucf, total_co2_emissions_excluding_lucf_per_capita)
    
class Tests(unittest.TestCase):
    pass

if (__name__ == '__main__'):
    unittest.main()
