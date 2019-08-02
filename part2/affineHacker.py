# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:59:24 2019

@author: GuoOu
"""

import affinecypher, detectEnglish, cryptomath

SILENT_MODE = False

def hackAffine(message):
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    
    for key in range(len(affinecypher.SYMBOLS) ** 2):
        keyA = affinecypher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affinecypher.SYMBOLS)) != 1:
            continue
        decryptedText = affinecypher.decryptMessage(key, message)
        
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
        
        if detectEnglish.isEnglish(decryptedText):
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print('Enter D for done, or just press Enter to continue hacking:')
            
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    message = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
    hackedMessage = hackAffine(message)
    print(hackedMessage)