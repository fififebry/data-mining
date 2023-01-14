"""This module creates the home page."""

# Import necessary modules.
import streamlit as st
from PIL import Image

def app():
    st.title("Motor Pridiction app")
    img=Image.open("welcome.jpg")
    st.image(img)
    st.text(
        """
        This web app allows a user to predict the prices of a motorcycle based on their 
        engine size, horse power, peakrm, motor's file, company and etch.
        """
    )

