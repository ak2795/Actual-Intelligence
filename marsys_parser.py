import sys
from decisionTree import decisionTree
import json
from random import randint

def parseVars(fstream):
    attrArr = []
    count = 0
    tempArr = []
    labels = []
    for line in fstream:
        split = line.split(" ")
        if (count % 3 == 0):
            fileNameSplit = split[2].split("/")
            split_len = len(fileNameSplit)
            fName = fileNameSplit[split_len-1]
            genre = fileNameSplit[split_len-2]
            if genre == "blues":
                labels.append(0)
            elif genre == "classical":
                labels.append(1)
            elif genre == "country":
                labels.append(2)
            elif genre == "disco":
                labels.append(3)
            elif genre == "hiphop":
                labels.append(4)
            elif genre == "jazz":
                labels.append(5)
            elif genre == "metal":
                labels.append(6)
            elif genre == "pop":
                labels.append(7)
            elif genre == "reggae":
                labels.append(8)
            elif genre == "rock":
                labels.append(9)
            else:
                print("AHHHHHH")


        elif (count % 3 == 1):
            srate = split[2]
        else:
            values = line.split(",")
            # for i in values:
            #     if (i != "music"):
            #         tempArr.append(i)
            # print tempArr
            del values[-1]
            values = map(float, values)
            attrArr.append(values)

        count += 1
    # print (count)
    # print ("\nlabels:\n{}\n".format(labels))
    return (attrArr, labels)

def scanData(tempInput, attrList):
    # fname = input("Enter Filename: ")
    marsysFile = open(tempInput, "r")
    feat_labels = ()

    for line in marsysFile:
        split = line.split(" ")
        # This gets rid ot the first created by marsys line
        if (split[0] == "%"):
            print (split[1])
        # This gets rid of the relation line
        elif (split[0] == "@relation"):
            print()
        # This parses the attribute names and puts them into an array
        elif (split[0] == "@attribute" and split[1] != "output"):
            attrList.append(split[1])
        # detects that the rest is data and parses it and breaks out of loop
        elif (split[0] == "@data\n"):
            feat_labels = parseVars(marsysFile)
            break

    marsysFile.close()
    return feat_labels

def randTrainTestData(feat_labels):
    twoArr = []
    givenData = feat_labels[0]
    answerData = feat_labels[1]

    trainData = []
    trainDataAns = []
    testData = []
    testDataAns = []

    for i in range(10):
        numUsed = []
        loop = True
        while loop:
            randIndex = randint(0,99)
            if randIndex not in numUsed:
               numUsed.append(randIndex)
            if len(numUsed) == 10:
                loop = False
        for j in range(100):
           arrIndex = i*100 + j
           if j in numUsed:
               testData.append(givenData[arrIndex])
               testDataAns.append(answerData[arrIndex])
           else:
               trainData.append(givenData[arrIndex])
               trainDataAns.append(answerData[arrIndex])

    twoArr.append([trainData, trainDataAns])
    twoArr.append([testData, testDataAns])

    return twoArr

def main():
    fname = "MARSYAS_SINGLEfeatures.arff"
    attrNameList = []
    feat_labels = scanData(fname, attrNameList)

    testData = randTrainTestData(feat_labels)

    # split into training and test set

    # Creates 10 files with random chosen training and dataset
    # for each 100 songs genres 90 training and 10 testing
    # total of 900 training and 100 testing
    for i in range(10):
        testData = randTrainTestData(feat_labels)
        with open("tests/features_labelsTrain" + str(i) + ".json", "w") as outfile:
            json.dump(testData[0], outfile, indent=3)

        with open("tests/features_labelsTest" +str(i) + ".json", "w") as outfile:
            json.dump(testData[1], outfile, indent=3)

    # Call your function here to do the processing


if __name__ == "__main__":
    main()
