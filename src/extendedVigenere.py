import string
import re

def textCleaning(text):
    text = text.upper()
    text = re.sub(r'\s*\d+\s*', '',text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace(' ', '')
    return text

def encrypt(text, key):
    key = textCleaning(key)
    cipher = ''

    i = 0
    for chr in text:
        cipher += ord(chr)+ ord(key[i]) % 256
        i = (i+1) % len(key)

    return cipher