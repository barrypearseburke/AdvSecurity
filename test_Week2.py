from unittest import TestCase

from Adv2 import encrypt, decrypt,vigenereEncrypt,vigenereDecryptBrute
import time
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
q4decrypt = '''Yhwvtroi, 28 Yudq 2016 ­ Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv"+
"nsoyr uvs ndcljebv rk pkium hy bef; sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph"+
"fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv"+
"lanebx ejipkt, obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv"+
"gjskwusr pgoe zqbklsg. cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge pvvlw"+
"ipxfadogafua oj zfs kr uvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo,"+
"we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, ba wp oqdxny gj smhwy qgdogsdn, lzam nlql"+
"nmws poitwj wbu ptrg lbddsay'''
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


    def test_decrypt(self):
        #this tests decrpytion before brute forcing.
        EncrpytedValue = vigenereEncrypt(q3Encrypt,'password')
        DecrpytedValue = vigenereEncrypt(EncrpytedValue,'password',decrypt=True)
        self.assertEqual(DecrpytedValue,q3Encrypt.lower().replace(",","").replace(" ", ""))

    def test_brute(self):
        EncrpytedValue = vigenereEncrypt('TestPhrase','pass')
        t1=time.time()
        returnvalues = vigenereDecryptBrute(EncrpytedValue,'test',2,4,)
        t2 = time.time()
        t3 = t2-t1
        print("time Taken {}sec".format(t3))
        print("possible solutions")
        for i in returnvalues:
            print("pharse:{0}. Key:{1}".format(i[0],i[1]))

    def testq4w2(self):
        #question4
        t1=time.time()
        returnvalues = vigenereDecryptBrute(q4decrypt,'thursday',16,16)
        t2 = time.time()
        t3 = t2-t1
        print("time Taken {}sec".format(t3))
        print("possible solutions")
        for i in returnvalues:
            print("pharse:{0}. Key:{1}".format(i[0],i[1]))