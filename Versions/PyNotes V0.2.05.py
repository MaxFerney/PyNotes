#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 9.16.2015
#Version: 0.2.05
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
            f.write('\t[FILE: ' + file + ']\n')
            f.write('\t[DATE CREATED: ' + str(dateCreated)+\
                    ']\n')
            f.write('\t[Title: ' + TITLE + ']\n')
        f.close()

    def EditFile(self, file='', system=False, message=""):
        
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
        
        bp = str(input('input bullet point type: ')) #Bullet Point
        SaveText = str(input('type(y/n) for TimeStamp text: ')) #controls if last save text is turned on
        savebool = True
        if SaveText == 'n':
            savebool = False
        width = 55
        lenI = 1
        Coding = False
        
        '''
        All indenting and bullet point editing will be
        done and implemented in the GUI version of
        PyNotes, expected to be in version v1.

        IDEA!!!!!
        since the program uses textwrap, which reads and
        edits the text that was inputed...
        use that ability to do bulletpoints/indentation

        this above statement has been officially completed
        as of version 0.1.08.


        replace last index[-1] with [-(len(bp))]

        ##implement code key_command, for code input
            this will have no bullet points
            indents will be either 2 or 4
            textwrap will be turned off

        ##add subtitle key_command

        pySlideShow
            clear screen for each slide
            include margins/borders
        '''

        
        with open(file) as f:
            t = f.read()
        f.close()
        if not system:
            pretext = bp
            ind_lvl = 0
            key_commands = ['done', '-->',
                            '<--', 'ChBp',
                            'TITLELINE', 'SUBTITLE',
                            'CODEMODE', 'CODEEXIT']
            print("""
                to end input: type 'done' or press Ctrl+c
                to indent: type '-->'
                to unindent: type '<--'
                to make title line: type 'TITLELINE'
                to make subtitle line: type 'SUBTITLE'
                to change the bullet point: type 'ChBp'
                to enter Code Input: type 'CODEMODE'
                to exit Code Input: Type 'CODEEXIT'
                
            """)
            while 1:
                
                try:
                    
                    string = input(str(pretext))
                    lenI = len(bp)

                    #key_commands
                    if string.lower() == 'done':
                        break
                    if pretext == '':
                        pretext = bp
                        width = 55
                        
                    elif string == '-->':
                        pretext = '  ' + pretext
                        ind_lvl += 1
                        width -= 2

                    elif string == '<--':
                        if ind_lvl > 0:
                            pretext = pretext[2:]
                            ind_lvl -= 1
                            width += 2

                    elif string == 'ChBp':
                        newbp = str(input('input bullet point: '))
                        pretext = pretext[:-1] + newbp
                        bp = newbp
                            
                    elif string == 'TITLELINE':
                        ind_lvl = 0
                        pretext = ''
                        string2 = input('input title:')
                        string = "--[" + string2 + "]--"

                    elif string == 'SUBTITLE':
                        ind_lvl = 0
                        pretext = ''
                        string2 = input('input subtitle:')
                        string = "[" + string2 + "]"

                    elif string == 'CODEMODE':
                        ind_lvl = 0
                        pretext = ' '
                        Coding = True
                        savedBp = bp
                        bp = ''
                    elif string == 'CODEEXIT':
                        Coding = False
                        pretext = ''
                        bp = savedBp

                    elif len(string) > width:
                        #this is breaking indentation
                        #FIND IT!!!!!
                        lines = textwrap.wrap(string, width)
                        new_string = ''
                        for l in lines:
                            new_string += l + \
                                          '\n' + \
                                          pretext[:-1]# + \
                                          #' '

                        string = new_string
                            
                    
                    #does not write key commands
                    key_match = 3
                    for k in key_commands:
                        if string == k:
                            key_match -= 1
                    if key_match < 3:
                        t += ''
                    else:
                        if len(string) > width:
                            t += pretext + string
                        else:
                            t += pretext + string + '\n'

                    
                except KeyboardInterrupt:
                    break
                    
            else:
                t += 'SYSTEM\t'+message+'\n'



        #This checks if the last time modified was on
        #the same date as the current date..
        #This is to separate your notes by day.
        #It returns true if last modified date is
        #current date.
        def lastDateMatches(string):
            strStart=t.rfind(string)
            date = t[(strStart+20):(strStart+26)]
            initDate = str(self.InitializeTimeStamp)[4:10]

            if date == initDate:
                return True
            else:
                return False
                

        timestampstring = "TIMESTAMPSTR:  "+\
                          '['+\
                          str(self.InitializeTimeStamp)+\
                          ']'
        
        if not lastDateMatches('TIMESTAMPSTR'):
            t += '\n' + \
                 '\t' + timestampstring + \
                 '\n' + \
                 '\t#####Last Save: [' + \
                 time.asctime() + \
                 ']#####\n\n'
        else:
            if savebool:
                t += '\n\tLast Save: [' + \
                     time.asctime() + \
                     ']\n\n'

            #20-26
                 
            
            

        #Ask to backup file
        backupText = str(input('BackUp File?(y/n)'))
        backup = False
        if backupText.lower() == 'y' or backupText.lower() == 'yes':
            backup = True
            
        #Save File
        with open(file, 'w') as f:
            f.write(t)
        f.close()

        #Write to file backup location too
        if backup:
            currentCwd = self.cwd
            os.chdir(self.MainCwd)
            with open('Backup/'+file, 'w') as f:
                f.write(t)
            f.close()
            os.chdir(currentCwd)
            print("Backup Successful!")

        #set current text to text in the file
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
        while i<8:
            print()
            i+=1
        print("""
        --------------------
        Welcome to PyNotes V0.2.05
        
        This program is used to take notes
        and save them to a simple text document
        
        Author: Max Ferney
        if you have any questions or concerns
        about this program, you may email
        me at maxferney@gmail.com please set
        the title of the subject to PyNotes, so
        I know what it is. Thank you.

        This is now on Github!!!
        so everything above is done through github..
        or something like that, you can email me
        if you would like to though still.
        (Use FileManager to start)
        --------------------
        """)
        i = 0
        while i<4:
            print()
            i+=1
    titleDisplay()


startUp()
FileManager = Data()

    
