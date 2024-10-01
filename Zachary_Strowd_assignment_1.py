#!/usr/bin/env python3
"""
=============================================================================
Title : Zachary_Strowd_assigment_1.py
Description : This script gets FNA data from a file and sorts the sequences from Largest to Smallest. Ouputs the sorted data into a file.
Author : errees
Date : 09/19/23
Version : 1.0
Usage : python3 Zachary_Strowd_assigment_1.py
Notes : Needs a input file to read sequences.
Python Version: 3.9.12
=============================================================================
"""
import argparse

print("Assigment 1")

#Setting up the Parsing for the input and output files
parser = argparse.ArgumentParser(description='Parser')
parser.add_argument('-i',  type=str,  help='Input file path')
parser.add_argument('-o', type=str, help='Output file path')
args = parser.parse_args()
input_file = args.i
output_file = args.o

def getFNAdata(input_file):
    #Getting the data from the file
    dict = {}
    with open(input_file, 'r') as f:
        for line in f:
            if '>' in line:
               l = line.strip()
               dict[l] = ''
               temp = l
            else:
                
                dict[temp] = dict[temp] + line.strip()
    return dict

def writeToFNA(dict, output_file):
    #Writing to the output file
    count = 0
    with open(output_file, 'w') as f:
        #parsing through the dictionary with the keys and values
        for key, value in dict.items():
            identLine = key + "\n"
            f.write(identLine)
            sequenceLine = value
            #calling split80 to get the 80 character limit
            split80(sequenceLine, f)
    f.close()               

def split80(line, f):
    count = 0
    current = 0
    length = len(line)
    for char in line:
        current += 1
        count += 1
        if count == 80:
            f.write(char)
            f.write("\n")
            count = 0
        elif length == current:
            f.write(char)
            f.write("\n")
        else:
            f.write(char)

#Sorting the data
def sortSequences(data):
    #Using a lamda function. Sorting the sequence by using the len function and reversing it
    d = sorted(data.items(), key=lambda x: len(x[1]), reverse=True)
    d = dict(d)
    return d

sequences = getFNAdata(input_file)
sorted_sequences = sortSequences(sequences)
writeToFNA(sorted_sequences, output_file)
