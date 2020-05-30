import pandas as pd
import numpy as np
# libraries for making count matrix and similarity matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# reading the data from the preprocessed .csv file
cust_tags_list= pd.read_csv('Customer_Tags.csv')
mv_tags_list= pd.read_csv('Table_advert1.csv')
