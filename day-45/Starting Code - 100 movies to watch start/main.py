import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")
gelasha = soup.find_all(name="h3", class_="title")
gelasha.reverse()
with open("movies.txt", "a") as file:
    for names in gelasha:
        print(names.get_text())
        file.write(names.get_text() + "\n")
