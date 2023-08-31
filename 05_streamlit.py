import sqlite3
import streamlit as st
import pandas as pd

#
con = sqlite3.connect("identifier.sqlite")

cur = con.cursor()

res = cur.execute("""
WITH tbl AS (select eventdate,
                    count(*) AS count
             from sales
             GROUP BY eventdate)

SELECT tbl.eventdate as eventdate, count, temp
from tbl
left join weather
on tbl.eventdate = weather.eventdate;
""")

data = res.fetchall()
df = pd.DataFrame(data)
df.columns = ['eventdate', 'count', 'temp']
df['count'] = df['count'] / 50

st.line_chart(df, x='eventdate', y=['count', 'temp'])
# python3 -m streamlit run 05_streamlit.py
