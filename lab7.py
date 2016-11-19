import base64
from Crypto.Cipher import DES


def addPadding(data):
    length = 8 - (len(data) % 8)
    data += "\x00" * (length)
    return data


def chunks(longdata, n):
    for i in range(0, len(longdata), n):
        yield longdata[i:i + n]


iv = "00000000"
plainText = 'AAAABBBBCCCCD'
plainTextP = addPadding(plainText)
dataS = dict(enumerate(list(chunks(plainTextP, 8)), start=1))

hash = iv
for d in dataS:
    des = DES.new(dataS[d], DES.MODE_ECB)
    cipherT = des.encrypt(hash)

    hash = "".join(chr(ord(x) ^ ord(y)) for x, y in zip(hash, cipherT))
print("plaintext :{} ").format(plainText)
print("hash(base 16 encoded):") + str(map("".join, zip(*[iter(base64.b16encode(hash))] * 16)))