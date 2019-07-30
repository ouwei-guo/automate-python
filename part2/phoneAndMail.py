#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:52:28 2019

@author: M
"""

import pyperclip, re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))? # area code
        (\s|-|\.)? # separator
        \d{3} # first 3 digits
        (\s|-|\.) # separator
        \d{4} # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
        )''', re.VERBOSE)

mailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+ #username
        @
        [a-zA-Z0-9.-]+ #domain name
        (\.[a-zA-Z]{2,4}) #dot-something
        )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for match in mailRegex.findall(text):
    matches.append(match[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')