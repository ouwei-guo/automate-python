# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:46:37 2019

@author: GuoOu
"""

import sys, cryptomath, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def process(key, mode, text):

    if mode == 'encrypt':
        translated = encryptMessage(key, text)
    elif mode == 'decrypt':
        translated = decryptMessage(key, text)
    else:
        sys.exit("Invalid mode")
    
    return translated

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1. Choose a different key.')
    
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key B is 0. Choose a different key.')
    
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
        
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol # Append the symbol without encrypting.
    
    return ciphertext

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # Append the symbol without decrypting.
    
    return plaintext

def getRandomKey():
    keyA = random.randint(2, len(SYMBOLS))
    keyB = random.randint(2, len(SYMBOLS))
    if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
        return keyA * len(SYMBOLS) + keyB
    
    return getRandomKey()

if __name__ == '__main__':
    text = "'A computer would deserve to be called intelligent if it could deceive a human into believing that it was human.' -Alan Turing"
    key = getRandomKey()
    
    text = process(key, 'encrypt', text)
    print(text)

    text = process(key, 'decrypt', text)
    print(text)







