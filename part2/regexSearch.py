#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:07:22 2019

@author: M
Usage: python regexSearch.py [path] [regex] [extention]
"""

import re, sys, os

regex = None
extention = ''

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

if len(sys.argv) == 4 and os.path.isdir(sys.argv[1]):
    regex = re.compile(r''+str(sys.argv[2]), re.IGNORECASE)
    print(regex)
    if sys.argv[3] != '.':
        extention = sys.argv[3]
    searchInPath(sys.argv[1])

