import csv
from typing import * # type: ignore
from dataclasses import dataclass
import unittest
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


# Purpose: return the number of items in a given linked list
def listlen(ll: LinkedList) -> int:
    match ll:
        case None:
            return 0
        case RLNode(first, rest):
            return 1 + listlen(rest)

# Purpose: add a row object to the front of a given linked list
def add_to_list(list: LinkedList, row: Row) -> LinkedList:
    return RLNode(row, list)

# Purpose: return the value given a row and field name
def get_item_in_row(row: Row, field_name: str) -> Any:
    if(field_name == "country"):
        return row.country
    if(field_name == "year"):
        return row.year
    if(field_name == "electricity_and_heat_co2_emissions"):
        return row.electricity_and_heat_co2_emissions
    if(field_name == "electricity_and_heat_co2_emissions_per_capita"):
        return row.electricity_and_heat_co2_emissions_per_capita
    if(field_name == "energy_co2_emissions"):
        return row.energy_co2_emissions
    if(field_name == "energy_co2_emissions_per_capita"):
        return row.energy_co2_emissions_per_capita
    if(field_name == "total_co2_emissions_excluding_lucf"):
        return row.total_co2_emissions_excluding_lucf
    if(field_name == "total_co2_emissions_excluding_lucf_per_capita"):
        return row.total_co2_emissions_excluding_lucf_per_capita
    return None

# Purpose: given a csv file name, read the file and format it into a linked list of Row objects
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
        
        data_list : LinkedList = None
        for line in iter:
            this_row : Row = string_to_row(line)
            data_list = add_to_list(data_list, this_row)

        return data_list
    
# Purpose: return a row object when given a list of strings representing that row's properties
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
    
# Purpose: compare two values with a given comparison type
def compare_values(value1: Any, value2: Any, comparison_type: Literal["equal", "less_than", "greater_than"]) -> bool:
    if(comparison_type == "equal"):
        return value1 == value2
    if(comparison_type == "less_than"):
        return value1 < value2
    if(comparison_type == "greater_than"):
        return value1 > value2

# Purpose: given a linked list, return a new linked list only containing values that pass the given criteria
# when using filter with a field_name of "country" the only valid comparison type is "equal"
# when using filter with co2 emissions, the only valid comparison types are "less_than" or "greater_than"
def filter(list: LinkedList, field_name: str, comparison_type: Literal["equal", "less_than", "greater_than"], comparison_value: Any) -> LinkedList:
    passing_list : LinkedList = None
    current_node : LinkedList = list

    while current_node != None:
        this_field = get_item_in_row(current_node.first, field_name)

        if(this_field != None):
            passes_filter : bool = compare_values(this_field, comparison_value, comparison_type)

            if(passes_filter):
                passing_list = add_to_list(passing_list, current_node.first)

        current_node = current_node.rest
        
    return passing_list

# Purpose: return the number of countries in a given dataset
def answer_1(rows : LinkedList):
    filtered : LinkedList = filter(rows, "year", "equal", 2020)
    return listlen(filtered)

# Purpose: return all the rows associated with mexico
def answer_2(rows : LinkedList):
    filtered : LinkedList = filter(rows, "country", "equal", "Mexico")
    return filtered

# Purpose: return a row for every country that had a higher total_co2_emissions_excluding_lucf_per_capita than the US in 1990
def answer_3(rows : LinkedList):
    all_1990 : LinkedList = filter(rows, "year", "equal", 1990)
    US_1990 = filter(all_1990, "country", "equal", "United States")

    if US_1990 == None:
        raise LookupError("could not find data for the US in 1990")

    US_1990_excluding_lucf_per_capita = get_item_in_row(US_1990.first, "total_co2_emissions_excluding_lucf_per_capita")
    filtered : LinkedList = filter(all_1990, "total_co2_emissions_excluding_lucf_per_capita", "greater_than", US_1990_excluding_lucf_per_capita)
    return filtered

# Purpose: return a row for every country that had a higher total_co2_emissions_excluding_lucf_per_capita than the US in 2020
def answer_4(rows : LinkedList):
    all_2020 : LinkedList = filter(rows, "year", "equal", 2020)
    US_2020 = filter(all_2020, "country", "equal", "United States")

    if US_2020 == None:
        raise LookupError("could not find data for the US in 2020")
    
    US_1990_excluding_lucf_per_capita = get_item_in_row(US_2020.first, "total_co2_emissions_excluding_lucf_per_capita")
    filtered : LinkedList = filter(all_2020, "total_co2_emissions_excluding_lucf_per_capita", "greater_than", US_1990_excluding_lucf_per_capita)
    return filtered

