from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import json
import numpy
from pprint import pprint
from sklearn.neural_network import MLPClassifier
from IPython.display import Image
import pydotplus

def decisionTree():
    for numTimes in range(10):

        print("Using: tests/features_labelsTrain" + str(numTimes) + ".json")
        with open('tests/features_labelsTrain' + str(numTimes) + '.json') as data_file:
            data = json.load(data_file)

        # Decision Trees
        clf = tree.DecisionTreeClassifier(criterion="entropy", max_leaf_nodes=10)
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

        import pydotplus
        dot_data = tree.export_graphviz(clf, out_file=None)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_pdf("decTree.pdf")

        # Random Forests
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

        # Neural Networks Classifiers
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                hidden_layer_sizes=(5, 2), random_state=1)

        clf.fit(data[0], data[1])
        MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
               beta_1=0.9, beta_2=0.999, early_stopping=False,
               epsilon=1e-08, hidden_layer_sizes=(15,), learning_rate='constant',
               learning_rate_init=0.50, max_iter=500, momentum=0.9,
               nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
               solver='lbfgs', tol=0.5, validation_fraction=0.5, verbose=False,
               warm_start=False)

        tempPred = clf.predict(dataTest[0])
        count = 0
        total = 0
        for i in range(len(answers)):
            if (tempPred[i] == answers[i]):
                count += 1
            total += 1

        print("\tMLP Neural Network: " + str(count) + " out of " + str(total))


def main():
    decisionTree()

if __name__ == "__main__":
    main()

# 3jgqhxg
# http://whenisgood.net/3d39dyh/results/3jgqhxg
