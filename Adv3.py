__author__ = 'Barry'

from Crypto  import Random
from Crypto.Cipher import DES


def desFxn(text,key,MODE,iv_DES = Random.get_random_bytes(8),Decrypt =False):
    key_DES = key
    des = DES.new(key_DES,MODE,iv_DES)
    if Decrypt == True:
        return (des.decrypt(text))
    else:
        return (des.encrypt(text))

def removePadding(string):
    paddingLength = int(string[-2:])
    return string[:-paddingLength]

def addPadding(String,keylen):
    if len(String) == int(keylen):
        return String
    padding = int(keylen)%len(String)
    if padding >2:
        paddedString = String+'\x00\x000{0}'.format(padding)
    else:
        paddedString = String+'0{0}'.format(padding)
    return(paddedString)