# Purpose: return the approximate population of Luxembourg in 2014
def answer_5(rows : LinkedList):
    all_2014 : LinkedList = filter(rows, "year", "equal", 2014)
    Lux_2014 = filter(all_2014, "country", "equal", "Luxembourg")

    if Lux_2014 == None:
        raise LookupError("could not find data for the Luxembourg in 2014")
    
    Lux_2014_energy_co2_emissions = get_item_in_row(Lux_2014.first, "energy_co2_emissions") * 1000000
    Lux_2014_energy_co2_emissions_per_capita = get_item_in_row(Lux_2014.first, "energy_co2_emissions_per_capita")
    return Lux_2014_energy_co2_emissions / Lux_2014_energy_co2_emissions_per_capita

# Purpose: return the increase in total electricity and heat emissions in china from 1990 to 2020
def answer_6(rows : LinkedList):
    all_1990 : LinkedList = filter(rows, "year", "equal", 1990)
    China_1990 = filter(all_1990, "country", "equal", "China")
    if China_1990 == None:
        raise LookupError("could not find data for the China in 1990")
    
    all_2020 : LinkedList = filter(rows, "year", "equal", 2020)
    China_2020 = filter(all_2020, "country", "equal", "China")
    if China_2020 == None:
        raise LookupError("could not find data for the China in 2020")
    
    China_1990_electricity_and_heat_co2_emissions = get_item_in_row(China_1990.first, "electricity_and_heat_co2_emissions")
    China_2020_electricity_and_heat_co2_emissions = get_item_in_row(China_2020.first, "electricity_and_heat_co2_emissions")
    print(China_1990_electricity_and_heat_co2_emissions, China_2020_electricity_and_heat_co2_emissions)
    return China_2020_electricity_and_heat_co2_emissions / China_1990_electricity_and_heat_co2_emissions

# Purpose: return the estimated electricity and heat co2 emissions for China in 2070
def answer_7(rows : LinkedList):
    all_1990 : LinkedList = filter(rows, "year", "equal", 1990)
    China_1990 = filter(all_1990, "country", "equal", "China")
    if China_1990 == None:
        raise LookupError("could not find data for the China in 1990")
    
    all_2020 : LinkedList = filter(rows, "year", "equal", 2020)
    China_2020 = filter(all_2020, "country", "equal", "China")
    if China_2020 == None:
        raise LookupError("could not find data for the China in 2020")
    
    China_1990_electricity_and_heat_co2_emissions = get_item_in_row(China_1990.first, "electricity_and_heat_co2_emissions")
    China_2020_electricity_and_heat_co2_emissions = get_item_in_row(China_2020.first, "electricity_and_heat_co2_emissions")

    percent_increase_per_year : float = (China_2020_electricity_and_heat_co2_emissions / China_1990_electricity_and_heat_co2_emissions) ** (1/30)

    future_year : int = 2070
    return China_1990_electricity_and_heat_co2_emissions * percent_increase_per_year ** (future_year - 1990)


class Tests(unittest.TestCase):
    test_row : Row = Row("US", 2025, 100., 10., 50., 5., 200., 20.)
    test_row_2 : Row = Row("Canada", 2020, 20., 5., 400., 100., 1000., 250.)
    empty_LL : LinkedList = None
    one_item_LL : LinkedList = RLNode(test_row, None)
    two_item_LL : LinkedList = RLNode(test_row_2, RLNode(test_row, None))

    def test_add_to_list(self):
        self.assertEqual(add_to_list(self.empty_LL, self.test_row), self.one_item_LL)
        self.assertEqual(add_to_list(self.one_item_LL, self.test_row_2), self.two_item_LL)

    def test_string_to_row(self):
        test_row_string : List[str] = ["US", "2025", "100", "10", "50", "5", "200", "20"]
        test_row_2_string : List[str] = ["Canada", "2020", "20", "5", "400", "100", "1000", "250"]
        self.assertEqual(string_to_row(test_row_string), self.test_row)
        self.assertEqual(string_to_row(test_row_2_string), self.test_row_2)

    def test_listlen(self):
        self.assertEqual(listlen(self.empty_LL), 0)
        self.assertEqual(listlen(self.one_item_LL), 1)
        self.assertEqual(listlen(self.two_item_LL), 2)

    def test_get_item_in_row(self):
        self.assertEqual(get_item_in_row(self.test_row, "country"), "US")
        self.assertEqual(get_item_in_row(self.test_row_2, "energy_co2_emissions_per_capita"), 100.)

    def test_compare_values(self):
        self.assertTrue(compare_values("hello", "hello", "equal"))
        self.assertFalse(compare_values(10, 15, "greater_than"))
        self.assertTrue(compare_values(5, 15, "less_than"))

    def test_filter(self):
        self.assertEqual(filter(self.two_item_LL, "country", "equal", "Canada"), RLNode(self.test_row_2, None))
        self.assertEqual(filter(self.two_item_LL, "total_co2_emissions_excluding_lucf", "less_than", 2000.), RLNode(self.test_row, RLNode(self.test_row_2, None)))
        self.assertEqual(filter(self.two_item_LL, "electricity_and_heat_co2_emissions", "greater_than", 50.), self.one_item_LL)

if (__name__ == '__main__'):
    unittest.main()
