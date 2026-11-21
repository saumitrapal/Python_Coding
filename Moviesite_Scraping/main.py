import requests
from bs4 import BeautifulSoup

URL = "https://time.com/collections/100-best-movies/"

responce = requests.get(url=URL)
website_html = responce.text
# print(responce.json)

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="p", class_="mb-1 font-graphik text-mobile-t1 duration-300 lg:text-t1")
all_movies_list = [movie.getText() for movie in all_movies]

with open(file="movie.txt", mode="a") as movie_file:
    for movie in all_movies_list:
        movie_file.write(f"{all_movies_list.index(movie) + 1}: {movie}\n")
