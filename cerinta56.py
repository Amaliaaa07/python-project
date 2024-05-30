import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_filename = 'train.csv'
df = pd.read_csv(csv_filename)

age_categ = ['1', '2', '3', '4']
x = 0
y = 0
z = 0
t = 0

for num in df['Age']:
    if 0 <= num <= 20:
        x += 1
    elif 21 <= num <= 40:
        y += 1
    elif 41 <= num <= 60:
        z += 1
    elif num >= 61:
        t += 1

age_bins = [0, 20, 40, 60, np.inf]

df['AgeCategory'] = pd.cut(df['Age'], bins=age_bins, labels=age_categ, right=False)
df['AgeCategory'] = df['AgeCategory'].cat.add_categories('Unknown').fillna('Unknown')


survivors = df[df['Sex'] == 'male'].groupby('AgeCategory', observed=False)['Survived'].sum().sort_index()


total = df[df['Sex'] == 'male'].groupby('AgeCategory', observed=False).size().sort_index()

male = survivors / total * 100

for age_category, rate in male.items():
    print(f'{age_category} : {rate:.2f}%')
    
data = {'0-20':x, '21-40':y, '41-60':z , '61+':t}
names = list(data.keys())
values = list(data.values())

plt.figure(figsize = (7, 5))
plt.subplot(1, 2, 1)
plt.bar(names, values, color = ["red", "blue"], width = 0.4)
plt.title("Males ages - cerinta 5")
plt.grid(axis='y')
plt.savefig('cerinta5-6.png')


data = {'0-20':29.21, '21-40':18.82, '41-60':18.39, '61+':13.64}
names = list(data.keys())
values = list(data.values())


plt.subplot(1, 2, 2)
plt.bar(names, values, color = ["red", "blue"], width = 0.4)
plt.title("Survivors- cerinta 6")
plt.grid(axis='y')
plt.savefig('cerinta5-6.png')


print(x, y, z, t)
        