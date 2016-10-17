from unittest import TestCase
from Adv3 import removePadding,addPadding
from Adv4 import aesEncryptionECB

class TestEncrypt(TestCase):
    def testAESQ1(self):
         plaintext = 'AAAABBBBCCCCDDDDAA'
         plaintextWithPadding ='AAAABBBBCCCCDDDDAA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0014'
         key = '1234567812345678'
         text = addPadding(plaintext,32)
         self.assertEquals(text,plaintextWithPadding)
         encrypt = aesEncryptionECB(plaintextWithPadding,key)
         decrypt = aesEncryptionECB(encrypt,key)
         self.assertEqual(decrypt,plaintextWithPadding)

