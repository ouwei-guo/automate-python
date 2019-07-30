#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:07:22 2019

@author: M

Usage: python regexSearch.py [path] [regex]
"""

import re, sys, os

regex = None

def searchInFile(fileName):
    file = open(fileName, 'r', encoding="ISO-8859-1")
    fileContent = file.read()
    match = regex.search(fileContent)
    if match:
        print(fileName)
    file.close()

def searchInPath(path):
    for fileName in os.listdir(path):
        file = path + os.path.sep + fileName
        if os.path.isdir(file):
            searchInPath(file)
        else:
            searchInFile(file)

if len(sys.argv) == 3 and os.path.isdir(sys.argv[1]):
    regex = re.compile(sys.argv[2])
    searchInPath(sys.argv[1])