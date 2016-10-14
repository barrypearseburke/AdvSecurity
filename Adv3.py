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
        for i in range(padding-2):
            String = String+'\x00'
        String = String+'0{0}'.format(padding)
    else:
        String = String+'0{0}'.format(padding)
    return(String)

