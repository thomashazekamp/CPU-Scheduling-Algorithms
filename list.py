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

def make_list(file):
    # A standard list would consist of [task name, priority, CPU burst in milliseconds]
    l = []
    for line in file:
        temp_list = line.strip().split(",")
        temp_list[1], temp_list[2] = int(temp_list[1]), int(temp_list[2])

        l.append(temp_list)
    return l