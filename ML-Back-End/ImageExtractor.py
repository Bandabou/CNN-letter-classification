#Relevant imports


import numpy as np
from PIL import Image
import cv2
import os
import csv

  
IMG_DIR = 'C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\Images'
print(IMG_DIR)


#class Image_to_csv:
#An image loader function, which reshapes the files into a single array.
def load_image(IMG_DIR):
    global image_list 
    image_list = []
    for img in os.listdir(IMG_DIR):
        
        img_array = cv2.imread('C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\Images/'+img)
        gray_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        
        #print(img_array)
        img_pil = Image.fromarray(gray_array)
        #print(img_pil)
        img_28x28 = np.array(img_pil.resize((28, 28), Image.ANTIALIAS))
        #print(img_28x28)
        
        flat = (img_28x28.flatten())
        #image_list.append(flat.tolist())
        #print(image_list)
        #img_array  = img_array.reshape(-1,1).T
    #print(flat)
        
        with open('C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\tryX.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(flat)
        #np.savetxt(f, flat, delimiter=",")
    return(image_list)


load_image(IMG_DIR)	



def remove_empty_rows():
    
    with open('C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\tryX.csv', newline='') as in_file:
        with open('C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\clean.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)


remove_empty_rows()
