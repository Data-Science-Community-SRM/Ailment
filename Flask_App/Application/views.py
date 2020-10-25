from Application import A
from flask import render_template, request, redirect
from datetime import datetime
import os
import urllib
#from werkzeug.utils import secure_filename
import cv2
import numpy as np
from Application import predict_image as pr

@A.route('/')
def index():
	return render_template('public/index.html')

A.config['IMAGE_UPLOADS'] = '/home/shinjinee/Documents/Python Programs/DiseasePredictor/FlaskApp/Application/static/img/uploads'
A.config['ALLOWED_EXTENSIONS'] = ['PNG', 'JPG', 'JPEG']

def allowed_files(file):
	if not '.' in file:
		return False
	ext = file.rsplit('.', 1)[1]
	if ext.upper() in A.config['ALLOWED_EXTENSIONS']:
		return True
	else:
		return False

def verify(img, text):

	if img.filename == '':
		text = 'Image must have a filename'
		return False

	if not allowed_files(img.filename):
		text = 'Invalid file type (valid: png, jpg, jpeg)'
		return False

	else:
		return True


@A.route('/malaria', methods=['GET', 'POST'])
def malaria():
	
	text = ''
	if request.method == 'POST':

		if request.files:
			image = request.files['image']

			if verify(image, text):

				image.save(os.path.join(A.config["IMAGE_UPLOADS"], image.filename))				
				text = 'Image Uploaded: '+image.filename

				prediction = pr.pred(image.filename, 'm')
				
		return render_template('public/malaria.html', text=text, prediction=prediction, filename=image.filename)

	return render_template('public/malaria.html', filename='')

# 


@A.route('/pneumonia', methods=['GET', 'POST'])
def pneumonia():
	text = ''
	if request.method == 'POST':

		if request.files:
			image = request.files['image']

			if verify(image, text):

				image.save(os.path.join(A.config["IMAGE_UPLOADS"], image.filename))				
				text = 'Image Uploaded: '+image.filename

				prediction = pr.pred(image.filename, 'p')
				
		return render_template('public/pneumonia.html', text=text, prediction=prediction, filename=image.filename)
	return render_template('public/pneumonia.html', filename='')




@A.route('/cardio', methods=['GET', 'POST'])
def cardio():
	return render_template('public/cardio.html')

@A.route('/liver', methods=['GET', 'POST'])
def liver():
	return render_template('public/liver.html')



#image.save(os.path.join(A.config['IMAGE_UPLOADS'], file))
#mongo.save_file(image.filename, image)
#image = mongo.send_file(image.filename)

#from flask_pymongo import PyMongo

#A.config['MONGO_URI'] = 'mongodb+srv://shinjinee:'+urllib.parse.quote('Jins@mongo04122000')+'@diseasepredictor.nxyfe.mongodb.net/diseasePredictor?retryWrites=true&w=majority'
#mongo = PyMongo(A)