#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 9.04.2015
#Version: 0.1.03
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
    InitializeTimeStamp = None
    
    text = ""

    def __init__(self):
        self.MainCwd = os.getcwd()
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)

        self.InitializeTimeStamp = str(time.asctime())

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
        for c in os.walk(path).__next__()[1]:
            self.cpaths.append(c)
        for c in os.walk(path).__next__()[2]:
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

    def NewFile(self, name, TITLE=' ', Type='txt'):
        file = name + "." + Type

        dateCreated = time.asctime()
        
        with open(file, 'w') as f:
##            f.write('REFERENCE_TIME\n')
            f.write('\t[FILE: ' + file + ']\n')
            f.write('\t[DATE CREATED: ' + str(dateCreated)+\
                    ']\n')
            f.write('\t[Title: ' + TITLE + ']\n')
        f.close()

    def EditFile(self, file='', system=False, message=""):
        print("to stop typing, press ENTER, then press CONTROL + C")
        #use line numbers in text to go back and edit line
        #will be used with index
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
        PyNotes, expected to be in version v1.
        '''

        with open(file) as f:
            t = f.read()
        f.close()
        if not system:
            while 1:
                                
                FinalLine = ''
                print(bulletPoint, end='')
                try:
                    line = sys.stdin.readline()

                except KeyboardInterrupt:
                    break

                if not line:
                    break

                lines = textwrap.wrap(line, width)
                for l in lines:
                    FinalLine += l + '\n'

                #if input is None, then NewLine
                if len(FinalLine) == 0:
                    FinalLine += '\n'

                t += (bulletPoint+FinalLine)
                
                
        else:
            t += 'SYSTEM\t'+message+'\n'



        #this block of code is useless...
        #it simple does not work...
        def findStringInLine(string):
            strStart=t.rfind(string)
            strCompare0=t.rfind('[', \
                                strStart, \
                                strStart+25)
            strCompare1=t.rfind(']', \
                                strCompare0, \
                                strCompare0+25)
            dateStr = t[strCompare0+1:strCompare1]
            if self.InitializeTimeStamp == dateStr:
                return False
            else:
                return True
                

        timestampstring = "TIMESTAMPSTR:  "+\
                          '['+\
                          str(self.InitializeTimeStamp)+\
                          ']'
        if findStringInLine('TIMESTAMPSTR'):
            t += '\n\n' + \
                 timestampstring + \
                 '\n' + \
                 'Last Save: [' + \
                 time.asctime() +\
                 ']\n'

##            if self.InitializeTimeStamp == dateStr:
##                return False
##            else:
##                return True
            #19-26
                 
            
            

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

        help()
        -Displays this text...

        ''')

    def __str__(self):
        return 'File Name: ' + str(self.FileName) + '\n' +\
               'Main cwd: ' + str(self.MainCwd) + '\n' +\
               'Current cwd: ' + str(self.cwd) + '\n' +\
               'Current path: ' + str(self.path) + '\n' +\
               'Time Stamp: ' +\
               str(self.InitializeTimeStamp) + '\n'
               
        

    
        


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


def startUp():
    def titleDisplay():
        i = 0
        while i<10:
            print()
            i+=1
        print("""
        --------------------
        Welcome to PyNotes V0.1.03
        
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

    
