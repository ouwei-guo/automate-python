# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:57:39 2019

@author: GuoOu
"""

import requests, sys, webbrowser, bs4

address = 'https://www.google.com/search?q='
print('Googling...') # display text while downloading the Google page
res = requests.get(address + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))