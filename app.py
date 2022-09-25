import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



# Title with big font
st.header('Warning!!!')

# Subtitle
st.subheader('''\n\n\nYou cannot take a Photo of the Screen as it is voilation of the company regulation.\n\n\n''')


image = Image.open('forbidden.jpg')
new_image = image.resize((500, 500))
st.image(new_image)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 