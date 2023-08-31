import sqlite3
from yaweather import YaWeather
from config import secret
from datetime import date

y = YaWeather(api_key=secret)
res = y.forecast_raw(coordinates=(56.5128, 35.5518))
today = date.today()

con = sqlite3.connect("identifier.sqlite")

cur = con.cursor()

cur.execute(f"""
INSERT INTO  weather VALUES  ('{today}', {res['fact']['temp']})
            """)
con.commit()
