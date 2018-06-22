from PIL import Image


# img  = Image.open(r'宋体.png')
img  = Image.open(r'..\icons\quick1.png')

img = img.resize((34, 31))
img.save(r'..\icons\quick.png')