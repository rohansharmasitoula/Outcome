import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid
import matplotlib.pyplot as plt
#import plotly.figure_factory as ff
st.title('Programme Outcome using Normalization')

st.write('Upload an excelsheet containing marks for a semester')
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
    st.bar_chart(df_min_max_scaled)
    st.header('After Standardization')
    df_z_scaled = df.copy()
    for column in df_z_scaled.columns:
    	df_z_scaled[column] = (df_z_scaled[column] - df_z_scaled[column].mean()) / df_z_scaled[column].std()
    AgGrid(df_z_scaled)
    st.bar_chart(df_z_scaled)
    #fig = ff.create_distplot(df, bin_size=[.1, .25, .5])
    #st.plotly_chart(fig, use_container_width=True)


	


