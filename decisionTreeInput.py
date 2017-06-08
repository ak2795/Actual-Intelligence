from marsys_parser import *
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import json
import numpy
from pprint import pprint

def getMusicType(num):
    if num == 0:
        print("blues")
    elif num == 1:
        print("classical")
    elif num == 2:
        print("country")
    elif num == 3:
        print("disco")
    elif num == 4:
        print("hiphop")
    elif num == 5:
        print("jazz")
    elif num == 6:
        print("metal")
    elif num == 7:
        print("pop")
    elif num == 8:
        print("reggae")
    elif num == 9:
        print("rock")

def decisionTreeParser(fname):
    attrNameList = []

    with open(fname) as data_file:
        feat_labels = json.load(data_file)

    with open('tests/features_labelsTrain' + str(7) + '.json') as data_file:
        data = json.load(data_file)

    print("Decision Trees: ")
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(data[0], data[1])

    tempPred = clf.predict(feat_labels)
    print("Song Predicted: ")
    getMusicType(tempPred[0])

    print("Random Forests: ")
    rtf = RandomForestClassifier(n_estimators=200)
    rtf = rtf.fit(data[0], data[1])

    tempPred = rtf.predict(feat_labels)
    print("Song Predicted: ")
    getMusicType(tempPred[0])


def main():
    fileName = raw_input("Enter fileName: ")
    decisionTreeParser(fileName)

if __name__ == "__main__":
    main()
