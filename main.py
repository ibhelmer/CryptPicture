# Python program to read image using OpenCV
# importing OpenCV(cv2) module
import base64
import cv2
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)
# Save image in set directory
# Read RGB image
#img = cv2.imread('image.png')
#imgcrypt = cipher.encrypt(img)
# Output img with window name as 'image'
#cv2.imshow('image', img)
#print(img)
# Maintain output window utill
# user presses a key
#cv2.waitKey(0)
# Destroying present windows on screen
#cv2.destroyAllWindows()
import base64

with open("image.png", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())
print(converted_string)
imgcrypt = cipher.encrypt(converted_string)
with open('image.bin', "wb") as file:
    file.write(imgcrypt)

file = open('image.bin', 'rb')
byte = file.read()
file.close()

decodeit = open('crypimg.jpg', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()