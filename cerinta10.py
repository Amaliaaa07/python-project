import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_filename = 'train.csv'
df = pd.read_csv(csv_filename)

df['Single'] = (df['SibSp'] == 0) & (df['Parch'] == 0)

people = df.head(100)
plt.figure(figsize = (8, 4))
sns.histplot(data = df, x = 'Single', hue = 'Survived')
sns.catplot(x = 'Pclass', y = 'Fare', hue = 'Survived', data = people, kind = 'swarm', height = 5)
plt.savefig('cerinta10.png')
