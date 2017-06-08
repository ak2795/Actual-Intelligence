from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import json
import numpy
from pprint import pprint

def decisionTree():
    for numTimes in range(10):

        print("Using: tests/features_labelsTrain" + str(numTimes) + ".json")
        with open('tests/features_labelsTrain' + str(numTimes) + '.json') as data_file:
            data = json.load(data_file)

        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(data[0], data[1])

        with open('tests/features_labelsTest' + str(numTimes) + '.json') as data_file:
            dataTest = json.load(data_file)

        count = 0
        total = 0
        tempPred = clf.predict(dataTest[0])
        answers = dataTest[1]

        for i in range(len(answers)):
            if (tempPred[i] == answers[i]):
                count += 1
            total += 1

        print("\tDecision Tree: " + str(count) + " out of " + str(total))

        rtf = RandomForestClassifier(n_estimators=100)
        rtf = rtf.fit(data[0], data[1])
        tempPred = rtf.predict(dataTest[0])

        count = 0
        total = 0
        for i in range(len(answers)):
            if (tempPred[i] == answers[i]):
                count += 1
            total += 1

        print("\tRandom Forests: " + str(count) + " out of " + str(total))



def main():
    decisionTree()

if __name__ == "__main__":
    main()

# 3jgqhxg
# http://whenisgood.net/3d39dyh/results/3jgqhxg
