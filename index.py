import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid
import matplotlib.pyplot as plt

from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title('Calculating the Course Scores using Normalization')

st.write('Upload an excelsheet containing subjects and the respective marks for a semester as given in the sample below')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    AgGrid(df)
    st.bar_chart(df)
    st.header('After Normalization')
    df_min_max_scaled = df.copy()
    for column in df_min_max_scaled.columns:
    	df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min())	
    AgGrid(df_min_max_scaled)
    for column in df_min_max_scaled.columns:
        st.bar_chart(df_min_max_scaled[column])
    st.header('After Standardization')
    df_z_scaled = df.copy()
    for column in df_z_scaled.columns:
    	df_z_scaled[column] = (df_z_scaled[column] - df_z_scaled[column].mean()) / df_z_scaled[column].std()
    AgGrid(df_z_scaled)
    for column in df_z_scaled.columns:
        st.bar_chart(df_z_scaled[column])
    st.header('Scores for all the subjects')
    
    st.write(df_min_max_scaled.describe())

    df_sc=df_min_max_scaled.describe()
    
    df_score=df_sc.iloc[1,:]
    st.bar_chart(df_score)
    
