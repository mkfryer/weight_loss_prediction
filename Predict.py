from sklearn import tree
from sklearn.utils import shuffle
import csv
import numpy as np
import matplotlib.pyplot as plt
import graphviz 

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

def load(file, col_mask):
    data = []
    with open(file, newline='') as csvfile:
        csvReader = csv.reader(csvfile)
        for i, row in enumerate(csvReader):
            if i == 0:
                continue
            data.append(np.array(row)[col_mask])
        return np.array(data)

"""
INDEX KEY
0 date
1 Calories
2 Fat
3 Saturated Fat
4 Polyunsaturated Fat
5 Monounsaturated Fat
6 Trans Fat
7 Cholesterol
8 Sodium 
9 Potassium
10 Carbohydrates
11 Fiber
12 Sugar
13 Protein
14 Vitamin A
15 Vitamin C
16 Calcium
17 Iron
18 weight
19 lost weight
"""
def predict():

    mask = [5, 10, 7, 11, 14, 18]
    data = load("data/nutrition_summary_day_average.csv", mask).astype(float)
    # data[0, -1] += "Yes"
    # mask1 = np.where(data[:, -1] == "Yes")
    # mask2 = np.where(data[:, -1] == "No")
    # data[mask1, -1] = 1
    # data[mask2, -1] = 0
    # print(data)
    # data = data.astype(float)

    m, n = data.shape
    t = int(.8 * m)
    train_data = data[:t, :]
    test_data = data[t:, :]
    # train_data = np.vstack((data[:22, :], data[31:, :]))
    # test_data = data[22:31]
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(train_data[:, :-1], train_data[:, -1])

    X = range(0, m)
    Y = [clf.predict([data[i, :-1]])[0] for i in X]

    loss_prediction = []
    gain_prediction = []
    # for i in range(len(Y) - 1):
    #     if 


    plt.plot(X, Y, label = "prediction")
    plt.plot(X, data[:, -1], label = "true")
    plt.legend()
    plt.xlabel("Days")
    plt.ylabel("Y")
    plt.title("Trend Prediction")
    plt.plot()
    plt.show()

predict()