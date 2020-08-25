#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 8.26.2015
#Version: 0.0.02
#Description: Organize and take notes with PyNotes!


#imports
import os
import time


#globals
files = []
CPaths = []
#cwd = os.getcwd()
#DoNotChange
ORIGINAL_CWD = os.getcwd()


#classes
class Data():
    FileName=None
    MainCwd = None
    cwd = None
    path = None
    cpaths = []
    cfiles = []
    text = ""

    def __init__(self):
        self.MainCwd = os.getcwd()
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)

    def UPL(self):
        self.cpaths = list()
        self.cfiles = list()
        cwd = self.cwd
        path = self.path
##        print("##########---FOLDERS---##########")
        for c in os.walk(path).__next__()[1]:
##            print(c)
            self.cpaths.append(c)
##        print("##########----FILES----##########")
        for c in os.walk(path).__next__()[2]:
##            print(c)
            self.cfiles.append(c)

    def ChangeDir(self, newpath=""):
        if len(str(newpath))==0:
            newpath = self.MainCwd
        os.chdir(newpath)
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)

    def ListPaths(self):
        self.UPL()
        print("##########---FOLDERS---##########")
        for c in self.cpaths:
            print(c)
        print("##########----FILES----##########")
        for c in self.cfiles:
            print(c)

    def __str__(self):
        return 'Main cwd: ' + str(self.MainCwd) + '\n' +\
               'Current cwd: ' + str(self.cwd) + '\n' +\
               'Current path: ' + str(self.path) + '\n'
               
        

    
        


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

def UPL():
    global CPaths
    CPaths = list()
    cwd = os.getcwd()
    path = os.path.join(cwd)
    print("##########---FOLDERS---##########")
    for c in os.walk(path).__next__()[1]:
        print(c)
        CPaths.append(c)
    print("##########----FILES----##########")
    for c in os.walk(path).__next__()[2]:
        print(c)
        CPaths.append(c)

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

def ListDir():
    UPL()

def MainDir():
    os.chdir(ORIGINAL_CWD)

def startUp():
    def titleDisplay():
        i = 0
        while i<10:
            print()
            i+=1
        print("""
        --------------------
        Welcome to PyNotes V0.0.02
        
        This program is used to take notes
        and save them to a simple text document
        
        Author: Max Ferney
        if you have any questions or concerns
        about this program, you may email
        me at maxferney@gmail.com please set
        the title of the subject to pygame, so
        I know what it is. Thank you.
        --------------------
        """)
        i = 0
        while i<8:
            print()
            i+=1
    titleDisplay()


startUp()


    
