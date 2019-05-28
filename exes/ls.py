#!/usr/bin/python3

import os
import sys
import hashlib
from multiprocessing import Pool


def md5creator(arr):
    num = arr[0]
    fullpath = arr[1]
    print(str(num)+","+fullpath+","+hashlib.md5(fullpath.encode('utf-8')).hexdigest())


def createlist(path):
    listf  = []
    listd = []
    i = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            i+=1
            fullpath = os.path.join(root,name)
            listf.append([i,fullpath])
        
        for name in dirs:
            i+=1
            fullpath = os.path.join(root,name)
            listd.append([i,fullpath])

    return listf,listd



if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("USAGE: <DIR>")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.isdir(path):
        print("USAGE <DIR>")
    
    filesList,dirList = createlist(path)
    p = Pool(5)
    p.map(md5creator,filesList)
    p.map(md5creator,dirList)

