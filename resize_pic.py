from PIL import Image

img = Image.open('login.png')
img = img.resize((136, 40),Image.ANTIALIAS)

img.save('login2.png')