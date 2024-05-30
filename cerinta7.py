import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_filename = 'train.csv'
df = pd.read_csv(csv_filename)

kids = 0
for num in df['Age']:
    if num < 18:
        kids += 1
        
kids = (kids / len(df['Age'])) * 100
print("Procentul copiilor aflati la bord este {}.".format(kids))

survivors = df[(df['Age'] < 18) & df['Age'].notnull()]['Survived'].mean() * 100
adults = df[(df['Age'] >= 18) & df['Age'].notnull()]['Survived'].mean() * 100

data = {'Kids':survivors, 'Adults':adults}
names = list(data.keys())
values = list(data.values())

plt.figure(figsize = (8, 5))
plt.bar(names, values, color = ["red", "blue"], width = 0.2)
plt.title("Survival rate")
plt.grid(axis='y')
plt.savefig('cerinta7.png')