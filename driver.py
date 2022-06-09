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

import sys
from list import make_list
from fcfs import fcfs_algo
from non_pre_algo import algo_print
from sjf import sjf_algo
from prio import prio_algo
from rr import rr_algo
from err_handling import nums_check, items_check

def main():
    try:
        given_file = sys.argv[1] # File name from argument line
        algo_type = sys.argv[2] # Algorithm to use from argument line

        file = open(given_file, "r") # Opening file
        l_of_l = make_list(file) # Calling function to format the processes taken from the file
        file.close() # Closing file

        nums_check(l_of_l) # Error control to check if process information is not valid
        items_check(l_of_l) # Error control to check if there are over 3 attributes for each process

        # If Fist-come-fist-served algorithm is called
        if algo_type == "FCFS":
            new = fcfs_algo(l_of_l) # Gets any changes necessary to the list of specific algorithm
            algo_print(new, algo_type) # Printing the results of algorithm

        # If Shortest-job-first algorithm is called
        elif (algo_type == "SJF"):
            new = sjf_algo(l_of_l) # Gets any changes necessary to the list of specific algorithm
            algo_print(new, algo_type) # Printing the results of algorithm
        
        # If the Priority algorithm is called
        elif (algo_type == "Prio"):
            new = prio_algo(l_of_l) # Gets any changes necessary to the list of specific algorithm
            algo_print(new, algo_type) # Printing the results of algorithm
        
        # If the Round-robin algorithm is called
        elif (algo_type == "RR"):
            rr_algo(l_of_l) # Goes through the algorithm and prints results
        
        else: # If the algorithm is not found
            print("Algorithm not found! Please use one of the following:\nFCFS (First-come-first-served),\nSJF (Shortest-job-first),\nPrio (Priority),\nRR (Round-robin).")

    except FileNotFoundError: # Error handling if an error occured with a given file
        print("There was a problem with the given file")
    except IndexError: # Error handling if position of file name or algorithm is wrong
        print("There was a problem with the arguments given or the process information from the given file.")
    except (ValueError, TypeError, ZeroDivisionError): # Error handling if the process information is in a wrong format
        print("There was a problem with the given processes information,\nplease check the given file has a format as such: \"P1, 1, 5\",\nthis represents [process name], [priority number - must be between 1 and 10 inc.], [burst time - must be a positive integer].\nNOTE: remember the \",\" after each part.")

if __name__ == '__main__':
    main()
