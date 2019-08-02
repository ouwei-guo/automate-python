# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:38:26 2019

@author: GuoOu
"""

import requests, bs4

website = 'https://nostarch.com/'
res = requests.get(website)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")
#or from file
#exampleFile = open('example.html')
#exampleSoup = bs4.BeautifulSoup(exampleFile)

#elems = soup.select('div .views-field')
elems = soup.select('script')
for elem in elems:
#    print(elem.getText())
    for key in elem.attrs:
        print('key: ' + key + ', value: ' + elem.get(key))