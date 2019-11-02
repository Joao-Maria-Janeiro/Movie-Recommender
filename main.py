import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("test.csv",  engine='python', encoding='utf8', error_bad_lines=False)

features = ['plot_keywords', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'genres', 'director_name']

def combine_features(row):
    return row['plot_keywords']+' '+ row['actor_1_name'] + ' ' + row['actor_2_name'] + ' ' + row['actor_3_name'] +' '+row['genres']+' '+row['director_name']

for feature in features:
    df[feature] = df[feature].fillna('')

df["combined_features"] = df.apply(combine_features,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in “combined_features” column

cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["movie_title"].values[0]

def get_index_from_title(title):
    title = title.rstrip() + "\xa0"
    return df[df.movie_title == title]["index"].values[0]


user_movie = input("Give me a movie title: ")
movie_index = get_index_from_title(user_movie)
similar_movies = list(enumerate(cosine_sim[movie_index])) #accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it

sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

i=0
print("The best recommendations for "+user_movie+" are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>5:
        break