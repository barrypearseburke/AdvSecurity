from PIL import Image

import numpy as np
import scipy.misc as smp

im = Image.open("catBlack.png")
pix = im.load()
# print (im.size )#Get the width and hight of the image for iterating over
UserInput = input(" Enter a message and it shall be hidden in plain sight")
ascistring = []
for c in UserInput:
    ascistring.append("0{0:b}".format(
        ord(c)))  # converts  char to asci and asci to bits and puts a 0 in front of it to make it 8 bits
print(ascistring)

data = np.zeros((im.size[0], im.size[1], 2), dtype=np.uint8)
counterbits = 0
counterletters = 0
adding = True
for i in range(im.size[0]):
    for j in range(im.size[1]):
        print(i, j)
        # change each pix value to bits

        bits = "{0:08b}".format(pix[i, j][0])
        # test
        bits = list(bits)
        if adding == True:
            bits[6], bits[7] = ascistring[counterletters][counterbits:counterbits + 2]
            if counterbits == 6:
                counterbits = 0
                if counterletters != (len(ascistring) - 1):
                    counterletters = counterletters + 1
                else:
                    adding = False
            else:
                counterbits = counterbits + 2

        bits = ''.join(bits)
        value = int(bits, 2)
        #
        data[i, j] = value, pix[i, j][1]

im = Image.fromarray(data)
im.save("GreyCat.png")
