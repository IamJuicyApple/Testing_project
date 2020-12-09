import os
# Functions for checking if a file
                            # Exists
                            # read from a file
                            # write to a file
def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filePath, textToWrite):
    fileHandle = open(filePath , "w")
    fileHandle.write(textToWrite)
    fileHandle.close()

def readFile(filePath):
    if not fileExists(filePath):
        print("The file "+ filePath + " does not exist - cannot read it.")
        return ""
    fileHandle = open(filePath , "r")
    data = fileHandle.read()
    fileHandle.close()
    return data


# writing and reading a line at a time

def openFileForWriting(filePath):
    fileHandle = open(filePath , "w")
    return fileHandle

def writeALine(fileHandle , lineToWrite):
    lineToWrite = lineToWrite + "\n"
    fileHandle.write(lineToWrite)

def openFileForReading(filePath):
    if not fileExists(filePath):
        print("The file "+filePath+" does not exists - cannot read it.")
        return ""
    fileHandle = open(filePath,"r")
    return fileHandle
  
def readALine(fileHandle):
    theLine = fileHandle.readline()
    if not theLine:
        return False
    if theLine.endswith("\n"):
        theLine = theLine.rstrip("\n")
    return theLine

def closeFile(fileHandle):
    fileHandle.close()

f=openFileForReading("ID_name.txt")
##x = readALine(f)
##split_list= x.split("|")
##print(split_list[1])
##
##read_list = f.readlines()
##list_append = []
##
##
##for elements in read_list:
##    aList = elements.strip("\n").split("|")
##    list_append.extend(aList)
##for i in range(0,len(list_append),2):
##    if ID == list_append[i]:
##        print(list_append[i+1])
##print(list_append)
##    
##with open("ID_name.txt","r")as data:
##    print(data.readlines())
ID = "2002224"
with open("User_Calculator.txt","a+") as f:
    IDStr = ID + "\n"
    f.write(IDStr)
