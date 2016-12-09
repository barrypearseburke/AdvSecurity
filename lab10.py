from PIL import Image

import numpy as np
import scipy.misc as smp

im = Image.open("catBlack.png") #Can be many different formats.
pix = im.load()
print (im.size )#Get the width and hight of the image for iterating over
print (pix[1,1]) #Get the RGBA Value of the a pixel of an image
#pix[x,y] = value # Set the RGBA Value of the image (tup


data = np.zeros( (im.size[0],im.size[1],2), dtype=np.uint8 )

for i in range (im.size[0]):
    for j in range (im.size[1]):
        print (i,j)
        data[i,j] = pix[i,j]

im = Image.fromarray(data)
im.save("GreyCat.png")


# data[512,512] = [254,0,0]       # Makes the middle pixel red
# data[512,513] = [0,0,255]       # Makes the next pixel blue
#
# img = smp.toimage( data )       # Create a PIL image
# img.show()                      # View in default viewer
# im.size[1]
#
# data = np.zeros( (im.size[0],im.size[1],3), dtype=np.uint8 )