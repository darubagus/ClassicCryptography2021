import string
from typing import Iterable
import json

# alphabet = list(string.ascii_uppercase)

# print(alphabet)

# text = 'ABCDEF'
# test = [ord(chr) for chr in text]

# print(test)

key = '17,26'
string = key.split(',')
string = [int(item) for item in string]

print(string)