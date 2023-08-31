from datetime import date, timedelta
from bs4 import BeautifulSoup
import pandas as pd

with open("погода_август.html", 'r', encoding="utf-8") as f:
    text = f.read()

soup = BeautifulSoup(text, "html.parser")

weather = soup.findAll('tr', align='center')

today = date.today() - timedelta(days=29)
result = dict()
for el in weather:
    i = el.findNext("td", class_="first").text

    result[today + timedelta(int(i) - 1) ] = int(el.findNext("td", class_="first_in_group positive").text)

df = pd.DataFrame.from_dict(result, orient='index', )

df.to_csv("weather.csv")
