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
            if counter > len(pw):
                keypos = counter%len(pw)
            else:
                keypos = counter

            shift = phrasePos + keypos
            encryptValue.append(alphabet[shift%26])

        else:
            continue
        counter= counter+1
