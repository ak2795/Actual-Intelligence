from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import json

with open("features_labels.json") as data_file:
    data = json.load(data_file)

features = data[0]
labels = data[1]


clf = AdaBoostClassifier(base_estimator=RandomForestClassifier(max_depth=2), n_estimators=1000, learning_rate=.8, random_state=1, algorithm="SAMME")
scores = cross_val_score(clf, features, labels, cv = 5)
print "\nAdaBoosted Random Forest: \n{}\n{}".format(scores, scores.mean())

clf = RandomForestClassifier(n_estimators = 100)
scores = cross_val_score(clf, features, labels, cv = 5)
print "\nRandom Forest: \n{}\n{}".format(scores, scores.mean())

clf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=2), n_estimators=1000, learning_rate=.8, random_state=1, algorithm="SAMME")
scores = cross_val_score(clf, features, labels, cv = 5)
print "\nAdaBoosted Decision Tree: \n{}\n{}".format(scores, scores.mean())

clf = DecisionTreeClassifier()
scores = cross_val_score(clf, features, labels, cv = 5)
print "\nDecision Tree: \n{}\n{}".format(scores, scores.mean())