#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 8.19.2015
#Version: 0.0.01
#Description: Organize and take notes with PyNotes!


#imports
import os
import time


#globals
files = []



#functions
def UFL(folder="Files\\"):
    global files
    files = list()
    cwd = os.getcwd()
    path = os.path.join(cwd, folder)
    #print("------------FILES------------")
    for c in os.walk(path).__next__()[2]:
        #print(c)
        files.append(c)

def OpenFile(fileName, directoryPath="Files/"):
    fileName = directoryPath+fileName
    with open(fileName, 'r') as f:
        text=f.read()
    f.close()
    return text

def NewFile(fileName, directoryPath="Files/"):
    dirPath=directoryPath + fileName + ".txt"
    with open(dirPath, 'w') as f:
        f.write('[FILE: ' + fileName + ']')
    f.close()

def AllFiles():
    UFL()
    print("------------FILES------------")
    for f in files:
        print(str(f))

def EditFile(fileName):
    pass
    
