import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

def main():
    from PIL import Image
    #image_hospital = Image.open('head.png')
    #st.sidebar.image(image_hospital)
    image_ban = Image.open('head.png')
    st.image(image_ban, use_column_width=True)

if __name__ == '__main__':
    main()


st.write("""
# Machine Learning Applications for Predicting Intracranial Injury of Pediatric Traumatic Brain Injury
""")

st.write ("""
## Tunthanathip et al. 

""")

#st.write("""
### Performance of various algorithms from the training dataset >>> [Link](https://pedtbi-train.herokuapp.com/) 
#""")

st.write ("""
### Apply algorithms with unseen data

""")

st.markdown( "  [Random forest] (https://ct-pedtbi-test-rf.herokuapp.com/) ")
st.markdown( "  [Logistic Regression] (https://ct-pedtbi-test-ln.herokuapp.com/) ")
st.markdown( "  [Neural Network] (https://ct-pedtbi-test-nn.herokuapp.com/) ")
st.markdown( "  [naive Bayes] (https://ct-pedtbi-test-nb.herokuapp.com/) ")
st.markdown( "  [Support Vector Machines] (https://ct-pedtbi-test-svm.herokuapp.com/) ")
st.markdown( "  [Nomogram] (https://psuneurosx.shinyapps.io/ct-pedtbi-nomogram/) ")

st.write ("""
### [Home](https://ct-pedtbi-home.herokuapp.com/)

""")
