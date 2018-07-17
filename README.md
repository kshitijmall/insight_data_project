# Pharmacy Data Engineering Project

The objective of this project is to use the raw input data and generate a useful output from it. The output includes total drug cost and the total number of unique prescribers for a particular drug.

## Approach

Using the standard libraries of Python, the given input csv data was read from a give input directory. A nested dictionary and a set were created to identify unique drugs and their prescribers, respectively. The number of prescribers were incremented upon finding duplicate records for them. The total cost of the drug was also evaluated.

Once the nested dictionary was created, sorting was performed by performing a comparison between the total cost for each drug. If the total cost was found same, the comparison was made between the names of the drugs. A sorted list was then generated out of the nested dictionary input. The elements of this list were then written to an output file in an output folder.

Certain errors were raised if the data was found to be corrupt or missing. Input-output errors were also raised. The sorting for this project required nested dictionaries and functools were used.

## Running the code

The main python file is named as pharmacy_main, which resides in the src folder. This main file includes all the necessary code required for this project.

## Running the tests

There is only one unit test that I was able to complete in the end. There should be more unit tests written to make this project better. Some of the functions in the mainfile have not been tested as a result. The unit test file needs to be run from the command line.

## Built With

* [Atom](https://atom.io/) - Text and source code editor
* [Python](https://www.python.org/) Programming tool

## Authors

* **Kshitij Mall**

## Acknowledgments

* Purdue Air Link
