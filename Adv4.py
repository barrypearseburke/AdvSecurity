from Crypto.Cipher import AES
from Crypto import Random

def aesEncryptionECB(text,key,Decrypt =False):
    key = key
    cipher = AES.new(key, AES.MODE_ECB)
    if Decrypt == True:
        return  cipher.decrypt(text)
    else:
        return cipher.encrypt(text)