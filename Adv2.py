__author__ = 'Barry'
#Advance Security Week 2
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

def vigenereEncrypt(phrase,pw):
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
            shift = phrasePos + keypos
            encryptValue.append(alphabet[shift%26])
            counter= counter+1
        else:
            continue

    return ''.join(encryptValue)