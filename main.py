import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import re
from PIL import Image
import umap
import matplotlib.pyplot as plt
import seaborn as sns
# libraries for making count matrix and similarity matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# define a function that creates similarity matrix
# if it doesn't exist


# defining a function that recommends 10 most similar movies
def rcmd(movie):

    cust_tags_list= pd.read_csv('Customer_Tags.csv')
    mv_tags_list= pd.read_csv('Table_advert1.csv')
    movie= (input ("Input the name of the Customer"))
    target_tag_list = cust_tags_list[cust_tags_list.Customer_ID == movie].tag_list.values[0]
    mv_tags_list_sim = mv_tags_list[['Title','tag_list']]
    mv_tags_list_sim['jaccard_sim'] = mv_tags_list_sim.tag_list.map(lambda x: len(set(x).intersection(set(target_tag_list))) / len(set(x).union(set(target_tag_list))))
    text = ','.join(mv_tags_list_sim.sort_values(by = 'jaccard_sim', ascending = False).head(25)['tag_list'].values)
    bool_series = pd.notnull(mv_tags_list_sim["Title"])
    mv_tags_list_sim.sort_values(by = 'jaccard_sim', ascending = False).head(10)[bool_series] 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    r = rcmd(movie)
    movie = movie.upper()
    if type(r)==type('string'):
        return render_template('recommend.html',movie=movie,r=r,t='s')
    else:
        return render_template('recommend.html',movie=movie,r=r,t='l')



if __name__ == '__main__':
    app.run()
