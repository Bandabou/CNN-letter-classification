from PIL import Image
import numpy as np
import csv



def load_image():
    image = Image.open('C:\\Users\\20183382\\Desktop\\CNN\\test1.jpg')
    resized= image.resize((28,28))
    resized.save('C:\\Users\\20183382\\Desktop\\CNN\\test1_resized.jpg')
    
    return(resized)




def array_maker():
    array_image =  np.array(Image.open('C:\\Users\\20183382\\Desktop\\CNN\\test1_resized.jpg'))
    print(array_image)
    return(array_image)

array_maker()

# load all images in a directory
from os import listdir
from matplotlib import image
# load all images in a directory
loaded_images = list()
for filename in listdir("C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\Images/"):
	# load image
	img_data = image.imread('C:\\Users\\20183382\\Desktop\\CNN\\CNN-letter-classification\\Images/' + filename)
	# store loaded image
	loaded_images.append(img_data)
	print('> loaded %s %s' % (filename, img_data.shape))


def csvWriter(array_image, nparray):
#   example = nparray.tolist()
#   with open(file_name+'.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerows(example)




load_image()

#csvWriter("myfilename", img)
