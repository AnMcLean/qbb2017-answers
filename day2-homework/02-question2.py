#!/usr/bin/env python

import sys 

ids = open(sys.argv[1])
tab = open(sys.argv[2])
choice = int(sys.argv[3])

ids_dictionary = {}


for line in ids:
    fields = line.rstrip("\r\n").split("\t")
    fb_id = fields[0]
    uni_id = fields[1]
    ids_dictionary[fb_id] = uni_id

count = 0

while count < 100:
    for line2 in tab:
        fields2 = line2.rstrip("\r\n").split()
        x = fields2[8]
        if x in ids_dictionary:
            print ids_dictionary[x] + "\t" + line2
            count += 1   
        elif choice == 2:
            print "*" + "\t" + line2
            count += 1  
        elif choice == 1:
            count += 1  
            continue
    
"""  
To run, enter the following in the command line:

./02-question2.py two_col t_data.ctab ?  

Replace the ? in the above command with 1 to print nothing when the gene name cannot 
be mapped to the FlyBase ID in the c_tab file. To print * instead, replace the ? in 
the above command with a 2.
      
"""        

         