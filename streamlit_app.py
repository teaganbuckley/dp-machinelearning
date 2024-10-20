import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learning model.')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

st.wite('**X**')
X = df.drop('species', axis=1)
X

st.write('**Y**')
Y = df.species
Y
