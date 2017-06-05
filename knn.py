from sklearn.neighbors import KNeighborsClassifier
from sklearn import manifold
import numpy as np
import json
from pprint import pprint
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

    # get the first two feature for all training data
    for row in data_x:
        X.append(row[:2])

    h = .02 #step size in the mesh

    knn = KNeighborsClassifier()
    knn.fit(X, Y) # fit the data

    # Plot the decision boundary
    x_min, x_max = X[:,0].min() - 0.5, X[:,0].max() + 0.5

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
