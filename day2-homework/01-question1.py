#!/usr/bin/env python


# imports the system-specific parameters and functions module.
import sys

# Initiates a for loop that will perform an operation on each of the lines in fly.txt.
for line in sys.stdin:
    # Selects lines containing the necessary data, including a FlyBase ID.
    if "DROME" and "FB" in line:
        # Removes trailing characters from lines and slipts the columns using whitespace as the delimeter.
        fields = line.rstrip("\r\n").split() 
        # Selects the FlyBase and Uniprot IDs and assigns them variable names.
        fb_id = fields[-1] 
        uni_id = fields[-2]  
        # Maps FlyBase IDs to UniProt IDs.
        mapped = fb_id + "\t" + uni_id # Combines associated FlyBase and Uniprot IDs.
        # Prints mapped IDs in two columns.
        print mapped

""""
        
To output mapped IDs in the file, two_col, enter the following code in the command line:
cat fly.txt | ./01-question1.py >> two_col

"""




