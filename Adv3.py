__author__ = 'Barry'

from Crypto  import Random
from Crypto.Cipher import DES


def desFxn(text,key,MODE,Decrypt =False):
    iv_DES = Random.get_random_bytes(8)
    key_DES = key
    des = DES.new(key_DES,MODE,iv_DES)
    if Decrypt == True:
        return (des.decrypt(text))
    else:
        return (des.encrypt(text))

