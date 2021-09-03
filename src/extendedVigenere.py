import string
import re

def textCleaning(text):
    text = text.upper()
    text = re.sub(r'\s*\d+\s*', '',text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace(' ', '')
    return text

def postProcess(text):
    text = [text[i:i+5] for i in range(0, len(text), 5)]
    text = ' '.join(text)

    return text

def encrypt(text, key):
    key = textCleaning(key)
    # text = textCleaning(text)
    cipher = ''

    i = 0
    for chr in text:
        cipher += (ord(chr)+ ord(key[i])) % 256
        i = (i+1) % len(key)

    cipher = bytes(cipher)
    cipher = postProcess(cipher)

    return cipher

def decrypt(cipher, key):
    key = textCleaning(key)
    # cipher = textCleaning(cipher)
    plainText = ''

    i = 0
    for chr in cipher:
        plainText += (ord(chr) - ord(key[i]) + 256) % 256
        i = (i+1) % len(key)

    plainText = bytes(plainText)
    plainText = postProcess(plainText)

    return plainText

def main():
    
    return 0