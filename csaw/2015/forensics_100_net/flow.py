#!/usr/bin/env python
import random
import string
import sys
from base64 import b64encode, b64decode

FLAG = 'flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'

enc_ciphers = ['rot13', 'b64e', 'caesar']
dec_ciphers = ['rot13', 'b64d', 'caesard']

def rot13(s):
	_rot13 = string.maketrans(
    	"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	return string.translate(s, _rot13)

def b64e(s):
	return b64encode(s)

def b64d(s):
    return b64decode(s)

def caesar(plaintext, shift=3):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def caesard(ciphertext, shift=3):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(shifted_alphabet, alphabet)
    return ciphertext.translate(table)

def encode(pt, cnt=50):
	tmp = '2{}'.format(b64encode(pt))
	for cnt in xrange(cnt):
		c = random.choice(enc_ciphers)
		i = enc_ciphers.index(c) + 1
		_tmp = globals()[c](tmp)
		tmp = '{}{}'.format(i, _tmp)

	return tmp

def decode(data):
    # digit describes encoding
    # remainder is 'ciphertext'
    while not data.startswith('flag{'):
        encoding, content = data[0], data[1:]
        # encoding is a digit in the enc/dec array
        data = globals()[dec_ciphers[int(encoding) - 1]](content)
    print data

if __name__ == '__main__':
	# print encode(FLAG, cnt=?)
    with open(sys.argv[1], 'r') as dumpfile:
        decode(dumpfile.read())
