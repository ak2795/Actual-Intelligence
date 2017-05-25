from sklearn import svm
import json
import numpy as np
from pprint import pprint 

def svm_func():
   for nt in range(10):
      print("Using: tests/features_labelsTrain" + str(nt) + ".json")
      with open('tests/features_labelsTrain' + str(nt) + '.json') as data_file:
         data = json.load(data_file)
      
      clfr = svm.LinearSVC()
      clfr.fit(data[0], data[1])
      
      with open('tests/features_labelsTest' + str(nt) + '.json') as data_file:
         data_test = json.load(data_file)

      predicts = clfr.predict(data_test[0])
      answers = data_test[1]
      correct = 0      
      total = len(data_test[1])
      
      for i in range(total):
         if predicts[i] == answers[i]:
            correct += 1
      
      print("\tSVM.LinearSVC: " + str(correct) + " out of " + str(total)) 
      
      #for i in range(len(data)):
      #   for j  in range(len(data[i])):
      #      print(data[i][j])
         
def main():
   #print("Hello world")
   svm_func()

if __name__ == "__main__":
   main()   
