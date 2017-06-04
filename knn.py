from sklearn.neighbors import KNeighborsClassifier
from sklearn import manifold
import numpy as np
import json
from pprint import pprint
import matplotlib.pyplot as plt

def kneighbors():
    for numTimes in range(10):
        print("Using: tests/features_labelsTrain" + str(numTimes) + ".json")
        with open('tests/features_labelsTrain' + str(numTimes) + '.json') as data_file:
            data = json.load(data_file)

        # using k = 30
        knn = KNeighborsClassifier(n_neighbors = 30)
        neigh = knn.fit(data[0], data[1])

        return neigh

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
    testKNN()

if __name__ == "__main__":
    main()
