print(__doc__)

from sklearn import svm
import json
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import os

def svm_func():
   for nt in range(10):
      print("Using: tests/features_labelsTrain" + str(nt) + ".json")
      with open('tests/features_labelsTrain' + str(nt) + '.json') as data_file:
         data = json.load(data_file)
      
      with open('tests/features_labelsTest' + str(nt) + '.json') as data_file:
         data_test = json.load(data_file)
     
      model_string = ["LinearSVC                            ", 
                      "SVC with RBF Kernel                  ", 
                      "SVC with polynomial (degree 3) kernel"]

      C = 1.0
      mdls = (
             svm.LinearSVC(C=C),
             svm.SVC(kernel='rbf', gamma=0.7, C=C),
             svm.SVC(kernel='poly', degree=3, C=C)
             )
      models = list((clf.fit(data[0], data[1]) for clf in mdls))
      
      predicts = list(clfr.predict(data_test[0]) for clfr in models)
      answers = data_test[1]
      correct = [0,0,0]      
      total = len(data_test[1])
      
      for x in range(len(models)):
         for i in range(total):
            if predicts[x][i] == answers[i]:
               correct[x] += 1
         
         print("\t" + model_string[x] + ": " + str(correct[x]) + " out of " + str(total)) 
      
      #svm_graphs(mdls, data, nt)

def svm_graphs(mdls,data, test_n):
   titles = ('LinearSVC (linear kernel)',
             'SVC with RBF kernel',
             'SVC with polynomial (degree 3) kernel')

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
      filename = 'SvmGraphsTest/Data' + str(test_n);
      if ttl == 'LinearSVC (linear kernel)':
         filename += 'LinearSvc'
      elif ttl == 'SVC with RBF kernel':
         filename += 'SvcRbf'
      else:
         filename += 'SvcPoly'
      filename += '.png'
      plt.savefig(filename)

def svm_test(test_file):
   if (os.path.isfile(test_file)):
      with open(test_file) as data_file:
         data_test = json.load(data_file)
   
      nt = 2
      print("Using: tests/features_labelsTrain" + str(nt) + ".json to train")
      with open('tests/features_labelsTrain' + str(nt) + '.json') as data_file:
         data = json.load(data_file)
         
      C = 1   
      clf = svm.SVC(kernel='poly', degree=3, C=C)
      clf.fit(data[0], data[1])
      
      predicts = clf.predict(data_test[0])
      answers = data_test[1]
      correct = 0
      total = len(data_test[1])
      
      for i in range(total):
         if predicts[i] == answers[i]:
            correct += 1
      
      print("\tSVC with polynomial (degree 3) kernel" + ": " + str(correct) + " out of " + str(total)) 
   else:
      print("Test File: " + test_file + " doesn't exist")
      
def main():
  #svm_func()
  
  svm_test(raw_input("File to test: "))
  
if __name__ == "__main__":
   main()   
