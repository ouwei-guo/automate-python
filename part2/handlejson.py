# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:17:45 2019

@author: GuoOu
"""

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
stringOfJsonData = json.dumps(jsonDataAsPythonValue)
print(stringOfJsonData)