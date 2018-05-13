from PIL import Image


# img  = Image.open(r'宋体.png')
img  = Image.open(r'微软.png')

img = img.resize((24 * 6, 20 * 6))
img.save(r'..\hotkey.png')