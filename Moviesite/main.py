import requests
import dotenv
import os

dotenv.load_dotenv()

movie = input("Enter a movie name: ")
enter_year = input("Enter a year(optional): ")

movie_params = {
    "apikey": os.getenv("API_KEY"),
    "t": movie,
    "y": enter_year,
}

responce = requests.get(url="http://www.omdbapi.com/", params=movie_params)
responce_json = responce.json()

movie_title = responce_json['Title']
movie_year = responce_json['Year']
movie_genre = responce_json['Genre']
imdb_rating = responce_json['imdbRating']
imdb_vote = responce_json['imdbVotes']

print(f"Movie title: {movie_title}")
print(f"Movie released year: {movie_year}")
print(f"Movie genre: {movie_genre}")
print(f"IMDB Rating: {imdb_rating}")
print(f"IMDB Vote: {imdb_vote}")


