
from PIL import Image
img = Image.open('cat.jpg')
img.convert("LA")
img.save('greyscale.png')
