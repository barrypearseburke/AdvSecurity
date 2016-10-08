__author__ = 'Barry'
from Crypto.Cipher import AES,DES
from Crypto import Random

def des(text,key,Decrypt =False):
    iv_DES = Random.get_random_bytes(8)
    key_DES = key
    des = DES.new(key_DES,DES.MODE_ECB,iv_DES)
    if Decrypt == True:
        return (des.decrypt(text))
    else:
        return (des.encrypt(text))

if __name__ =='__main__':
    des()