from unittest import TestCase
from Adv1 import encrypt, decrypt , encrypt2, decrypt2
__author__ = 'Barry'
#Week1 run his code

class TestEncrypt(TestCase):
    #Question1
    def test_encrypt(self):
        key = 3
        p = 'TestPhrase'
        encryptValue = encrypt(p,key)
        decryptValue  = decrypt(encryptValue,key)
        self.assertEqual(decryptValue,p)

    #Question2
    def test_encrptQ2(self):
        key = 3
        p = 'TestPhrase'
        encryptValue = encrypt2(p,key)
        decryptValue  = decrypt2(encryptValue,key)
        self.assertEqual(decryptValue,p)