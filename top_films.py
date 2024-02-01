import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime


cur_year = datetime.utcnow().year
data = []
for year in range(2017, cur_year + 1):
    pages = requests.get(
        f'https://www.kinoafisha.info/rating/movies/{year}/'
    )
    soup = BeautifulSoup(
        pages.text,
        'html.parser'
    )
    
    time.sleep(1)
    
    all_films = soup.findAll(
        'a',
        class_='movieItem_title'
    )
    for film in all_films:
        text = film.text
        link = film.get('href')
        data.append([text, link, year])

header = (
    'film_name',
    'link',
    'year'
)
data_file = pd.DataFrame(
    data,
    columns=header
)
data_file.to_csv(
    'films.csv',
    sep=';',
    encoding='utf8'
)
