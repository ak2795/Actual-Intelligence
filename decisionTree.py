from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import json
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import os

def decisionTree():
    for numTimes in range(10):

        print("Using: tests/features_labelsTrain" + str(numTimes) + ".json")
        with open('tests/features_labelsTrain' + str(numTimes) + '.json') as data_file:
            data = json.load(data_file)

        # clf = tree.DecisionTreeClassifier()
        # clf = clf.fit(data[0], data[1])

        with open('tests/features_labelsTest' + str(numTimes) + '.json') as data_file:
            dataTest = json.load(data_file)


        model_string = ["Decision Tree",
                        "Random Forest"]

        mdls = (tree.DecisionTreeClassifier(),
                RandomForestClassifier(n_estimators=100)
                )
        models = list((clf.fit(data[0], data[1]) for clf in mdls))
        predicts = list(clfr.predict(dataTest[0]) for clfr in models)
        answers = dataTest[1]
        correct = [0, 0, 0]
        total = len(dataTest[1])

        for x in range(len(models)):
            for i in range(total):
                if predicts[x][i] == answers[i]:
                    correct[x] += 1

            print("\t" + model_string[x] + ": " + str(correct[x]) + " out of " + str(total))
        printGraphs(mdls, data, numTimes)


        # count = 0
        # total = 0
        #
        # tempPred = clf.predict(dataTest[0])
        # answers = dataTest[1]
        #
        # for i in range(len(answers)):
        #     if (tempPred[i] == answers[i]):
        #         count += 1
        #     total += 1
        #
        # print("\tDecision Tree: " + str(count) + " out of " + str(total))
        #
        # rtf = RandomForestClassifier(n_estimators=100)
        # rtf = rtf.fit(data[0], data[1])
        # tempPred = rtf.predict(dataTest[0])
        #
        # count = 0
        # total = 0
        # for i in range(len(answers)):
        #     if (tempPred[i] == answers[i]):
        #         count += 1
        #     total += 1
        #
        # print("\tRandom Forests: " + str(count) + " out of " + str(total))

def printGraphs(mdls, data, test_n):
   titles = ('Decision Tree',
             'Random Forest')

   X = []
   for d in data[0]:
      X.append(np.asarray([d[0], d[1]]))
   X = np.asarray(X)
   x_col = []
   y_col = []
   for x in X:
      x_col.append(x[0])
      y_col.append(x[1])
   Y = np.asarray(data[1])
   graph_models = list((clf.fit(X, Y) for clf in mdls))

   for clf, ttl in zip(graph_models, titles):
      plot_decision_regions(X=X, y=Y, clf=clf, legend=2)
      plt.xlabel(x_col)
      plt.ylabel(y_col)
      plt.title(ttl)
      filename = 'Docs/';
      if ttl == 'Decision Tree':
         filename += 'DecisionTree'
      else:
         filename += 'RandomForest'

      filename += '.png'

      plt.savefig(filename)




def main():
    decisionTree()

if __name__ == "__main__":
    main()

# 3jgqhxg
# http://whenisgood.net/3d39dyh/results/3jgqhxg
