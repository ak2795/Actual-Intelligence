import sys
from decisionTree import decisionTree
import json

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
    # print attrArr[0:3]
    return (attrArr, labels)

def scanData(tempInput, attrList):
    # fname = input("Enter Filename: ")
    marsysFile = open(tempInput, "r")
    print ("Opened: " + tempInput)
    feat_labels = ()

    for line in marsysFile:
        split = line.split(" ")
        # This gets rid ot the first created by marsys line
        if (split[0] == "%"):
            print (split[1])
        # This gets rid of the relation line
        elif (split[0] == "@relation"):
            print ("RELATION")
        # This parses the attribute names and puts them into an array
        elif (split[0] == "@attribute" and split[1] != "output"):
            attrList.append(split[1])
        # detects that the rest is data and parses it and breaks out of loop
        elif (split[0] == "@data\n"):
            print ("HERE")
            feat_labels = parseVars(marsysFile)
            break

    marsysFile.close()
    return feat_labels

def main():
    fname = "MARSYAS_SINGLEfeatures.arff"
    attrNameList = []
    feat_labels = scanData(fname, attrNameList)

    print(feat_labels[1])
    with open("features_labels.json", 'w') as outfile:
        json.dump(feat_labels, outfile, indent=3)
    # print (attrNameList)
    # for key, value in attrNameToValues.items():
    #     print(value)

    decisionTree()


if __name__ == "__main__":
    main()
