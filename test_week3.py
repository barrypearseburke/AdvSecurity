from unittest import TestCase
from Adv3 import desFxn,removePadding,addPadding
from Crypto.Cipher import DES
__author__ = 'Barry'


class TestEncrypt(TestCase):
    def test_desECB(self):
         plaintext = 'AAAABBBBAAAABBBB'
         key = '12345678'
         encrypt = desFxn(plaintext,key,DES.MODE_ECB)
         self.assertEqual(plaintext, desFxn(encrypt,key,DES.MODE_ECB,Decrypt=True).decode("utf-8"))

    def test_desCBC(self):
        plaintext ='AAAABBBBAAAABBBB'
        key = '12345678'
        iv ='00000000'
        encrypt = desFxn(plaintext, key, DES.MODE_CBC,iv_DES=iv)
        self.assertEqual(plaintext, desFxn(encrypt, key, DES.MODE_CBC,iv_DES=iv, Decrypt=True).decode("utf-8"))


    def test_removePadding(self):
        textWithPadding ='AAAABBBBCCCC\x00\x0004'
        plaintext = 'AAAABBBBCCCC'
        removed =removePadding(textWithPadding)
        self.assertEqual(plaintext,removed)

    def test_addPadding(self):
        textWithPadding ='AAAABBBBCCCC\x00\x0004'
        plaintext = 'AAAABBBBCCCC'
        added = addPadding(plaintext,16)
        self.assertEqual(textWithPadding,added)