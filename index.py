import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from plotly.subplots import make_subplots
import plotly.graph_objects as go
from PIL import Image
st.title('Calculating the Course Scores using Normalization')

st.write('Upload a CSV file containing subjects and the respective marks for a semester as given in the sample below')

image = Image.open('sample.jpg')
st.image(image, caption='sample')
sample=pd.read_csv('sample.csv')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.table(df)
    st.bar_chart(df)
    st.header('After Normalization')
    df_min_max_scaled = df.copy()
    for column in df_min_max_scaled.columns:
    	df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min())	
    st.table(df_min_max_scaled)
    for column in df_min_max_scaled.columns:
        st.bar_chart(df_min_max_scaled[column])
    st.header('After Standardization')
    df_z_scaled = df.copy()
    for column in df_z_scaled.columns:
    	df_z_scaled[column] = (df_z_scaled[column] - df_z_scaled[column].mean()) / df_z_scaled[column].std()
    st.table(df_z_scaled)
    for column in df_z_scaled.columns:
        st.bar_chart(df_z_scaled[column])
    st.header('Scores for all the subjects')
    
    st.write(df_min_max_scaled.describe())

    df_sc=df_min_max_scaled.describe()
    df_new=df_min_max_scaled.mean();

    
    df_score=df_sc.iloc[1,:]
    st.bar_chart(df_score)
