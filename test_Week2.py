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

q3Encrypt = '''I shall from now on select and take the ingots individually in my own yard, and I shall exercise against you my right of rejection because you have treated me with contempt'''
class TestCaesar(TestCase):
    #Question1
    def test_encryptQ1W2(self):
        key = -3
        encryptValue = encrypt(q1Encrypt,key)
        print (encryptValue)
        #Value is
        # Xka F pexii objxfk pxqfpcfba, xka molra ql exsb ybbk qeb cfopq tel exp bsbo bkglvba qeb corfq
        # lc efp tofqfkdp xp criiv xp eb zlria abpfob; clo jv abpfob exp ybbk kl lqebo qexk ql abifsbo
        # lsbo ql qeb abqbpqxqflk lc jxkhfka qeb cxipb xka cllifpe qxibp lc qeb yllhp lc zefsxiov, tefze,
        # qexkhp ql qexq lc jv qorb Alk Nrfulqb, xob bsbk klt qlqqbofkd, xka alryqibpp alljba ql cxii
        # clo bsbo. Cxobtbii


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
        EncrpytedValue = vigenereEncrypt(q3Encrypt,'password')
        print(EncrpytedValue)
        #Value is
        #xszshzwudmfgscevtlwupoegiacwpvvlcgglowegxvavqoconifeucnqnajvwbulhhsdhsohgcakaoxdxnkluclpnraydhfigebwyhzrcbwuwijhnomzwjvwgeslardhlilzycewtmhl

