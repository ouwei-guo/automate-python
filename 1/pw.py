#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:12:23 2019

@author: M
"""
PW = {'mail': 'mail pw',
      'git': 'git pw',
      'phone': 'phone pw'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: $python pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]

if account in PW:
    pyperclip.copy(PW[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('No account')