from tkinter.filedialog import SaveAs
from PIL import Image
import numpy as np
import csv
import pandas as pd



def load_image():
    image = Image.open('..\\Desktop\\CNN\\test1.jpg')
    resized= image.resize((28,28))
    resized.save('C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\\CNN-letter-classification\\test1_resized.jpg')
    
    return(resized)




def array_maker():
    array_image =  np.array(Image.open('C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\\CNN-letter-classification\\Images\\test1_resized.jpg'))
    print(array_image)
    return(array_image)
array_maker()

array_image =  np.asarray(Image.open('C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\\CNN-letter-classification\\Images\\test1_resized.jpg'))
   
print(array_image)

# load all images in a directory
from os import listdir
from matplotlib import image
# load all images in a directory
loaded_images = np()
for filename in listdir("C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\\CNN-letter-classification\\Images/"):
	# load image
	img_data = image.imread('C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\\CNN-letter-classification\\Images\\'  + filename)
	# store loaded image
	loaded_images.append(img_data)
	print('> loaded %s %s' % (filename, img_data.shape))

print(loaded_images)

def csvWriter(file_name, loaded_images):
    with open(file_name +'.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(loaded_images)
    
filename = 'C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\\CNN-letter-classification\\test'


csvWriter(filename, array_image)

# np.savetxt(filename, 
#            loaded_images,
#            delimiter =", ", 
#            fmt ='% s')
    


load_image()

array_maker()

csvWriter(filename, loaded_images)

#csvWriter("myfilename", img)
import matplotlib as img

imageMat = img.read('C:\\Users\\maxhi\\OneDrive\\Desktop\\CNN\\CNN-letter-classification\\Images\\test1_resized.jpg')
print("Image shape:", imageMat.shape)




import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/CNN-letter-classification/images'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 5GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, b