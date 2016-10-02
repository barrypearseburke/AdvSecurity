__author__ = 'Barry'
from Crypto.Cipher import AES,DES
from Crypto import Random

def des():
    iv_DES = Random.get_random_bytes(8)

    key_DES = 'abcdefgh'

    des = DES.new(key_DES,DES.MODE_CFB,iv_DES)

    plaintext = 'Hello! World'

    print ( plaintext == des.decrypt(des.encrypt(plaintext)))

if __name__ =='__main__':
    des()