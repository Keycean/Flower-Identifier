import os
from tensorflow import keras
from keras.models import load_model
import streamlit as st 
import tensorflow as tf
import numpy as np

st.header('FlowerNet Deep Learning for Flower Classification')
flower_names = ['Gumamela', 'Sunflower', 'Daisy', 'Dandelion', 'Rose', 'Tulip',]

model = keras.models.load_model('Flower_Recog_Model.keras')

def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array,0)

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    outcome = 'The Image belongs to ' + flower_names[np.argmax(result)] + ' with a score of '+ str(np.max(result)*100)
    return outcome

uploaded_file = st.file_uploader('Upload an Image')
if uploaded_file is not None:
    file_path = os.path.join('upload', uploaded_file.name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getvalue())

    st.image(uploaded_file, width = 350)

    st.markdown(classify_images(file_path))