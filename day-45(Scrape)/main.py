from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
all_movies = soup.find_all(name='h3', class_='title')
all_movies_name = [movie.text for movie in all_movies]
all_movies_name.reverse()

with open('movies.txt', 'w', encoding='UTF-8') as file:
    for movie in all_movies_name:
        file.write(f"{movie} \n")
