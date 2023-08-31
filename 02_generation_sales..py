import random
import pandas as pd

data = pd.read_csv("weather.csv")
data.columns = ['eventdate', "weather"]

result = []
types = ["Бежецкий пломбир", "Эскимо Волга", "Стаканчик в шок", "Фруктовый лед"]
for line in data.to_records():
    for i in range(4):
        #for j in range(
        for j in range(150 + random.randint(0, int(100 * line[2] / 25))):
            a = random.randint(0, 3)
            result.append((line[1], i, a))

df = pd.DataFrame.from_records(result)
df.to_csv("sales.csv", index=False)