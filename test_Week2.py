from unittest import TestCase

from Adv2 import encrypt, decrypt,vigenereEncrypt

__author__ = 'Barry'

q1Encrypt='''
And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit
of his writings as fully as he could desire; for my desire has been no other than to deliver
over to the detestation of mankind the false and foolish tales of the books of chivalry, which,
thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall
for ever. Farewell'''

q2Decrypt = '''Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur zrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlfznqr uvz nfx jurgure fbzrbar zvtug or
uvqvat ure sebz gur jbeyq'''

class TestCaesar(TestCase):
    #Question1
    def test_encryptQ1W2(self):
        key = -3
        encryptValue = encrypt(q1Encrypt,key)
        print (encryptValue)


    #Question 2
    def test_decryptQ2W2(self):
        key = 0
        while key <27:
            decryptValue = decrypt(q2Decrypt,key)
            print('\n key:{}'.format(key))
            print(decryptValue)
            key =key+1
        #key 13 is answer

    #Question 3
    def test_encryptQ3W2(self):
        vigenereEncrypt('MyPhrase','pass')