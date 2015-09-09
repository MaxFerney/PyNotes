#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 9.02.2015
#Version: 0.1.00
#Description: Organize and take notes with PyNotes!


#imports
import os
import sys
import time
import textwrap


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

        self.UPL()

    def InitSettings(self):
        self.FileName=None
        self.cpaths = []
        self.cfiles = []
        self.text = ""
        self.cwd = self.MainCwd
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

    def readF(self):
        text = self.text
        
        if self.FileName == None:
            print("[ERROR: NO FILE SELECTED]")
            print("Use SelectFile() to select a file.")
            
        else:
            FileName = self.FileName
            with open(FileName, 'r') as f:
                text = f.read()
                self.text = text
            f.close()

        print(self.text)

    def sf(self, file):
        self.UPL()
        self.FileName = file
        self.readF()
        

    def cd(self, newpath=""):
        if len(str(newpath))==0:
            newpath = self.MainCwd
        elif str(newpath)[-1] == '/':
            newpath = str(newpath)[:-1]
        os.chdir(newpath)
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)
        #self.InitSettings()

    def NewFile(self, name, Type='txt'):
        file = name + "." + Type

        dateCreated = time.asctime()
        
        with open(file, 'w') as f:
            f.write('[FILE: ' + file + ']' + '\n')
            f.write('[DATE CREATED: ' + str(dateCreated)+\
                    ']' + '\n')
        f.close()

    def EditFile(self, file='', system=False, message=""):
        print("to stop typing, press ENTER, then press CONTROL + C")
##        print("type @>>@ to indent")
##        print("type @<<@ to unindent")
##        print("type #Basic# to go back to original indent\n")
        if len(file)>0:
            self.sf(file)
        self.readF()
        if self.FileName == None:
            print("[ERROR: NO FILE SELECTED]")
            print("Use SelectFile() to select a file.")
            return None
        file = self.FileName
        text = self.text
        bulletPoint = "*"
        MainInd = 55
        width = 55
        tab = 0
        '''
        All indenting and bullet point editing will be
        done and implemented in the GUI version of
        PyNotes, expected to be in version v1 or v2
        '''

##        Tabs = list()
##        Tind = {"Str":"#>>#",
##                "Wid":-3,
##                "Ind":3,
##                "bp":"*"}
##        Tout = {"Str":"#<<#",
##                "Wid":3,
##                "Ind":-3,
##                "bp":"*"}
##        Tmain = {"Str":"#Basic#",
##                 "Wid":0,
##                 "Ind":0,
##                 "bp":"*"}
##        Tcurrent = Tmain
##        Tabs.append(Tind)
##        Tabs.append(Tout)
##        Tabs.append(Tmain)
##        def Tabify(Operator="#Basic#"):
##            if Operator == "#>>#":
##                Twidth = None

        with open(file) as f:
            t = f.read()
        f.close()
        if not system:
            while 1:
                
##                width += Tmain['Wid']
##                tab += Tmain['Ind']
##                bulletPoint = Tmain['bp']
                
                
                FinalLine = ''
                print(bulletPoint, end='')
                try:
                    line = sys.stdin.readline()

                except KeyboardInterrupt:
                    break

                if not line:
                    break


                
                    
##                if line == "#>>#":
##                    Tcurrent = Tind
##                elif line == "#<<#":
##                    Tcurrent = Tout
##                elif line == "#Basic#":
##                    Tcurrent = Tmain
##
##                width += Tcurrent['Wid']
##                tab += Tcurrent['Ind']
##                bulletPoint = Tcurrent['bp']
                

##                strTab = ''
##                for t in range(tab):
##                    strTab += ' '
                lines = textwrap.wrap(line, width)
                for l in lines:
                    FinalLine += l + '\n'# + strTab

                #if input is None, then NewLine

                if len(FinalLine) == 0:
                    FinalLine += '\n'

##                elif FinalLine == "@>>@":
##                    width -= 3
##                    bulletPoint += "  >"
##                    tab += 3
##                elif FinalLine == "@<<@":
##                    width += 3
##                    bulletPoint = bulletPoint[:-3]
##                    tab -= 3
##                
##                    
##                
##                tab = tab
##                #if FinalLine == specific string, use
##                #certain bulletpoint or format
##                if width < 55:
##                    tab = 0
##                    width = 55
##                    bulletPoint = "*"
                t += (bulletPoint+FinalLine)
                
                
        else:
            t += 'SYSTEM\t'+message+'\n'

        with open(file, 'w') as f:
            f.write(t)
        f.close()

        with open(file) as f:
            text = f.read()
            self.text = text
        f.close()

        

    
    def lp(self):
        self.UPL()
        print("##########---FOLDERS---##########")
        for c in self.cpaths:
            print(c)
        print("##########----FILES----##########")
        for c in self.cfiles:
            print(c)

    def help(self):
        print('''

        ##########---Help Section---##########

        InitSetting()
        -Sets specific variables to the initial settings

        UPL()
        -Update Path List: Updates the directory

        readF()
        -Reads the current file, and stores it
        in variable: [text].
        
        sf(New File)
        -Selects a file. This file is stored and saved 
        until a new file is selected.

        cd([file])
        -Changes current directory. If left blank, it will
        return to the original directory.

        NewFile(filename, extension=txt)
        -Creates a new file.
        WARNING: IF THE FILE EXISTS, THEN THE ORIGINAL
        WILL BE DELETED

        EditFile()
        -Edits the current file.
        NOTICE: This only works for txt files.

        lp()
        -Lists all folders and files in the current
        directory.

        ''')

    def __str__(self):
        return 'File Name: ' + str(self.FileName) + '\n' +\
               'Main cwd: ' + str(self.MainCwd) + '\n' +\
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

##def OpenFile(fileName, directoryPath="Files/"):
##    fileName = directoryPath+fileName
##    with open(fileName, 'r') as f:
##        text=f.read()
##    f.close()
##    return text

##def NewFile(fileName, directoryPath="Files/"):
##    dirPath=directoryPath + fileName + ".txt"
##    with open(dirPath, 'w') as f:
##        f.write('[FILE: ' + fileName + ']')
##    f.close()

##def AllFiles():
##    UFL()
##    print("------------FILES------------")
##    for f in files:
##        print(str(f))

##def EditFile(fileName):
##    pass

##def ListDir():
##    UPL()
##
##def MainDir():
##    os.chdir(ORIGINAL_CWD)

def startUp():
    def titleDisplay():
        i = 0
        while i<10:
            print()
            i+=1
        print("""
        --------------------
        Welcome to PyNotes V0.1.00
        
        This program is used to take notes
        and save them to a simple text document
        
        Author: Max Ferney
        if you have any questions or concerns
        about this program, you may email
        me at maxferney@gmail.com please set
        the title of the subject to PyNotes, so
        I know what it is. Thank you.
        (Use FileManager to start)
        --------------------
        """)
        i = 0
        while i<7:
            print()
            i+=1
    titleDisplay()


startUp()
FileManager = Data()

    
