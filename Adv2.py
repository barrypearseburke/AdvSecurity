__author__ = 'Barry'
#Advance Security Week 2
import time
def caesar(s, k, decrypt=False):
    if decrypt: k = 26 - k

    r = ""

    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90):
            r += chr((ord(i) - 65 + k) % 26 +65)
        elif (ord(i) >= 97 and ord(i) <= 122):
            r += chr((ord(i) - 97 + k) % 26 + 97)
        else:
            r += i

    return r

def encrypt(p, k):
    return caesar(p, k)

def decrypt(c, k):
    return caesar(c, k, True)

def vigenereEncrypt(phrase,pw,decrypt=False):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    encryptValue = []
    phrase= list(phrase)
    counter =0
    for i in phrase:
        i = i.lower()
        if i in alphabet:
            phrasePos = alphabet.index(i)
            if counter > len(pw) -1 :
                keynumber = counter%len(pw)
                pwlist =list(pw)
                key=pwlist[keynumber]
                if key in alphabet:
                    keypos = alphabet.index(key)
            else:
                pwlist =list(pw)
                key=pwlist[counter]
                if key in alphabet:
                    keypos = alphabet.index(key)
            if decrypt == False:
                shift = phrasePos + keypos
            if decrypt == True:
                shift = phrasePos - keypos
            encryptValue.append(alphabet[shift%26])
            counter= counter+1
        else:
            continue

    return ''.join(encryptValue)

def vigenereDecryptBrute(phrase, knownWord,minLength,MaxLength,hint=False):
    t1=time.time()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    guessKey =[]
    returnvalues = []
    cipherCounter =0
    i =0
    phraseCracked = False
    if hint != False: # Cant brute force it. setting up a hint as to start brute force near where i know the key is
        for i in list(hint):
            guessKey.append(i)
    elif hint ==False:
        while i !=minLength:
            guessKey.append('a')
            i=i+1


    while phraseCracked == False:
        returnString = vigenereEncrypt(phrase,''.join(guessKey),decrypt=True)
        if knownWord in returnString:
            possiblesolution = (returnString,''.join(guessKey))#decrptedvalue,key used
            print('************************************')
            print("{0}{1}".format(possiblesolution[0],possiblesolution[1]))
            print('************************************')
            returnvalues.append(possiblesolution)

        changekey = False
        #change key

        cipherCounter = cipherCounter +1
        if cipherCounter%1000 ==0:
            t2=time.time()
            t3=t2-t1
            print("key at {0}".format(guessKey))
        lenofkey =len(guessKey)-1
        while changekey == False:
            if guessKey[lenofkey] == 'z':
                if lenofkey != 0:
                    guessKey[lenofkey] = 'a'
                    lenofkey = lenofkey-1
                else:
                    if len(guessKey) != MaxLength:
                        guessKey.append('a')
                        guessKey[0] ='a'
                        changekey =True
                    else:
                        print(' I give up')
                        return returnvalues
            else:
                if guessKey[lenofkey] in alphabet:
                    alphabetno = alphabet.index(guessKey[lenofkey])
                    alphabetno=alphabetno+1
                    guessKey[lenofkey] = alphabet[alphabetno]
                    changekey=True
    return returnvalues