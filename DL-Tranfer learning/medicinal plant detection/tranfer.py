
import cv2
from glob import glob
import pathlib 
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense,Conv3D,MaxPool3D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from keras.models import load_model
model=load_model('heart.h5')
# model=r"C:\Users\MUJEEB\Desktop\upload\heart.h5"

from tensorflow.keras.preprocessing import image
# testing the model
from web import upload_video
x=r"C:\Users\MUJEEB\Desktop\upload\data\Azadirachta Indica (Neem)\AI-S-005.jpg"
def testing():
    path=x#upload_video()
    print(path)
    test_image = image.load_img(path, target_size = (224, 224))
    #print(test_image)
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image/255
    result = model.predict(test_image)
    print(result)
    if np.argmax(result)  == 0:        
      prediction = 'Rasna'
    elif np.argmax(result)  == 1:
      prediction = 'Arive-Dantu'
    elif np.argmax(result)  == 2:
      prediction ='Jackfruit'
      
  
    elif np.argmax(result)  == 3:
      prediction = 'Neem'
    elif np.argmax(result)  == 4:
      prediction ='Basale'
    elif np.argmax(result)  == 5:
      prediction = 'Indian Mustard'
    elif np.argmax(result)  == 6:
      prediction ='Karanda'  
    elif np.argmax(result)  == 7:
      prediction = 'Lemon'
    elif np.argmax(result)  == 8:
      prediction ='Roxburgh fig'
    elif np.argmax(result)  == 9:
      prediction = 'Peepal Tree'
    elif np.argmax(result)  == 10:
      prediction ='sinensis'  
    elif np.argmax(result)  == 11:
      prediction = 'Jasmine'
    elif np.argmax(result)  == 12:
      prediction ='Mango'
    elif np.argmax(result)  == 13:
      prediction = 'Mint'
    elif np.argmax(result)  == 14:
      prediction ='Drumstick'  
    elif np.argmax(result)  == 15:
      prediction = 'Jamaica Cherry-Gasagase'
    elif np.argmax(result)  == 16:
      prediction ='Curry'
    elif np.argmax(result)  == 17:
      prediction = 'Oleander'
    elif np.argmax(result)  == 18:
      prediction ='Parijata'  
    elif np.argmax(result)  == 19:
      prediction = 'Tulsi'
    elif np.argmax(result)  == 20:
      prediction ='Betel'
    elif np.argmax(result)  == 21:
      prediction = 'Mexican Mint'
    elif np.argmax(result)  == 22:
      prediction ='Indian Beech'  
    elif np.argmax(result)  == 23:
      prediction = 'Guava'
    elif np.argmax(result)  == 24:
      prediction ='Pomegranate'
    elif np.argmax(result)  == 25:
      prediction = 'Sandalwood'
    elif np.argmax(result)  == 26:
      prediction ='Jamun'  
    elif np.argmax(result)  == 27:
      prediction = 'Rose Apple'
    elif np.argmax(result)  == 28:
      prediction ='Crape Jasmine'
    elif np.argmax(result)  == 29:
      prediction = 'Fenugreek' 
    print(prediction)             
   

testing()
#
#print(x)


