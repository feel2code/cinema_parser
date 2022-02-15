import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

data = []
for year in range(2017, 2023):
    pages = requests.get(f'https://www.kinoafisha.info/rating/movies/{year}/')
    soup = BeautifulSoup(pages.text, 'html.parser')
    time.sleep(1)
    all_films = soup.findAll(
        'a',
        class_='movieItem_title'
    )
    for film in all_films:
        text = film.text
        link = film.get('href')
        data.append([text, link, year])

header = ('film_name', 'link', 'year')
df = pd.DataFrame(data, columns=header)
df.to_csv('/Users/felixmac/Desktop/films.csv', sep=';', encoding='utf8')
