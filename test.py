import string
from typing import Iterable

alphabet = list(string.ascii_uppercase)

print(alphabet)

text = 'ABCDEF'
test = [ord(chr) for chr in text]

print(test)