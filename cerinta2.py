import pandas as pd
import matplotlib.pyplot as plt

csv_filename = 'train.csv'
df = pd.read_csv(csv_filename)

survivors = 0
not_survivors = 0
for i in df['Survived']:
    if i == 1:
        survivors += 1
    else:
        not_survivors += 1

sum = survivors + not_survivors
rez = survivors * 100 / sum

print("Procentul persoanelor care au supravietuit este {0}% iar procentul celor care nu au supravietuit este {1}%".format(rez, 100-rez))

clasa = df['Pclass'].value_counts(normalize=True) * 100
gen = df['Sex'].value_counts(normalize=True) * 100

print("Procentul pasagerilor pentru fiecare clasa:")
print("Clasa 1:{}%".format(clasa[1]))
print("Clasa 2: {}%".format(clasa[2]))
print("Clasa 3:{}%".format(clasa[3]))

print("Procentul barbatilor este {0}% și al femeilor este {1}%.".format(gen['male'], gen['female']))

data = {'Survivors':rez, 'Non-Survivors':100-rez}
names = list(data.keys())
values = list(data.values())

plt.figure(figsize = (10, 5))
plt.subplot(1, 3, 1)
plt.bar(names, values, color = ["red", "blue"], width = 0.2)
plt.title("Survival")
plt.grid(axis='y')
plt.savefig('cerinta2.png')

data = {'Clasa 1':clasa[1], 'Clasa 2':clasa[2], 'Clasa 3':clasa[3]}
names = list(data.keys())
values = list(data.values())

plt.subplot(1, 3, 2)
plt.bar(names, values, color = ["hotpink", "purple", "black"], width = 0.2)
plt.title("Class percentage")
plt.grid(axis='y')
plt.savefig('cerinta2.png')

data = {'Males':gen['male'], 'Females':gen['female']}
names = list(data.keys())
values = list(data.values())

plt.subplot(1, 3, 3)
plt.bar(names, values, color = ["green", "yellow"], width = 0.2)
plt.title("Gender percentage")
plt.grid(axis='y')
plt.savefig('cerinta2.png')