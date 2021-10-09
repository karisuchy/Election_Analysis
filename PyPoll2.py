
# Add our dependencies. 
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = "election_results.csv"

# Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    # read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file (note: the following is a for loop code).
    #for row in file_reader:
        #print(row)

# The next set of instructions is based on 3.4.2; it returns the correct output 
# Assign a variable for the file to load and the path. 
# file_to_load = "election_results.csv"

# Open the election results and read the file:
# election_data = open(file_to_load, "r")

# To do: performan Anaysis
# print(election_data)

# Close the file.
# election_data.close()
