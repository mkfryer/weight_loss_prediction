from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv
from scipy import stats
import numpy as np

#normalize data
def normalize(list):
    l = list.copy()
    ma = max(l)
    mi = min(l)
    for i in range(len(l)):
        l[i] = (l[i] - mi)/(ma - mi)
    return l

def remove_outliers(list, thr, ave):
    l = list.copy()
    for i in range(len(l)):
        if l[i] >= thr:
            l[i] = ave
    return l

def plot_vit_a_corr():
    #vit a is idx 14
    #fiber idx 11
    dates = []
    days = []
    weight = []
    vit_A = []

    with open('nutrition_summary_day_average.csv', newline='') as csvfile:
        A_m = .02
        csvReader = csv.reader(csvfile)
        for i, row in enumerate(csvReader):
            if i == 0:
                continue
            days.append(i)
            dates.append(row[0][5:])
            weight.append(float(row[-2]))
            vit_A.append(float(row[14]))

    
    
    weight = np.array(normalize(weight))
    vit_A = remove_outliers(vit_A, 30, 30)
    vit_A = np.array(normalize(vit_A))
    print(vit_A)
    date = np.array(dates)
    days = np.array(days)

    # Generated linear fit weight
    mask = np.where(weight > .3)
    slope, intercept, r_value, p_value, std_err = stats.linregress(days[mask], weight[mask])
    line = slope*days+intercept
    plt.plot(dates, line, label="weight")
    # plt.plot(dates, weight)
    plt.scatter(dates, weight)

    mask = np.where(vit_A < .8)
    slope, intercept, r_value, p_value, std_err = stats.linregress(days[mask], vit_A[mask])
    line = slope*days+intercept

    plt.plot(dates, line, label="vit-A")
    # plt.plot(dates, vit_A)
    plt.scatter(dates, vit_A)
    ax = plt.gca()
    fig = plt.gcf()
    fig.autofmt_xdate()
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("y")
    plt.show()

plot_vit_a_corr()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# print(date, vit_A, weight)
# ax.scatter(date, vit_A, weight, c='r', marker='o')

# ax.set_xlabel('time')
# ax.set_ylabel('fiber')
# ax.set_zlabel('weight')
# plt.scatter(date, weight, label="weight")
# plt.scatter(date, vit_A, label="vit-a")
# plt.legend()
# plt.show()