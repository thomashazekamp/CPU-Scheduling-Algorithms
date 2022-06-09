# CA216 CPU Scheduling

## Introduction
This repository contains programs that show CPU Scheduling. 


## How to test the different algorithms
On the command line, you will need to run the driver.py file, followed by the file with all the processes and then followed by the algorithms acronym/abbreviation.

The possible algorithm acronyms/abbreviations are: FCFS (First-come-first-served), SJF (Shortest-job-first), Prio (Priority Scheduling), RR (Round-robin).

Example:
```
        Main prog   Processes  Algorithm 
           |          file        |
           |            |         |
python3 driver.py processes.txt FCFS
```
This command will use the First-come-first-served algorithm on the processes in the processes.txt file


## How do the files link/work together

The driver.py file read the file with the processes information.

The list.py file is called inside the driver.py file and creates a list of lists to be used in the other algorithm files & functions.

The standard_algo.py file is used to print the output of the fcfs.py, sjf.py, prio.py algorithms after they have ran.

The output for standard_algo.py has the following format: 

"Process [process name] arrived at time (0) with a priority of [process priority] and ran for [process bust time] MS. It had a turn-around time of [process turn-around time] MS. Had priority of [process priority].

"Average turn-around time was: [average turn-around time of algorithm] MS."

"Average wait time was: [average wait time of algorithm] MS.

###### First-come-first-served scheduling
This algorithm is found in the fcfs.py file. This file returns the unchanged list, then the algo_print function in non_pre_algo.py program will print to screen the results of the algorithm. Note: this fcfs.py file has been created to keep the similar structure of other algorithms.

###### Shortest-job-first scheduling
This algorithm is found in the sjf.py file. This file returns a list sorted by the lowest process burst time, then the function algo_print in non_pre_algo.py program uses that list to print to screen the results.

###### Priority scheduling
This algorithm is found in the prio.py file. This file returns a list sorted by the highest priority, then the function algo_print in standard_algo.py program uses that list to print to the screen the results.

###### Round-robin scheduling
This algorithm is found in the rr.py file. This algorithm will print the turn-around time for each process, the average wait-time for the algorithm and the average turn-around time for the algorithm

## Misc
Name: Thomas Hazekamp

Student ID: 20423602

Module: CA216 - Operating Systems

University: Dublin City University

I have read and understood DCU's Academic Integrity Policy,
I have given detailed references to the authors of any material used to help me with this project.