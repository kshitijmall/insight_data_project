# Import all the relevant and required standard python libraries
import functools
import csv
import sys
import os
from typing import Dict, Tuple, List

# Increase the field size limit for csv to read very large input data files
csv.field_size_limit(sys.maxsize)

# type alias
# Tuple is used here since the input data is immutable
DrugEntry = Tuple[str, Dict[str, int]]


def compare_name(a: str, b: str) -> int:
    """Sort names (string format) in ascending order

    Args:
        a: The first name.
        b: The second name.

    Returns:
        The return value. -1 for swapping order, 1 otherwise.
    """
    if a >= b:
        # if the first name is greater than the second name then swap them
        return -1

    else:
        # retain the existing order
        return 1


def compare(x: DrugEntry, y: DrugEntry) -> int:
    """Sort first by total cost in descending order, and if there is a
        tie, sort by drug name.

    Args:
        x: The first drug tuple entry.
        y: The second drug tuple entry.

    Returns:
        The return value. -1 for swapping order, 1 otherwise.
    """
    # Obtain drug name from first element of each tuple entry
    x_name = x[0]
    y_name = y[0]

    # Obtain cost from dictionary part of each tuple
    x_cost = x[1]['total_cost']
    y_cost = y[1]['total_cost']
    # first sort the drugs by their cost
    if x_cost > y_cost:
        # retain the existing order
        return 1

    elif x_cost == y_cost:
        # if the costs of two drugs are same then
        # sort them by name using compare_name function
        return compare_name(x_name, y_name)

    else:
        # swap them
        return -1


def sorted_drugs(drugs: Dict[str, Dict[str, int]]) -> List[DrugEntry]:
    """Sort first by total cost in descending order, and if there is a
        tie, sort by drug name.

    Args:
        drugs: The first drug tuple entry.

    Returns:
        List of drug entries in a sorted form as specified by the compare function.
    """
    return sorted(
        drugs.items(),
        key=functools.cmp_to_key(compare),
        reverse=True
    )


def pharmacy_main():
    """This is the main module function which performs the following tasks.
    1. It reads the input file from the input folder
    2. It then creates a nested dictionary from the input drug data
    3. It adds the number of prescribers and calculates the total cost for each drug
    4. It then sorts the drug data in descending order of number of total cost. If the
        total cost is the same then it sorts based on ascending order of drug name.
    5. It then writes an output file named top_cost_drug.txt to the output folder.

    Args:
        No input arguments.

    Returns:
        It just creates an output file named top_drug_cost.txt in the output folder.

    Raises:
        IOError when an i/o operation fails for an i/o related reason
        ValueError when the input for cost is not numeric
    """


    # Create an empty dictionary for storing drug info and an empty set for
    # storing unique names of prescribers
try:
    drugdict = {}
    nameset = set()

    # Read the input file
    with open('.\input\itcont.txt', 'r') as drugIpFile:

        # Create a csvreader iterator
        ipdatarow = csv.reader(drugIpFile)

        # Skip the header (first row)
        next(ipdatarow)

        # Process each entry
        for row in ipdatarow:
            # Skip the row with missing data about drug name, cost. It is assumed that the empty
            # data for name of prescriber counts as a new person considering total cost is the priority.
            if (row[3] in (None, "") or row[4] in (None, "")):
                continue  # Continue the code and don't read any data

            last_name = row[1]
            first_name = row[2]
            name = first_name + " " + last_name  # Put a space in between just in case
            drug_name = row[3]
            cost = int(float(row[4]))  # Use float to manage float data

            # print(prescriberdict[drug_name])
            if drug_name in drugdict:
                """Update the existing entry by incrementing unique prescribers and adding cost
                drugdict is a dictionary comprising drug name as key and number of prescribers
                and total drug cost as values.
                """
                if name in nameset:
                    # Check if the name has a duplicate value
                    # If yes, there is no change in the number of new prescribers
                    drugdict[drug_name]['prescribers'] += 0
                else:
                    # Increment the number of unique prescribers for the existing drug
                    drugdict[drug_name]['prescribers'] += 1
                    nameset.add(name)  # Add the name of the new prescriber
                # Increment the cost for the existing drug
                drugdict[drug_name]['total_cost'] += cost
            else:
                # Add a new drug entry for the dictionary, drugdict
                drugdict[drug_name] = {
                    'prescribers': 1,
                    'total_cost': cost
                }
                nameset.add(name)  # Add the unique name for the new drug

# Check if the output folder exists. If not, create a new output folder with name as output.
        newpath = r'output'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    # Write the output file, top_cost_drug.txt to the output folder and
    # include fieldnames exactly as specified in the code challenge
    with open('.\output\\top_cost_drug.txt', 'w') as outfile:
        fieldnames = ['drug_name', 'num_prescriber', 'total_cost']

        # Create a csv.DictWriter iterator
        drugOpFile = csv.DictWriter(outfile, fieldnames=fieldnames)

        # First write the data header to the output file
        drugOpFile.writeheader()

        # Process each entry from the sorted results of the input file
        for opdata in sorted_drugs(drugdict):

            # Write a new row entry to the output file named as top_cost_drug.txt
            drugOpFile.writerow({
                'drug_name': opdata[0],
                'num_prescriber': opdata[1]['prescribers'],
                'total_cost': opdata[1]['total_cost']
            })
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

"""The following if condition allows this python module to be imported by other modules
without calling pharmacy_main function. If desired, this main function can be called by
the other module that imports this module.
"""
if __name__ == "__main__":
    pharmacy_main()
