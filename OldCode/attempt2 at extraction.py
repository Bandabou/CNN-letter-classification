import numpy as np
from PIL import Image
import cv2
import os

IMG_DIR = 'C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\Images\\test1.jpg'
print(IMG_DIR)

for img in os.listdir(IMG_DIR):
    img_array = cv2.imread(os.path.join(IMG_DIR,img), cv2.IMREAD_GRAYSCALE)
    
    img_pil = Image.fromarray(img_array)
    print(img_pil)
    img_28x28 = np.array(img_pil.resize((28, 28), Image.ANTIALIAS))
    print(img_28x28)
    
    flat = (img_28x28.flatten())
    #img_array  = img_array.reshape(-1,1).T
    print(flat)

    flat2 = flat.reshape(-1,1).T

print(flat2)

#Re-attempt:
image = Image.open('C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\Images\\test1.jpg')
 
print(image_reshaped)

image_okay = cv2.imread(IMG_DIR, 0)
print(image_okay)

image_aight = Image.fromarray(image_okay)
print(image_aight)

image_reshaped = np.array(image_aight.resize((28, 28), Image.ANTIALIAS))
print(image_reshaped) 

image_flat = (image_reshaped.flatten())


print(image_flat)

print(flat)





import csv

with open('C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\tryX.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(image_flat)
    #np.savetxt(f, flat, delimiter=",")








# from numpy import genfromtxt
# my_data = genfromtxt('C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\CNN-letter-classification\\test.csv', delimiter=',')

# print(my_data)

# from PIL import Image
# im = Image.fromarray(img_28x28)
# im.save("C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\CNN-letter-classification\\my_img.jpg")