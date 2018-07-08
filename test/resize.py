from PIL import Image

# img  = Image.open(r'宋体.png')
img  = Image.open(r'热键3.png')

# 476  326
# 600

img = img.resize((160, 138))
img.save(r'new1.png')