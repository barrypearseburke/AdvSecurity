import Crypto.Cipher.AES


class PKCS7Encoder(object):
    def __init__(self, k=16):
        self.k = k

    def unpad(self, text, l):

        val = l-len(text)
        text = text[:val]

        return text


def brute_force(passwdfile, c, padded):
    key = ""
    decrypted = ""

    for i in passwdfile:
        i = i.strip()

        if len(i) % 16 == 0:
            aes_decrypt = Crypto.Cipher.AES.new(i, Crypto.Cipher.AES.MODE_ECB)
            decrypted = aes_decrypt.decrypt(c)

            if decrypted == padded:
                key = i
                break

    return key, decrypted


def main():
    f = open("paswords.txt", 'r')

    p = "AAAABBBBCCCCDDDDAA"

    padded = "AAAABBBBCCCCDDDDAA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0014"

    c = "43d3215c92a75a1478fcf9cb950d20db502a485fd5735486d57aea9aa809e3dd"
    print 'Ciphertext to be brute-forced:\n%s\n\n' % c

    cipher = c.decode('hex')
    k, decrypted = brute_force(f, cipher, padded)

    print 'Decrypted- ', decrypted
    print 'Matched Key- ', k

    pclass = PKCS7Encoder()
    unpadded = pclass.unpad(decrypted, len(p))

    print 'Plain Text - ', unpadded


if __name__ == "__main__":
    main()
