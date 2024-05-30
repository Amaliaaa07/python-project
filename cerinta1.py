import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
csv_filename = 'train.csv'
with open(csv_filename, mode = 'r') as csv_file:
    reader = csv.reader(csv_file)
    headers = csv_file.readline().split(",")
    for row in reader:  #trecem prin toate linille fisierului
        pass
    
columns = len(headers)
lines_total = reader.line_num
print("Numarul de coloane este {0} si numarul de linii este {1}.".format(columns, lines_total))
print()
df = pd.read_csv(csv_filename)
tip = df.dtypes
print("Tipurile datelor din fiecare coloana sunt:\n{}".format(tip))
duplicate = df[df.duplicated()]
print()
if duplicate.empty:
    print("Nu exista linii duplicate.")
    print()
else:
    print("Exista {} linii duplicate.".format(duplicate))
    print()
val = df.isnull()
l = 0
for column in val:
    l = 0
    for element in val[column]:
        if element == True:
            l += 1
    print("Numarul de valori lipsa pentru coloana {0} este {1}.".format(column, l))


