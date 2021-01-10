import random
from . wordlist import wordlist

def get_word():
    rolls = 0
    for i in range(5):
        rolls += random.randint(1,6)*(10**i)
    return wordlist[rolls]

def generate(words=6, sep='-'):
    passphrase = []
    for i in range(words):
        passphrase.append(get_word())
    return sep.join(passphrase)
