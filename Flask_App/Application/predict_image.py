import tensorflow as tf
from keras.preprocessing import image
import cv2
import numpy as np

models = {
    'm': 'Application/models/malaria.h5',
    'p': 'Application/models/pneumonia.h5'}

disease = {
    'm': 'Malaria',
    'p': 'Pneumonia'}

def pred (filename, x):

    model=tf.keras.models.load_model(models[x]) 
    img = cv2.imread('/home/shinjinee/Documents/Python Programs/DiseasePredictor/FlaskApp/Application/static/img/uploads/'+filename)

    resized = cv2.resize(img, (150,150), interpolation = cv2.INTER_AREA)	#resize
    resized = resized/255	#normalize

    x = image.img_to_array(resized)
    x = np.expand_dims(x, axis=0)

    final_img = np.vstack([x])
    prob = model.predict(final_img)
    
    if (prob < 0.5):
        return 'Not detected'
    else:
        return 'Detected'