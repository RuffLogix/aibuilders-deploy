import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from model import Predict


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file)
    st.image(uploaded_image)

    # img = np.array(uploaded_image.getdata())

    st.image(Predict(uploaded_image))
    # st.write(np.array(uploaded_image.getdata()).reshape(uploaded_image.size[0], uploaded_image.size[1], 3).shape)

    # img = np.array(uploaded_image.getdata()).reshape(uploaded_image.size[0], uploaded_image.size[1], 3)

    # st.write(img.shape)
    # st.image(Predict(img))
    # st.image(Predict(uploaded_image))