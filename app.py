import streamlit as st
import pandas as pd

# Load the CSV you already downloaded or scraped in Colab
df = pd.read_csv('clustered_articles.csv')

for label in df['category'].unique():
    st.subheader(label)
    for url in df[df['category']==label]['url']:
        st.markdown(f"- [{url}]({url})")
