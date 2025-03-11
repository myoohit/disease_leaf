import streamlit as st
import tensorflow as tf
import numpy as np
import gdown
import os


url='https://drive.google.com/file/d/1fl6J_XDwbWss9XwxOdM9ULKrRITDUMN5/view?usp=sharing'.file_id('1fl6J_XDwbWss9XwxOdM9ULKrRITDUMN5')
model_path='trained_plant_disease_model.keras'



def model_prediction(test_image):
    model='trained_plant_disease_model.keras'
    image=tf.keras.preprocessing.image.load_img(test_image,target_size=(224,224))
    input_arr=tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])
    predictions=model.predict(input_arr)
    return.np.argmax(predictions)

st.sidebar.title('Plant Disease Detection')
app_mode=st.sidebar.selectbox('Select Page', ['HOME','DISEASE RECOGNITION'])

if(app_mode=='HOME'):
    st.markdown("<h1 style='text-align: center; color: red;'>Plant Disease Detection</h1>", unsafe_allow_html=True)
elif(app_mode=='DISEASE RECOGNITION'):
    st.header("Plant Disease detection")
    test_image=st.file_uploader('choose an  image',type=['jpg','png','jpeg'])
    if(st.button('Show Image')):
        st.image(test_image,width=4,use_column_width=True)
    if(test_image is not None):
        st.snow()
        st.write('our prediction')
        result_index= model_prediction(test_image)
        class_name=['Patato_Early_Blight','Patato_Late_Blight','Patato_Healthy','Tomato_Early_Blight','Tomato_Late_Blight','Tomato_Healthy']
        st.success("Model is predictiing its a {}".format(class_name[result_index]))