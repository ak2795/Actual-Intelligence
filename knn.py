
import matplotlib
matplotlib.use('Agg')

from sklearn.neighbors import KNeighborsClassifier
from sklearn import manifold
import numpy as np
import json
from pprint import pprint
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

def kneighbors():
    for numTimes in range(1):
        print("Using: tests/features_labelsTrain" + str(numTimes) + ".json")
        with open('tests/features_labelsTrain' + str(numTimes) + '.json') as data_file:
            data = json.load(data_file)

        # using k = 30
        knn = KNeighborsClassifier(n_neighbors = 30)
        neigh = knn.fit(data[0], data[1])
        printKNN(data[0], data[1])

        return neigh

def printKNN(data_x, data_y):
    X = []
    Y = data_y

    n_neighbors = 30

    # get the first two feature for all training data
    for row in data_x:
        X.append(row[:2])

    h = .02 #step size in the mesh

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    for weights in ['uniform', 'distance']:

        knn = KNeighborsClassifier(n_neighbors, weights=weights)
        knn.fit(X, Y) # fit the data
        
        x_min, x_max = X[0][0], X[0][0]
        y_min, y_max = X[0][0], X[0][0]

        # Plot the decision boundary
        for row in X:
            if row[0] > x_max:
                x_max = row[0]
            if row[1] > y_max:
                y_max = row[1]
            if row[0] < x_min:
                x_min = row[0]
            if row[1] < y_min:
                y_min = row[1]

        x_max += .5
        x_min -= .5
        y_max += .5
        y_min -= .5

        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                            np.arange(y_min, y_max, h))
        Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy ,Z, cmap=cmap_light)

    plt.savefig('test.png')                 

def testKNN():
    for numTimes in range(10):
        knn = kneighbors()
        with open('tests/features_labelsTest' + str(numTimes) + '.json') as data_file:
            dataTest = json.load(data_file)

        count = 0
        total = 0
        tempPred = knn.predict(dataTest[0])
        answers = dataTest[1]

        for i in range(len(answers)):
            if (tempPred[i] == answers[i]):
                count += 1
            total += 1

        print("\tk-Nearest Neighbors: " + str(count) + " out of " + str(total))

def main():
    # testKNN()
    kneighbors()

if __name__ == "__main__":
    main()
