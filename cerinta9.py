import pandas as pd
import matplotlib.pyplot as plt

csv_filename = 'train.csv'
df = pd.read_csv(csv_filename)
df['Title'] = df['Name'].str.extract('([A-Za-z]+)\.')

titles = df['Title'].value_counts()

names = {
    'Mr': 'male',
    'Miss': 'female',
    'Mrs': 'female',
    'Master': 'male',
    'Ms': 'female',
    'Lady': 'female',
    'Dr': 'unknown',  
    'Rev': 'male',
    'Col': 'male',
    'Mlle': 'female',
    'Major': 'male',
    'Don': 'male',
    'Mme': 'female',
    'Capt': 'male',
    'Sir': 'male',
    'Dona': 'female',
    'Countess': 'female',
    'Jonkheer': 'male'
}

df['Real Gender'] = df['Title'].map(names)


df['Match'] = (df['Real Gender'] == df['Sex']) | (df['Real Gender'] == 'both')


gender = df[df['Match']].groupby('Title').size()


plt.figure(figsize = (13, 5))
plt.bar(titles.index, titles.values, color = ["hotpink", "purple"], width = 0.2)
plt.title("Titles correspondence")
plt.grid(axis='y')
plt.savefig('cerinta9-1.png')


plt.figure(figsize = (13, 5))
plt.bar(gender.index, gender.values, color = ["hotpink", "purple"], width = 0.2)
plt.title("Real gender match")
plt.grid(axis='y')
plt.savefig('cerinta9-2.png')

