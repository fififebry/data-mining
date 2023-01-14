"""This create prediction page"""

# Import necessary module
import streamlit as st
import pickle
import pandas as pd
import numpy as np


with open("saved_rfr.pkl", "rb") as file:
    data2=pickle.load(file)

def predict_note_authentication(speedometer, enginesize, maks_kecepatan, peakrpm,  surat, maintenance, Company):
        prediction=data2.predict([[speedometer, enginesize, maks_kecepatan, peakrpm, surat, maintenance, Company]])
        print(prediction)
        return prediction 
    
def app(df):
    st.title("Price Prediction Model")

    surat={
        "ada",
        "tidak"
    }

    maintenance={
        "tidak",
        "ada"
    }

    
    Company=(
        "bajaj",
        "royal",
        "honda",
        "yamaha",
        "TVS",
        "hero",
        "KTM",
        "suzuki"
    )

    speedometer=st.slider("jarak_tempuh(km)", float(df["speedometer"].min()), float(df["speedometer"].max()))
    enginesize=st.slider("enginesize(cc)", float(df["enginesize"].min()), float(df["enginesize"].max()))
    maks_kecepatan=st.slider("maks_kecepatan(km/jam)",float(df["maks_kecepatan"].min()), float(df["maks_kecepatan"].max()))
    peakrpm=st.slider("peakrpm(rpm)", float(df["peakrpm"].min()), float(df["peakrpm"].max()))
    surat=st.selectbox("Ada surat atau tidak?", surat)
    maintenance=st.selectbox("Pernah perbaikan atau tidak?", maintenance)
    Company=st.selectbox("Company", Company)

    result=""
    ok=st.button("Calculate Price")
    if ok:

        result=predict_note_authentication(speedometer, enginesize, maks_kecepatan, peakrpm,  surat, maintenance, Company)
        st.success("".format(result))
        st.subheader(f"The Estimated Price is {result[0]:.2f}")
    