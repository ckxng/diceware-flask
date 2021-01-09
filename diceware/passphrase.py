def get_word():
    return 'word'

def generate(words=6):
    passphrase = []
    for i in range(words):
        passphrase.append(get_word())
    return '-'.join(passphrase)
