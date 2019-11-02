# Movie recommendation system

Today we're going to see how to go about implementing a movie recommendation system.

## Installing Requirements
simply run:
```
pip install -r requirements.txt
```

## Objective
Our main objective is, given a movie title, check our dataset and see the top 5 most similar movies.

Ok so let's see how I went about developing our content based recommendation system.

First, we are going to do a recommender based on similarity, so we need to define similarity.

There are a few text similarity methods but in this one we will use Cosine Similarity.

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

## The full story
You can read the full blog post that's more in depth [here](https://joao-maria-janeiro.github.io/movie-recommender.html)
