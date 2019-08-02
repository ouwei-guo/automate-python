# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:52:28 2019

@author: GuoOu
Unbreakable One-Time Pad Cipher
key criteria
It is exactly as long as the encrypted message.

It is made up of truly random symbols.

It is used only once and never again for any other message.
"""

import secrets

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS.
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # Add if encrypting.
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # Subtract if decrypting
            
            num %= len(LETTERS) # Handle any wraparound.
            
            if symbol.isupper():
                translated.append(LETTERS[num])
            else:
                translated.append(LETTERS[num].lower())
            
            keyIndex += 1 # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    
    return ''.join(translated)

def getKey(message):
    myKey = ''
    for i in range(len(message)):
        myKey += secrets.choice(LETTERS)
    return myKey

if __name__ == '__main__':
    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    
    myKey = getKey(myMessage)
    print(myKey)
    translated = encryptMessage(myKey, myMessage)
    print(translated)
    translated = decryptMessage(myKey, translated)
    print(translated)
    