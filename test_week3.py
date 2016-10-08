from unittest import TestCase
from Adv3 import desFxn
from Crypto.Cipher import DES
__author__ = 'Barry'


class TestEncrypt(TestCase):
     def test_desECB(self):
         plaintext = 'AAAABBBBAAAABBBB'
         key = '12345678'
         encrypt = desFxn(plaintext,key,DES.MODE_ECB)
         self.assertEqual(plaintext, desFxn(encrypt,key,DES.MODE_ECB,Decrypt=True).decode("utf-8") )
