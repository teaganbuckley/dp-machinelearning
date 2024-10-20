import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App', icon=":material/thumb_up:")

st.info('This app builds a machine learning model.')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  
  st.write('**X**')
  X = df.drop('species', axis=1)
  X
  
  st.write('**Y**')
  Y = df.species
  Y

with st.expander('Data Visualization'):
  st.write('**This is a Scatter Chart**')
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
  st.write('**This is a Bar Chart**')
  st.bar_chart(data=df, x='bill_length_mm', y='body_mass_g', color='#ffaa0088', x_label='Bill Length (MM)', y_label='Body Mass (G)')