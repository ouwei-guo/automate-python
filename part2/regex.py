#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:37:47 2019

@author: M
"""

import re

#basic
regex = re.compile(r'\d{3}-\d{3}-\d{4}')

match = regex.search('My number is 415-555-4242.')

print(match.group())

#subdivide in groups
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
#to match parenthesis add escape character \( \)
match = regex.search('My number is 415-555-4242.')

print(match.group(1))
print(match.group(2))
print(match.group(0))
print(match.groups())

match_list = regex.findall('My number is 415-555-4242. His number is 415-444-4242.')
print(match_list)

#find multiple instances
regex = re.compile(r'\d{3}-\d{3}-\d{4}')

match_list = regex.findall('My number is 415-555-4242. His number is 415-444-4242.')

print(match_list)

#match multiple groups with pipe |
regex = re.compile(r'Bat(man|mobile|copter|bat)')
match = regex.search('Batmobile lost a wheel')
print(match.group(0))
print(match.group(1))

#optional matching with question mark
regex = re.compile(r'Bat(wo)?man')
match = regex.search('The Adventures of Batwoman')
print(match.group())

#match zero or more with *, one or more with +
regex = re.compile(r'Bat(wo)*man')
match = regex.search('The Adventures of Batwowoman')
print(match.group())

regex = re.compile(r'Bat(wo)+man')
match = regex.search('The Adventures of Batman')
print(match)

#greedy search
regex = re.compile(r'(Ha){3,5}')
match = regex.search('HaHaHaHaHaHa')
print(match.group())

#non-greedy search
regex = re.compile(r'(Ha){3,5}?')
match = regex.search('HaHaHaHaHaHa')
print(match.group())

#beginning of a text ^ end $
regex = re.compile(r'^\d+$')
match = regex.search('1234567890')
print(match.group())

#any character .
regex = re.compile(r'.at')
match_list = regex.findall('The cat in the hat sat on the flat mat.')
print(match_list)

#match everything .*
regex = re.compile(r'First Name: (.*) Last Name: (.*)')
match = regex.search('First Name: Al Last Name: Sweigart')
print('First name: ' + match.group(1))
print('Last name: ' + match.group(2))

#substitute string
regex = re.compile(r'Agent (\w)\w+(\w)')
new_text = regex.sub(r'\1***\2', 'Agent Alice gave the secret documents to Agent Bob.')
print(new_text)

#verbose mode
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))? # area code
        (\s|-|\.)? # separator
        \d{3} # first 3 digits
        (\s|-|\.) # separator
        \d{4} # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
        )''', re.VERBOSE)











    