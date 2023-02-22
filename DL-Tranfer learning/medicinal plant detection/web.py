# from crypt import methods
# from distutils.log import debug
import pathlib
from urllib import response
from app import app
from flask import Flask, render_template, request,redirect, url_for,flash
from werkzeug.utils import secure_filename

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# import torch
# from torch.utils.model_zoo import load_url
import matplotlib.pyplot as plt
#from scipy.special import expit

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
import sys
sys.path.append('..')
prediction=""


@app.route('/')
def home():
    return render_template('home.html')




@app.route('/upload_video', methods=['POST'])
def upload_video():


    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        y=('static/uploads/'+ filename)
        print(y)
        

        def testing_image(path):
            global prediction
          
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

           

            return(prediction)             
        filename=y
        testing_image(y)
        print(prediction)
        #@app.route('/display/y')
        #def display_image(filename):
            #print('display_image filename: ' + filename)
            #eturn redirect(url_for('static', filename='uploads/' + filename), code=301)
        #return render_template('detection.html',path.format(filename))
        #return render_template('home.html',)

        return render_template('home.html',out="Your selected leaf is {}".format(prediction),path=(filename))
        

        


if __name__=="__main__":
    app.run(debug= True)
