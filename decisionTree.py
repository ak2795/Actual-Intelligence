from sklearn import tree
import numpy
from pprint import pprint

def decisionTree():
    with open(features_labels.json) as data_file:
        data = json.load(data_file)

    pprint(data)
