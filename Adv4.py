from Crypto.Cipher import AES
from Crypto import Random


def unpad( text, l):
    val = l - len(text)
    text = text[:val]

    return text


def pad(text,k=16):

    length = len(text)
    val = k - (length % k)
    padChar = b'\x00'

    n = val - 2

    return (text + str(padChar * n) + str(val))

key = '1234567812345678'
aes_encrypt = AES.new(key, AES.MODE_ECB)
aes_decrypt = AES.new(key, AES.MODE_ECB)
p = "AAAABBBBCCCCDDDDAA"


padded = pad(p)

print ('plaintext {0}- '.format(p))
print ('padded {0}- '.format( padded))

c = aes_encrypt.encrypt(padded)

print (c)
# encode encrypted text with hex to make
# it human readable
cipher = c.encode('hex')
print ('ciphertext\t- ', cipher)



# decrypt the ciphertext back into plaintext
decrypted = aes_decrypt.decrypt(c)

print ('decrypted{0}- '.format( decrypted))

if decrypted == padded:
    print ('matched')

plen = len(p)
unpad = unpad(decrypted, plen)

print ('unpadded {0}-'.format(unpad))

