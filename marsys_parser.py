import sys
from decisionTree import decisionTree

def parseVars(fstream):
    tempDict = {}
    count = 0
    tempArr = []
    for line in fstream:
        split = line.split(" ")
        if (count % 3 == 0):
            fileNameSplit = split[2].split("/")
            fName = fileNameSplit[len(fileNameSplit)-1]
        elif (count % 3 == 1):
            srate = split[2]
        else:
            values = line.split(",")
            for i in values:
                if (i != "music"):
                    tempArr.append(i)
            tempDict[fName] = tempArr
            tempArr = []
            fileName = []

        count += 1
    print (count)
    return tempDict

def scanData(tempInput, attrList):
    # fname = input("Enter Filename: ")
    marsysFile = open(tempInput, "r")
    print ("Opened: " + tempInput)
    tempAttr = {}

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
            tempAttr = parseVars(marsysFile)
            break

    marsysFile.close()
    return tempAttr

def main():
    fname = "MARSYAS_SINGLEfeatures.arff"
    attrNameList = []
    attrNameToValues = scanData(fname, attrNameList)

    print (attrNameList)
    for key, value in attrNameToValues.items() :
        print(key)

    decisionTree()


if __name__ == "__main__":
    main()
