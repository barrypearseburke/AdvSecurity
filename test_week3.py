from unittest import TestCase
from Adv3 import des
__author__ = 'Barry'


class TestEncrypt(TestCase):
     def test_des(self):
         plaintext = 'AAAABBBBAAAABBBB'
         key = '12345678'
         encrypt = des(plaintext,key)
         self.assertEqual(plaintext, des(encrypt,key,Decrypt=True).decode("utf-8") )
         decrypt = des('19FF4637BB2FE77C19FF4637BB2FE77C',key,Decrypt=True)
         print(encrypt)
         print(decrypt)