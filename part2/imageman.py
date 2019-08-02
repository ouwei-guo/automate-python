# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:56:03 2019

@author: GuoOu
"""

import pyautogui

pyautogui.PAUSE = 2

pyautogui.FAILSAFE = True

for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
