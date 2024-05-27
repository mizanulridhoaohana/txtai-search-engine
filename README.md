
# Search Engine Using Sentence-Transformers

This project demonstrates the implementation of a search engine using the `sentence-transformers/all-MiniLM-L6-v2` model from the txtai library. The search engine leverages embeddings to provide efficient and accurate search results. Two datasets are used in this project: Amazon product data and Seth-website data.

## Features

- **Embedding Model**: Utilizes the `sentence-transformers/all-MiniLM-L6-v2` model for creating embeddings.
- **Datasets**: Includes Amazon product data and Seth-website data to train and test the search engine.
- **txtai Library**: Employs the txtai library for managing and querying embeddings.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/mizanulridhoaohana/txtai-search-engine
   cd txtai-search-engine 
   ```
2. Install the required dependencies

   ```
   pip install -r requirements.txt 
   ```
3. Download Dataset

   You can dowload dataset from this link:

   - https://www.kaggle.com/datasets/piyushjain16/amazon-product-data
   - https://www.kaggle.com/datasets/glushko/seth-godins-blogs-dataset

## Usage
Data Preparation: Ensure your datasets (Amazon and Seth-website data) are in the appropriate format and placed in the data directory.



1. Generate Embeddings: Run the script to generate embeddings for the datasets.
```
main.ipynb
```
2. Run with Streamlit: Use Streamlit for web-based deployment.
```
streamlit run app_main.py
```
