from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

date = []
weight = []
vit_A = []

#vit a is idx 14
#fiber idx 11

with open('nutrition_summary_day_average.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile)
    for i, row in enumerate(csvReader):
        if i == 0:
            continue
        date.append(i)
        weight.append(float(row[-1]))
        vit_A.append(float(row[14]))



print(date, vit_A, weight)
ax.scatter(date, vit_A, weight, c='r', marker='o')

ax.set_xlabel('time')
ax.set_ylabel('fiber')
ax.set_zlabel('weight')

plt.show()