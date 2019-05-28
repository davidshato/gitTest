#!/usr/bin/python3

import sys
import os

def USAGE():
    print(os.path.basename(sys.argv[0])+" USAGE: <WORD> <PATH>");
    sys.exit(1)

if(len(sys.argv) != 3):
    USAGE()

if(not os.path.isfile(sys.argv[2])):
    USAGE()

fileName = open(sys.argv[2],"r")
searchWord = sys.argv[1]
found = False

linesList = fileName.readlines()

for line in linesList:
    if(searchWord in line):
        found = True
        print(line[:-1])

if(not found):
    print(searchWord+" is not found in "+sys.argv[2])
    sys.exit(1)



