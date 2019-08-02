#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:07:22 2019

@author: M

Usage:
    python regexSearch.py search [path] [regex] [extention]
    python regexSearch.py replace [filepath] [regex] [new_string]
"""

import re, sys, os

regex = None
extention = ''

def replaceInFile(fileName, new_string):
    file = open(fileName, 'r', encoding="ISO-8859-1")
    fileContent = file.read()
    matches = len(regex.findall(fileContent))
    new_text = regex.sub(new_string, fileContent)
    file.close()
    file = open(fileName, 'w')
    file.write(new_text)
    file.close()
    print('Replaced ' + str(matches) + ' instances')
    
def searchInFile(fileName):
    file = open(fileName, 'r', encoding="ISO-8859-1")
    if regex.search(file.read()):
        print(fileName)
    file.close()

def searchInPath(path):
    for fileName in os.listdir(path):
        file = path + os.path.sep + fileName
        if os.path.isdir(file):
            searchInPath(file)
        elif fileName.find(extention) != -1:
            searchInFile(file)

if len(sys.argv) == 5:
    regex = re.compile(r''+str(sys.argv[3]), re.IGNORECASE)
    if sys.argv[1] == 'search' and os.path.isdir(sys.argv[2]):
        if sys.argv[4] != '.':
            extention = sys.argv[4]
        searchInPath(sys.argv[2])
    elif sys.argv[1] == 'replace' and os.path.isfile(sys.argv[2]):
        replaceInFile(sys.argv[2], sys.argv[4])
    else:
        print('''Usage:
    python regexSearch.py search [path] [regex] [extention]
    python regexSearch.py replace [filepath] [regex] [new_string]''')
else:
    print('''Usage:
    python regexSearch.py search [path] [regex] [extention]
    python regexSearch.py replace [filepath] [regex] [new_string]''')
