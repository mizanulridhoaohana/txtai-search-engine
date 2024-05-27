import txtai
import numpy as np
import pandas as pd
import streamlit as st

def load_data_and_embeddings():
    df = pd.read_csv('./seth-data.csv').dropna()
    titles = df.title.values
    urls = df.url.values

    embeddings = txtai.Embeddings({
        'path': 'sentence-transformers/all-MiniLM-L6-v2'
    })

    embeddings.load('./embeddings-seth.tar.gz')

    return titles, urls, embeddings

titles, urls, embeddings = st.cache_data(load_data_and_embeddings)()

st.title('Seth blog Search Engine')

query = st.text_input("Enter search query : ")

if st.button('Search'):
    if query:
        result = embeddings.search(query,5)

        actual_results = [f'Title: {titles[x[0]]}, URL: {urls[x[0]]}' for x in result]

        for res in actual_results:
            st.write(res)
    else:
        st.write("Please enter query :")
