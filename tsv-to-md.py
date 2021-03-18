#!/bin/env python3

import csv
import sys

def main():

    key = sys.argv[1]
    infile = sys.argv[2]
    outfile = open('README.md', 'w')
    

    outfile.write('Example | Description | Tags | Duples | Triplets | Quintuplets | Pitch Names | Number of Notes | Lowest Note | Highest Note | Rests Used | Ornaments used\n')
    outfile.write(':---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:\n')
    
    inFile = open(infile, 'r')

    for line in inFile:
        line = line.strip().split('\t')

        if line[0] == key:
            print(line)
            string = line[1] + ' | ' + line[2] + ' | ' + line[3] + ' | ' + line[4] + ' | ' + line[5] + ' | ' + line[6] + ' | ' + line[7] + ' | ' + line[8] + ' | ' + line[9] + ' | ' + line[10] + ' | ' + line[11] + ' | ' + line[12] + '\n'
            outfile.write(string)

    inFile.close()
    outfile.close()
    # print(line)

main()