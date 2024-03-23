import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.freecodecamp.org/korean/news"
response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")

indexs = []
titles = []
authors = []
images = []
links = []

for i in range(0, 25):
    indexs.append(i)
    titles.append(soup.select(".post-card-title")[i].text.replace('\n', '').strip())
    authors.append(soup.select(".author-list")[i].text.replace('\n', '').replace('Translator:', '').strip())
    images.append(soup.select(".post-card-image")[i].attrs["src"])
    links.append(soup.select(".post-card-content-link")[i].text.replace('\n', '').strip()[20:].strip())

df = pd.DataFrame(
    data=zip(indexs, titles, authors, images, links),
    columns=["indexs", "titles", "authors", "images", "links"],
)

print(df)

df.to_csv("crawled_csv")