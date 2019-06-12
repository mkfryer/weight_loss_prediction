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

    mask = [1, 5, 10, 7, 11, 14, 18]
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
    # train_data = data[:t, :]
    # test_data = data[t:, :]
    # train_data = np.vstack((data[:23, :], data[31:, :]))
    # test_data = data[23:30]

    folds = [
            [data[15:, :], data[:15, :]], 
            [np.vstack((data[:15, :], data[30:, :])), data[15:30, :]], 
            [np.vstack((data[:30, :], data[40:, :])), data[30:40, :]], 
            [data[:40, :], data[40:51, :]]
            ]
    intervals = [
        [0, 15],
        [15, 30],
        [30, 40],
        [40, 52]
    ]
    # c = 0
    # for i in range(0, m-t):
    #     print(clf.predict([test_data[i, :-1]])[0], test_data[i, -1])

    #     if clf.predict([test_data[i, :-1]])[0] == test_data[i, -1]:
    #         c += 1
    # print("accuracy :", c/7)
    
    # dot_data = tree.export_graphviz(clf, out_file=None) 
    # graph = graphviz.Source(dot_data) 
    # dot_data = tree.export_graphviz(clf, out_file=None, 
    #                       feature_names=iris.feature_names,  
    #                       class_names=iris.target_names,  
    #                       filled=True, rounded=True,  
    #                       special_characters=True)  
    # graph = graphviz.Source(dot_data)  

    Y_hat = []
    for i, fold in enumerate(folds):
        X = range(intervals[i][0], intervals[i][1])
        train_data, testing_data = fold
        clf = tree.DecisionTreeRegressor()
        clf = clf.fit(train_data[:, :-1], train_data[:, -1])
        for i in X:
            print(i)
            Y_hat.append(clf.predict([data[i, :-1]])[0])
            print(Y_hat)
        # Y = [clf.predict([data[i, :-1]])[0] for i in X]
    X = range(0, m)
    print(m, len(Y_hat))
    plt.plot(X, Y_hat, label = "prediction", )
    plt.plot(X, data[:, -1], label = "true")
    plt.legend()
    plt.plot()
    plt.show()

predict()