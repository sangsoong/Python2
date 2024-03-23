import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://store.steampowered.com/"
response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")

titles = []
tags = []
prices = []
images = []

for i in range(0, 40):
    titles.append(soup.select(".tab_item_name")[i].text)
    tags.append(soup.select(".tab_item_top_tags")[i].text)
    prices.append(soup.select(".discount_final_price")[i].text)
    images.append(soup.select(".tab_item_cap_img")[i].attrs["src"])

df = pd.DataFrame(
    data=zip(titles, tags, prices, images),
    columns=("titles", "tags", "prices", "images"),
)

print(df)

df.to_csv("crawled_csv")