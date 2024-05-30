import pandas as pd
import matplotlib.pyplot as plt

csv_filename = 'train.csv'
df = pd.read_csv(csv_filename)
val = df.isnull().sum()
val = val[val > 0]
proportion = val / len(df) * 100

print(val)
print(proportion)
miss = df.drop(columns=['Survived']).groupby(df['Survived']).apply(lambda group: group.isnull().sum() / len(group) * 100).transpose()

miss= miss[(miss.T != 0).any()]

print(miss)