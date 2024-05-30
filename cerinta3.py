import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_filename = 'train.csv'
df = pd.read_csv(csv_filename)


file = df._get_numeric_data()
num = file.columns

i = 0
for column in num:
    i += 1
    plt.figure(figsize=(12, 5))
    plt.hist(file[column].dropna(), bins=15, edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    path = f'{column}-histogram.png'
    plt.savefig(path)