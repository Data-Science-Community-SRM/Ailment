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

    if (x=='p'):
        resized = cv2.resize(img, (150,150), interpolation = cv2.INTER_AREA)	#resize
        resized = resized/255	#normalize

        x = image.img_to_array(resized)
        x = np.expand_dims(x, axis=0)

        final_img = np.vstack([x])
        prob = model.predict(final_img)
        print (prob)
        if (prob < 0.5):
            return 'Pneumonia not detected'
        else:
            return 'Pneumonia detected'

    if (x=='m'):
        resized = cv2.resize(img, (50,50), interpolation = cv2.INTER_AREA)	#resize
        resized = resized/255	#normalize

        x = image.img_to_array(resized)
        x = np.expand_dims(x, axis=0)

        class_name = ['Malaria not detected', 'Malaria detected']

        final_img = np.vstack([x])
        classes = model.predict(final_img)
        classes = np.reshape(classes, (2,))
        idx = np.argmax(classes)

        return class_name[idx]