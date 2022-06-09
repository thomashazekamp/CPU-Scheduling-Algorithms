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

from operator import itemgetter

def sjf_algo(list): # This function will return a sorted list based on CPU burst time (in ascending order)
    sjf_sorted_list = sorted(list, key=itemgetter(2))
    return sjf_sorted_list