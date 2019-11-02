# Movie recommendation system

Today we're going to see how to go about implementing a movie recommendation system.

## Installing Requirements
simply run:
```
pip install -r requirements.txt
```

## Objective
Our main objective is, given a movie title, check our dataset and see the top 5 most similar movies.

This similarity can be of various types, it could be rating similarity, content similarity or even collaborative filtering.

#### Rating similarity
This is a rating or popularity based recommendation, based on views, likes, comments, ratings, reviews etc... This is what you get when you go to the trends.

#### Content similarity
This is what we are going to build today. So this similarity is based on the plot, title, cast, genre, etc... The movie's content. So we give it a movie title as input and based on it's content it will try to match it with the most similar to it, by ranking them.

#### Collaborative filtering
This is when you have two users, user A and user B, and both watched a movie, so you recommend user A some movies that user B has watched and vice versa.
![](https://i0.wp.com/datameetsmedia.com/wp-content/uploads/2018/05/2ebah6c.png?resize=1024%2C627)

Ok so let's see how to go about developing our content based recommendation system.

First, we are going to do a recommender based on similarity, so we need to define similarity.

There are a few text similarity methods but we'll look at the most common, Jaccard Similarity and Cosine Similarity.

##### Jacard Similarity
Jacard similarity is defined as the size of the intersection over size of the union of both sets.
Example(taken from towardsdatascience):
Sentence 1: AI is our friend and it has been friendly
Sentence 2: AI and humans have always been friendly

In order to calculate the similarity using the Jacard method, first we perform lemmeatization to get all to the words to their root word. Like "friend" and "friendly" will both become "friend".
Let's look at the Venn diagram(taken from towardsdatascience):
![](https://miro.medium.com/max/602/1*u2ZZPh5er5YbmOg7k-s0-A.png)

So for this internsection we get a Jaccard Similarity of 5/(5+3+2) = 0.5, which is the intersection size of the total amount of words.

##### Cosine Similarity
Cosine Similarity is calculated by measuring the cosine of angle between two vectors. This is calculated with:
![](https://miro.medium.com/max/554/1*hub04IikybZIBkSEcEOtGA.png)

You might be wondering of to convert a sentence to a vector. One way is to use a bag of words with either TF (term frequency) or TF-IDF (term frequency - inverse document frequency). Another way is Word2Vec.

Let’s calculate cosine similarity for these two sentences:
Sentence 1: AI is our friend and it has been friendly
Sentence 2: AI and humans have always been friendly

**First**, we get the Term Frequeccy using a bag of words:

| Sentence | AI | IS | FRIEND | HUMAN | ALWAYS | AND | BEEN | OUR | IT | HAS |
|----------|:---|:---|:-------|-------|--------|-----|------|-----|----|----:|
| Sentece 1| 1 | 1 | 2 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| Sentece 2| 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

**Second**, knowing that the main issue with term frequency vounts is that it favours the longer sentences. In order to solve this we must normalize the frequencies, with the respective magnitudes. Summing up squares of each frequency and taking a square root.

**Third**, as we already have the nomralized the two vectors to have a length of 1 we can calculate the cosine similarity by using the dot product.

##### Differences between methods
* Jaccard similarity takes only unique set of words for each sentence while cosine similarity takes total length of the vectors.
* Jaccard similarity is good for cases where duplication does not matter, cosine similarity is good for cases where duplication matters while analyzing text similarity.

We will use cosine similarity.

## The dataset
Looking online I found two viable options:

[3269 movies](https://raw.githubusercontent.com/codeheroku/Introduction-to-Machine-Learning/master/Building%20a%20Movie%20Recommendation%20Engine/movie_dataset.csv)

[5042 movies](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)

I tried both of them and got similar results, though the keywords are not exactly the same for all movies in both datasets I found that the second dataset had more movies and also it also had better results, usually.

## The end result
We can't actually see how good our results are but let's do some quick comparisons to the results Google will give you.

If we search for, let's say, the movie Shutter Island we get:
* The Sixth Sense 
* The Departed 
* Inception 
* The Wolf of Wall Street 
* The Aviator 
* Gangs of New York 

Google will give you:
* Gone Baby Gone
* Hugo
* Zodiac
* Mystic River
* A Cure for Wellness
* Maniac
* In the Cut
* The Silence of the Lambs
* The Departed
* One flew Over the Curf
* Inception
* Wolf of Wall Street
* The Revenant
* Gone Girl
* Catch Me if You Can
* Gangs of New Yotk
* The Aviator
* Django Unchained
* The Prestige

We can say our resuts are not too bad considering our dataset is quite small.

The results for a lot of movies are quite bad if we compare it to Google's suggestions. Central Intelligence for instance has none of the 5 our program gives.

## What could be better
So the results are not bad but could be improved, but how?
First they'd be much better if the dataset was bigger and there were more movies to choose from. We split the words and compare them but some coupling of words should be compared as pairs or tripplets, like the actors names for instance, if we see Leonardo DiCaprio we will match it to other Leonardos and other DiCaprios, this is not a very common first or last name but with some other names that are more common this is an issue.

We could also do a different approach using Neural Networks that might find some different relations between the movies.

It's also worth considering looking into collaborative filtering, although a different dataset would be needed for that.
