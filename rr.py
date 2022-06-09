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
# References:
# I have used https://www.geeksforgeeks.org/program-round-robin-scheduling-set-1/ webpage to understand
# and find a suitable solution to the Round-robin algorithm, some aspects of original algorithm have been modified to imporove code readability and functionality
#########################################################

def rr_algo(list):
    tq = 10 # Set time quantum

    temp_list = [0] * len(list) # Creating a copy of original processes information, so I can modify the new list
    tat = [0] * len(list) # Turn around time for each process, this is calculated by adding total wait time of a process to its burst time
    wait_time = [0] * len(list) # Wait time for each process

    # temp_list will hold the different processes burst time as a list
    for i in range(len(list)):
        temp_list[i] = list[i][2] # Copying burst time

    t = 0 # Varaible to have a set time

    while (True): # Loop until all process have completed
        finished = True # Variable set to know when processes have all been completed

        for i in range(len(list)): # Loop through the list

            if (temp_list[i] > 0): # If There is still time left for the process to complete
                finished = False # Change variable to "not finished"

                if (temp_list[i] > tq): # If the time left for the process is greater than time quantum then, this process is not finished
                    t += tq # Continue keeping track of total time

                    temp_list[i] -= tq # Change value of remaining process time of temp_list

                else: # If tq is greater then the process will finish
                    t += temp_list[i] # Continue keeping track of total time

                    wait_time[i] = t - list[i][2] # This is total wait time for the finished process, will be used to calculate turn around time

                    temp_list[i] = 0 # Process has finished so we burst time will be 0

        if (finished == True): # Once all process have finished
            for i in range(len(list)): # Set the turn-around time for each process in the tat list
                tat[i] = list[i][2] + wait_time[i] # Formula to find turn-around time, burst time + total wait time of the process

            average_wt = sum(wait_time) / len(wait_time) # Average wait-time of algorithm
            average_tat = sum(tat) / len(tat) # Average turn-around time of algorithm
            break # Exit infinite while loop

    # Print all results
    print(f'The final results using RR algorithm with time quantum of {tq}:')

    for i in range(len(list)): # Looping through the processes and their results
        print(f'process {list[i][0]} arrived at time (0) with priority of {list[i][1]} and ran for {list[i][2]} MS. It had a turn-around time of {tat[i]} MS.')

    print(f'Average turn-around time was: {average_tat} MS\nAverage wait time was: {average_wt} MS.')

