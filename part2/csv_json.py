# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:12:27 2019

@author: GuoOu
"""

import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleFile.close()

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()