#!/usr/bin/env python3

#########################################################
# Name: Thomas Hazekamp
# Student ID: 20423602
# Module: CA216 - Operating Systems
# University: Dublin City University
#########################################################
# I have read and understood DCU's Academic Integrity Policy,
# I have given detailed references to the authors of any material used to help me with this project.
#########################################################

# Check if priority number is not between 1 and 10 inclusive, check if CPU burst time is less than or equal to 0.
def nums_check(list):
    for item in list: # Going through the processes in the list
        priority = item[1]
        burst = item[2]
        if (priority < 1 or priority > 10) or (burst <= 0): # If error is found print a statement
            print("The priority or CPU burst time information in the given file is not valid.")
            quit() # Stop the program if the error is found

# Check if the process has more than 3 attributes
def items_check(list):
    for item in list: # Going through the processes in the list
        if len(item) > 3: # If error is found print a statement
            print("There are too many attributes for one or more processes in the given file.")
            quit() # Stop the program if the error is found