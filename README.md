<p align="center">
<a href="https://dscommunity.in">
	<img src="https://github.com/Data-Science-Community-SRM/template/blob/master/Header.png?raw=true" width=80%/>
</a>
	<h2 align="center"> Disease Predictor </h2>
	<h4 align="center"> Disease prediction for Pneumonia, Malaria, Liver Disease and Cardiovascular Disease <h4>
</p>
	
## Preview


- <p> Sample output for Pneumonia Prediction using Lung X-ray images </p>
<p align="center">
  <img src="Sample output/pneumonia positive.png" alt="Web app output #1" width="800" height="450">
</p>
<p align="center">
  <img src="Sample output/pneumonia negative.png" alt="Web app output #2"  width="800" height="450">
</p>
<br>

- <p> Sample output for Malaria Prediction using cell images </p>
<p align="center">
  <img src="Sample output/malaria positive.png" alt="Web app output #3" width="800" height="450">
</p>
<p align="center">
  <img src="Sample output/malaria negative.png" alt="Web app output #4" width="800" height="450">
</p>

<br>

## The Flask Web Application

- The Web Application has been built with Flask in the backend and HTML and Bootstrap for the frontend.
- Respective images (.jpg, .jpeg, .png) can be uploaded to get predictions for Pneumonia and Malaria.
- Functionality for preventing upload of file of any format other than .jpg, .jpeg and .png has been included.
- Sample images are included in the [Sample images](https://github.com/Data-Science-Community-SRM/disease-predictor/tree/master/Sample%20images) folder.

### Execution

- The prerequisites for running the Flask Application are included in the requirements.txt file.
- To run the application:
```
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```
<br>

## The Models

### Pneumonia Model

- The [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) dataset from [Kaggle](https://www.kaggle.com/) has been used to train this model.
- This model has been trained to identify 2 classes (Positive or negative for Pneumonia) using transfer learning on the InceptionV3 model till layer ‘mixed7’, followed by a Dense layer with 512 nodes (RelU), and a sigmoid layer with 1 output node using Keras with Tensorflow backend. 
- It was trained using the RMSprop optimizer with a batch size of 64. Input size of the images were (150, 150, 3). The images were rescaled before training. ([trainPneumonia.ipynb](https://github.com/Data-Science-Community-SRM/disease-predictor/blob/master/trainPneumonia.ipynb))
- The final trained model resulted in an accuracy of 85.2% on the test set with 777 images.
- Each image is resized to 150x150 and then normalized before feeding into the network to make a prediction. 

### Malaria Model

- The [Malaria Cell Images Dataset](https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria) dataset from [Kaggle](https://www.kaggle.com/) has been used to train this model.
- It was trained using the public Kaggle notebook [Detecting Malaria (val accuracy > 97%)](https://www.kaggle.com/harshel7/detecting-malaria-val-accuracy-97).
