import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import kagglehub

#Décommentez ces 2 lignes ci-dessous pour télécharger le jeu de données
#path = kagglehub.dataset_download("grouplens/movielens-20m-dataset")
#print("Path to dataset files:", path)

movies = pd.read_csv(
    "movie.csv",
    sep = ",",
    usecols=["movieId","title","genres"]
)

movies["genres"] = movies["genres"].apply(lambda x: x.replace("|"," ").replace("-", ""))

ratings = pd.read_csv(
    "rating.csv",
    sep = ",",
    usecols=["userId","movieId","rating"]
)
movie_rate_popular = ratings.groupby("movieId")["rating"].agg(["mean", "count"])
movie_rate_popular.columns = ["avg_rating", "rating_count"]
high_ratings = ratings[ratings["rating"] >= 4.0]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movies["genres"])
cos = cosine_similarity(tfidf_matrix)
cos_df = pd.DataFrame(cos, index = movies.movieId, columns=movies.movieId)

def recommendation(user, top = 5):
    user_ratings = ratings[ratings["userId"] == user]

    if len(user_ratings) == 0:
        listindex = movie_rate_popular.sort_values("rating_count", ascending=False)[:top].index
        top_popular = movies.set_index("movieId").loc[listindex]["title"].tolist()
        return top_popular
    
    max_rating = user_ratings["rating"].max()
    favorite_movie = user_ratings[user_ratings["rating"] == max_rating].iloc[0]["movieId"]

    other_users = high_ratings[high_ratings["movieId"] == favorite_movie]["userId"].unique()
    other_users = [u for u in other_users if u != user] 
    other_users = other_users[:50] 


    if len(other_users) == 0:
        top_movie = cos_df.loc[favorite_movie, :]
        top_recommendation = top_movie.sort_values(ascending=False)[1:top+1].index
        return movies.set_index("movieId").loc[top_recommendation, "title"].tolist()
    
    watched_movies = set(user_ratings["movieId"])
    movie_by_other = set()
    for u in other_users:
        user_fav_movies = high_ratings[high_ratings["userId"] == u]["movieId"]
        movie_by_other.update(user_fav_movies)

    possible_id = movie_by_other - watched_movies

    if len(possible_id) == 0:
        top_movie = cos_df.loc[favorite_movie, :]
        top_recommendation = top_movie.sort_values(ascending=False)[1:top+1].index
        return movies.set_index("movieId").loc[top_recommendation, "title"].tolist()
    
    cos_scores = cos_df.loc[favorite_movie, movies[movies["movieId"].isin(possible_id)].movieId]
    
    top_id = cos_scores.sort_values(ascending=False)[:top].index
    top_titles = movies.set_index("movieId").loc[top_id, "title"].tolist()
    
    return top_titles

