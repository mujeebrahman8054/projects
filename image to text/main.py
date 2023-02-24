# from crypt import methods
# from distutils.log import debug
import pathlib
from urllib import response
from app import app
from flask import Flask, render_template, request,redirect, url_for,flash
from werkzeug.utils import secure_filename
from PIL import Image
from pytesseract import pytesseract
from textspeek import text_to_speech
text=""

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

# model=r"C:\Users\MUJEEB\Desktop\upload\heart.h5"

from tensorflow.keras.preprocessing import image
import sys

sys.path.append('..')
prediction=""




@app.route('/')
def home():
    return render_template('home2.html')




@app.route('/imgtotxt', methods=['POST'])

def imgtotxt():
    #def text_to_speech(data):
      
    
        
        



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
            # import win32com.client as wincom
            # speak = wincom.Dispatch("SAPI.SpVoice")
            global text
            path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            #Define path to image
            path_to_image = path
            #Point tessaract_cmd to tessaract.exe
            pytesseract.tesseract_cmd = path_to_tesseract
            #Open image with PIL
            img = Image.open(path_to_image)
            #Extract text from image
            text = pytesseract.image_to_string(img)
            print(type(text))
            #speak.Speak(text)
            #print(path)
        

        text_to_speech(text)   
        filename=y
        testing_image(y)

        return render_template('home2.html',out=text)
        

        


if __name__=="__main__":
    app.run(debug= True)
