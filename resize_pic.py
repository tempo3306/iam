from PIL import Image

img = Image.open('HK.png')
img = img.resize((144, 120))

img.save('hotkey.png')

# import cv2
#
# img = cv2.imread('HK.png', -1)
# img = cv2.resize(img, (144,120))
# cv2.imwrite('hotkey.png', img)