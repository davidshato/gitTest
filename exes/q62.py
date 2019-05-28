#!/usr/bin/python3


import sys
import os
import json

usage = "USAGE: "+ os.path.basename(sys.argv[0])+" [STRING]"

if len(sys.argv) != 2:
    print(usage)
    sys.exit(1)

if sys.argv[1] == "":
    print(usage)
    sys.exit(1)


print(sys.argv)

string = str(sys.argv[1])
answer = {}

for char in string:
    if char in answer:
        answer[char] = answer[char] + 1
    else:
        answer[char] = 1
        
print(answer)

jsonfile = open("dictToJason.json","w")

jsonfile.write(json.dumps(answer, ensure_ascii=False))

jsonfile.close()


