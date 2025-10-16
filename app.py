# setup
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import torch 
import keras
from PIL import Image


# Load Model
# Load Model
model = keras.models.load_model('model.keras')



# Interface

# title
with st.container():
    image_col, heading_col = st.columns([.5, 1.5], vertical_alignment='center')

    with image_col:
        st.image('Images/logo.jpg', width=150)

    with heading_col:
        st.write('# :rainbow[Pneumonia Detector]')
        st.write('**:blue[Pneumonia Detector is a deep learning image classification model, that classifies the lungs x-ray images into Pneumonial and Normal.]**')

# Input and Output 
with st.container():
    image = st.file_uploader('**:orange[UPLOAD XRAY IMAGE]**', accept_multiple_files=False)
    if image:
        input_col, output_col = st.columns(2, border=False)
        with input_col:
            st.image(image=image, use_container_width=True)

        with output_col:
            image = Image.open(image)
            image = image.resize((180, 180))
            image = tf.expand_dims(image, axis=0)
            prediction = model.predict(image)
            if prediction < 0.5:
                st.image('Images/Normal.jpg')
            else:
                st.image('Images/Pneumonia.jpg')

# Share Contents
with st.container():
    github_col, linkedin_col, huggingface_col = st.columns(3, border=False)

    with github_col:
        st.link_button('**GITHUB**', icon=':material/code:', url='https://github.com/Ramesh143-code/todo-luxe', use_container_width=True, help='View the Project Source Code on GitHub ▶️')

    with linkedin_col:
        st.link_button('**LINKEDIN**', icon=':material/group_add:', url='https://www.linkedin.com/in/p-ramesh-477482304', use_container_width=True, help='Connect With Me 😊')

    with huggingface_col:
        st.link_button('**STREAMLIT PROFILE**', icon=':material/deployed_code:', url='https://share.streamlit.io/user/ramesh143-code', use_container_width=True, help='MY DEPLOYED STREAMLIT PROJECTS 🤗')


# setup
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import torch 
import keras
from PIL import Image


# Load Model
# Load Model
model = keras.models.load_model('model.keras')



# Interface

# title
with st.container():
    image_col, heading_col = st.columns([.5, 1.5], vertical_alignment='center')

    with image_col:
        st.image('Images/logo.jpg', width=150)

    with heading_col:
        st.write('# :rainbow[Pneumonia Detector]')
        st.write('**:blue[Pneumonia Detector is a deep learning image classification model, that classifies the lungs x-ray images into Pneumonial and Normal.]**')

# Input and Output 
with st.container():
    image = st.file_uploader('**:orange[UPLOAD XRAY IMAGE]**', accept_multiple_files=False)
    if image:
        input_col, output_col = st.columns(2, border=False)
        with input_col:
            st.image(image=image, use_container_width=True)

        with output_col:
            image = Image.open(image)
            image = image.resize((180, 180))
            image = tf.expand_dims(image, axis=0)
            prediction = model.predict(image)
            if prediction < 0.5:
                st.image('Images/Normal.jpg')
            else:
                st.image('Images/Pneumonia.jpg')

# Share Contents
with st.container():
    github_col, linkedin_col, huggingface_col = st.columns(3, border=False)

    with github_col:
        st.link_button('**GITHUB**', icon=':material/code:', url='https://github.com/Ramesh143-code/Pneumonia-Detector', use_container_width=True, help='View the Project Source Code on GitHub ▶️')

    with linkedin_col:
        st.link_button('**LINKEDIN**', icon=':material/group_add:', url='https://www.linkedin.com/in/p-ramesh-477482304', use_container_width=True, help='Connect With Me 😊')

    with huggingface_col:
        st.link_button('**STREAMLIT PROFILE**', icon=':material/deployed_code:', url='https://share.streamlit.io/user/ramesh143-code', use_container_width=True, help='MY DEPLOYED STREAMLIT PROJECTS 🤗')


# streamlit run app.py
