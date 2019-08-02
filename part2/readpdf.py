# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:21:36 2019

@author: GuoOu
"""

import PyPDF2

filename = 'DICHIARAZIONE SINISTRO.PDF'

pdfFileObj = open(filename, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#pdfReader.isEncrypted
#pdfReader.decrypt(password)

print(pdfReader.numPages)
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())

pdfFileObj.close()

"""
#copy pages from one pdf to another

pdf1File = open(filename, 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)


pdfWriter.encrypt('swordfish')

pdfOutputFile = open('copy.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
"""