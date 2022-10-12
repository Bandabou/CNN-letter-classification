import numpy as np
from PIL import Image
import cv2
import os

IMG_DIR = 'C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\\CNN-letter-classification\\Images'
print(IMG_DIR)

for img in os.listdir(IMG_DIR):
    img_array = cv2.imread(os.path.join(IMG_DIR,img), cv2.IMREAD_GRAYSCALE)
    
    img_pil = Image.fromarray(img_array)
    print(img_pil)
    img_28x28 = np.array(img_pil.resize((28, 28), Image.ANTIALIAS))
    print(img_28x28)
    img_array = (img_28x28.flatten())
    
    #img_array  = img_array.reshape(-1,1).T

    print(img_array)

    with open('C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\CNN-letter-classification\\try.csv', 'ab') as f:

        np.savetxt(f, img_array, delimiter=",")




from numpy import genfromtxt
my_data = genfromtxt('my_file.csv', delimiter=',')

from PIL import Image
im = Image.fromarray(A)
im.save("your_file.jpeg")