#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 15:13:44 2019

@author: M
"""

import os, shelve

cwd = os.getcwd()

def test():
    #os.chdir('/Users/M/Doc/automate-python/part2')
    print(os.path.basename(cwd))
    print(os.path.dirname(cwd))
    print(os.path.split(cwd))
    print(cwd.split(os.path.sep))
    print(os.path.getsize(cwd))
    print(os.listdir(cwd))
    print(os.path.exists(cwd))
    print(os.path.isfile(cwd))
    print(os.path.isdir(cwd))

test()
def readFile(fileName):
    helloFile = open(cwd + '/' + fileName)
    helloContent = helloFile.read()
    #helloContent = helloFile.readlines()
    print(helloContent)

def writeFile():
    fileName = 'bacon.txt'
    baconFile = open(fileName, 'w')
    baconFile.write('Hello world\n')
    baconFile.close()
    baconFile = open(fileName, 'a')
    baconFile.write('Bacon is not a vegetable.')
    baconFile.close()
    readFile(fileName)
    
#writeFile()

def shelveFile():
    shelfFile = shelve.open('mydata')
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
    shelfFile.close()
    
    shelfFile = shelve.open('mydata')
    print(type(shelfFile))
    for key in list(shelfFile.keys()):
        print(key)
        print(type(shelfFile[key]))
        print(shelfFile[key])
    shelfFile.close()
    
#shelveFile()






















