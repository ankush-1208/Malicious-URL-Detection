import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# Importing streamlit
import streamlit as st
from PIL import Image
import pickle

pickle_in = open("logreg.pkl", "rb")
model = pickle.load(pickle_in);
image = Image.open('images/cover.png')

def welcome():
    return "Welcome All"

@st.cache
def predict_url(url):
    
    """You can check whether the URL is 
    Malicious or not here
        
    """
    lst = [];
    lst.append(url);
    prediction=model.predict(lst)
    lst.clear()
    return prediction

def main():
    # st.title("Malicious URL Detection App")
    html_temp = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Malicious URL Detector</title>
    <div>
    <h1 style='text-align: center; color: #ba181b; border: 4px solid #780000; padding: 3pxl; border-radius: 15px'>Malicious URL Detection App</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    text_for_url = """ 
    <h3 style='text-align: center'>Enter the URL you want to check</h3>   
    """
    st.image(image);
    st.markdown(text_for_url, unsafe_allow_html=True)
    url = st.text_input("")
    result=""
    if st.button("Perform URL Check"):
        result=predict_url(url)
    
    for element in result:
        if(element == 'good'):
            st.success('The URL is safe.')
        else:
            st.error('This is a Malicious URL!!')
    if st.button("About"):
        desc_html = """
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <p class="card-text">This is a Machine learning project. Here we are classifying the URLs as malicious or benign using logistic regression.</p>
        <a href="https://github.com/ankush-1208/Malicious-URL-Detection-">GitHub Link</a>
        """
        st.markdown(desc_html, unsafe_allow_html=True)

if __name__=='__main__':
    main()