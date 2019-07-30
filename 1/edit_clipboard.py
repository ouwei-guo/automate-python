#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:12:23 2019

@author: M
"""

import pyperclip

text = pyperclip.paste()

print(text)
#edit text here
edited_text = text + ' Hello'
print(edited_text)

pyperclip.copy(edited_text)