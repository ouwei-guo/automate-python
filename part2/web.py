# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:46:59 2019

@author: GuoOu
Usage:
    python web.py [address]
"""

import webbrowser, sys, pyperclip, requests

address = ''

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#print(res.status_code == requests.codes.ok)
#print(res.text[:250])