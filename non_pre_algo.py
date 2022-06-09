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

# This function is used for fcfs, sjf and prio algorithms
# fcfs directly uses this function, meanwhile sjf and prio algorithms send a re-ordered list to this function
def algo_print(list, algo_name):
    tat = 0 # Turn around time for individual
    tot_tat = 0 # Turn around time for the whole CPU usage
    num_processes = 0 # Number of processes
    tot_wt = 0 # Wait time for all processes

    print(f'The final results using {algo_name} algorithm:') # Printing header/title

    # Looping through each process
    for process in list:
        tat += process[2] # Adding process burst time
        tot_tat += tat # Adding turn-around time so far
        num_processes += 1 # Incrementing number of processes
        tot_wt += (tat - process[2]) # Wait time is turn-around time - burst time

        print(f'Process {process[0]} arrived at time (0) with a priority of {process[1]} and ran for {process[2]} MS. It had a turn-around time of {tat} MS.')

    print(f'Average turn-around time was: {tot_tat / num_processes} MS\nAverage wait time was: {tot_wt / num_processes} MS.')
