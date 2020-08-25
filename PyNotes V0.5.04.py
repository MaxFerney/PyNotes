#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 1.7.2019
#Version: 0.5.04
#Description: Organize and take notes with PyNotes!
#Bugs: 3


#imports
import os
import sys
import time
import textwrap
import webbrowser
#import the paint program?


#globals
files = []
CPaths = []
#DoNotChange
ORIGINAL_CWD = os.getcwd()


#classes
class PyNotes:
    FileName=None
    MainCwd = 'C:\\Users\\lisaf_000\\Desktop\\Python\\PyNotes'
    cwd = None
    path = None
    cpaths = []
    cfiles = []
    InitializeTimeStamp = None
    version = '0.5.04'
    lastIndex = 0
    previousIndex = 0
    last_indented_line = 0
    last_indented_level = 0
    column_width=55
    end_time='00:00'
    
    text = ""

    def __init__(self):
        #self.MainCwd = os.getcwd()
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
        self.column_width = 55
        print("Settings Initialized")

    def UPL(self):
        self.cpaths = list()
        self.cfiles = list()
        cwd = self.cwd
        path = self.path
        for c in os.walk(path).__next__()[1]:
            self.cpaths.append(c)
        for c in os.walk(path).__next__()[2]:
            self.cfiles.append(c)

    def readF(self, sts=False, Display=True):
        #sts = Since Time Stamp
        #counter error with open webbrowser
        text = self.text

        AllLines=True
        lines=200
        
        if self.FileName == None:
            print("[ERROR: NO FILE SELECTED]")
            print("Use sf() to select a file.")
            
        else:
            FileName = self.FileName
            with open(FileName, 'r') as f:
                text = f.read()
                self.text = text
            f.close()

        DisplayText = ""
        counted_lines = 0
        lastIndex = 0
                
        if sts:
            lastIndex = text.rfind('TIMESTAMPSTR')
            DisplayText = text[lastIndex:]
            if Display:
                # \t is for tab before time
                print('\t', end='')
                
        else:
            DisplayText = self.text

        self.text = DisplayText
        if Display:
            print(DisplayText)

    def sf(self, file, show_text=True, alltext=False):
        self.UPL()
        self.FileName = file
        try:
            if not show_text:
                self.readF(sts=True, Display=False)
            else:
                if alltext:
                    self.readF(sts=False, Display=True)
                else:
                    self.readF(sts=True, Display=True)
        except UnicodeDecodeError:
            self.OpenPicture(self.FileName)

    def cd(self, newpath=''):
        if len(str(newpath))==0 or str(newpath)=="" or str(newpath)=='sysmain':
            newpath = self.MainCwd
        elif str(newpath)[-1] == '/':
            newpath = str(newpath)[:-1]
        os.chdir(newpath)
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)


    def OpenPicture(self, filename=''):
        #save current directory
        current_cwd = self.cwd
        #change directory
        self.cd()
        self.cd('Files/PAINT')
        #select file
        if filename == '':
            self.lp()
            filename = input("Input FileName(including extension): ")
        else:
            pass
        #open file
        webbrowser.open(filename)
        #change directory to saved directory
        self.cd()
        self.cd(current_cwd)

    def search(self, string='',
               section_length=100,):
        #maybe use better linear search method.
        #could do binary search by word order
        
        # Initialize Variables
        reset_index = False
        if string == '':
            string=input('string: ')
        stringUpper = string[0].upper() + string[1:]
        stringLower = string[0].lower() + string[1:]
        index = self.text.find(stringUpper, self.lastIndex)
        index2 = self.text.find(stringLower, self.lastIndex)
        #Why use multiple variables for case sensitivity?
        
        # Set Index
        if index < index2 and index != -1:
                self.lastIndex = index
        elif index2 < index and index2 != -1:
                self.lastIndex = index2
                

        # Reset Index
        else:
            print('#\n#\n#Message Text Variable: End String\n#\n#')
            print("==========NO RESULTS FOUND==========")
            reset_index = True

        # Printing
        print('\n\t\t-----------substring-----------\n')
        print(self.text[self.lastIndex-section_length:
                        self.lastIndex+section_length])
        print('\n\t\t-----------substring-----------\n')
    
        # Reset Variables / Reset Index
        if not reset_index:
            print(str(self.lastIndex))
            print('#\n#\n#Message Text Variable: Next String\n#\n#')
            self.lastIndex += 1
            print(str(self.lastIndex))
        else:
            self.lastIndex = 0
            print('#\n#\n#Message Text Variable: Reset String\n#\n#')
            reset_index=False
            
    def NewFile(self, name, TITLE=' ', Type='txt'):
        file = name + "." + Type
        dateCreated = time.asctime()
        page_top = ''
        for i in range(59):
            page_top+='='
        with open(file, 'w') as f:
            f.write('\n' + page_top + '\n')
            f.write('\t[FILE: ' + file + ']\n')
            f.write('\t[DATE CREATED: ' + str(dateCreated)+\
                    ']\n')
            f.write('\t[Title: ' + TITLE + ']\n\n\n')
        f.close()

        self.sf(file, alltext=True)
        print('File Selected')



####################  E D I T   F I L E #####################



    def EditFile(self, file='', system=False, message="",
                 system_vars={'end_time':'00:00'}):
        end_time=system_vars['end_time']
        
        def testchar(string):
            try:
                string = int(string)
                string = chr(string)
            except ValueError:
                string = str(string)
            return string

        def convert_to_min(time_string):
            hour = int(time_string[:2])
            minute = int(time_string[3:])
            total = (hour*60) + minute
            return total

        def adjust_indent(ind_lvl=0,
                          spaces='',
                          width=55,
                          bp='',
                          pretext=''):
            for i in range(ind_lvl):
                spaces += "   "
                width-=3
            pretext = spaces + bp
            return_var = [ind_lvl, spaces, width, bp, pretext]
##            print("IND_LVL: " + str(ind_lvl))
##            print("SPACES:  " + str(len(spaces)))
##            print("WIDTH:   " + str(width))
##            print("BP:      " + str(bp))
##            print("PRETEXT: " + str(pretext))
            return return_var
                



        #if filename variable is used
        if len(file)>0:
            self.sf(file)
        self.readF(sts=True)
        
        #this reads from last timestamp, not whole text
        if self.FileName == None:
            return None
        file = self.FileName
        text = self.text

        width = 55
        #NEW WIDTH VARIABLE HERE
        width = self.column_width
        
        # Initial Variables
        try:
            print()
            bp = input('input bullet point: ')
            #create predefined variable custom error
            bp = testchar(bp)
        
            #text for saving
            
            SaveText = str(input('type(y/n) for TimeStamp text: ')) #controls if last save text is turned on
            savebool = False
            if SaveText == 'y':
                savebool = True

            #start from last index
            indent_bool = False
            last_indent_ask = input('start from last indent(y/n): ')
            if last_indent_ask == 'y':
                indent_bool = True
                
        except KeyboardInterrupt:
            print("#####\tBroken out of the function!\t#####")
            return None

        
        #lenI is length of the bullet point string
        lenI = 1

        #text commands and Variables
        tagging = False
        taggingPretext = ''

        delete_last_line = False
        last_string = ''
        last_string_array = []
        last_string_array.append(last_string)

        t = ''

        ordering = False
        current_number = 1
##        ind_lvl = 0
        ordered_ind_lvl = 0
        temp_bp = bp
        start_order = False
        
        with open(file) as f:
            t = f.read()
        f.close()
        
        if not system:
            #pretext is the bullet and space before a string
            pretext = bp
            ind_lvl = 0
            key_commands = ['DONE', 'CHBP', 'CHPB',
                            'HELP',
                            '--->', '<---',     #user errors
                            '0>', '<0',       #user errors
                            '==>', '<==',       #user errors
                            '--', '<-', '->',   #user errors
                            ',--', '--.',       #user errors
                            '-->>', '<<--',     #user errors
                            '>', '<',           #user errors
                            '--:', ':--',       #user errors
                            '<--', '-->',
                            'TITLELINE', 'SUBTITLE',
                            'HEADER',
                            'CODEMODE', 'CODEEXIT',
                            'BULLETS', 'SIDENOTE',
                            'DELETE_LAST_LINE',
                            'TAGSTRING',
                            'ORDERED', 'ORDERED END',
                            'TIME',
                            'LINEBREAK',
                            'UNDERLINE',
                            'LINK']
            
            user_errors = ['--->', '<---',     
                            '0>', '<0',       
                            '==>', '<==',       
                            '--',   
                            ',--', '--.',       
                            '-->>', '<<--',     
                            '>', '<',           
                            '--:', ':--']
            
            print("""
            to end input: type 'DONE' or press Ctrl+c
            to indent: type '-->'
            to dedent: type '<--'
            to see more functions: type 'HELP'
                
            """)
            # Functions
            def edit_functions():
                print("""
                to end input: type 'DONE' or press Ctrl+c
                to indent: type '-->'
                to dedent: type '<--'
                to make a tagged string: type 'TAGSTRING'
                to make a sidenote: type 'SIDENOTE'
                to make a highlight: type 'HIGHLIGHT'
                to make a header: type 'HEADER'
                to change bullet point: type 'CHBP'
                to enter Code Input: type 'CODEMODE'
                to exit Code Input: type 'CODEEXIT'
                to see bullet points: type 'BULLETS'
                to erase last line: type 'DELETE_LAST_LINE'
                to make a list: type 'ORDERED'
                to exit list mode: type 'ORDERED END'
                to check for time remaining: 'TIME'
                to break with line: type 'LINEBREAK'
                to underline: type 'UNDERLINE'
                to note a link: type 'LINK'

                to see this page: type 'HELP'
                    
                """)
            def specialPoints():
                for i in range(1, 9):
                    print(str(i) + ' = ' + chr(i))
                for i in range(11, 32):
                    print(str(i) + ' = ' + chr(i))


            def tag_string(system=False,
                           tagstart='blank',
                           tagend='blank',
                           pretext='',
                           lenI=0,
                           double=False):
                # Inputs
                if not system:
                    tagstart = input('start tag: ')
                    tagend = input('end tag: ')
                tagstart = testchar(tagstart)
                tagend = testchar(tagend)
                note = input('NOTE: ')
                #Function
                taggingPretext = pretext
                pretext = pretext[:-lenI]
                #Do double function
                if double:
                    string = tagstart + tagstart + \
                             ' ' + note + ' ' + \
                             tagend + tagend
                else:
                    string = tagstart + \
                             '' + note + '' + \
                             tagend
                tagging = True
                if len(pretext) + len(string) >= 55:
                    print(pretext + string + '\n')
                else:
                    print(pretext + string)
                variables = [taggingPretext, tagging, string, pretext]
                return variables


            def textwrap_function(string,width,pretext,lenI):
                lines = textwrap.wrap(string, width)
                new_string = ''
                for l in lines:
                    index = lines.index(l)
                    
                    #single line
                    if index == len(lines)-1:   #if index is length of lines
                        new_string += l + '\n'  #line
                    #multiple lines
                    else:                        
                        new_string += l + '\n' +  pretext[:-lenI] + '  '
                        #line
                        #\n
                        #no bullet point,but indentation
                        #added indentation spaces

                string = new_string
                variables = [string, width, pretext, lenI]
                return variables

            def Underline(last_string,pretext_var):
                #Underlines the previous line/text input
#################Add for if substring not in string
                pretext = pretext_var
                utext = input('text: ')
                try:
                    string_index = last_string.index(utext)
                except ValueError:
                    string_index=-1
                    
                under=''
                first=''
                last=''

                #if string not in previous statement
                if string_index == -1:
                    for i in range(len(utext)):
                        under += '^'
                    string = utext+'\n'+under
                #if string in previous statement
                else:
                    for i in range(len(utext)):
                        under += '^'
                    for i in range(string_index):
                        first+=' '
                    for i in range(len(last_string)-(string_index+len(utext))):
                        last+=' '
    ##                for i in range(string_index+len(utext)):
    ##                        last+=' '
    ##                string = first+under+last + '\n'
                
                    string = first+under+'\n'
                
                variables=[string, string_index, [first,under,last]]
                return variables

##def loop():
##	text = ''
##	last_string='test string'
##	while True:
##		try:
##			pretext = ''
##			string=input()
##			if string=='underline':
##				utext = input('text: ')
##				string_index = last_string.index(utext)
##				under=''
##				first=''
##				last=''
##				for i in range(len(utext)):
##					under += '^'
##				for i in range(string_index):
##					first+=' '
##				for i in range(string_index+len(utext)):
##					last+=' '
##				string2 = first+under+last
##				string= string2+'\n'
##			text += string+'\n'
##			last_string=string+'\n'
##		except KeyboardInterrupt:
##			return text
##			break
##	return text
            #this function may be interfering with saving
            def Ordered(bp,
                        ind_lvl,
                        ordered_ind_lvl,
                        current_number,
                        temp_bp,
                        ordering,
                        pretext,
                        start_order,
                        lenI,
                        string,
                        key_commands):

                #fix numbers indentation..
                #fix bp recovery
                #do blank line
                
                
                #Reset
                if start_order:
                    ordered_ind_lvl = ind_lvl
                    temp_bp = bp
##                    print('temp bp: ' + temp_bp)
##                    print('\n--Ordering Start--\n')
                    start_order = False
                    ordering = True
                #Exit
                elif (ind_lvl < ordered_ind_lvl and ordering) or \
                     (string == 'ORDERED END'): #mod
                    #" string = '' "?
                    ordering = False
                    current_number = 1
                    lenI = len(bp) #this fixes the code.
                    bp = temp_bp
##                    print('\n--ind_lvl < ordered list--\n')
                    pretext = pretext[:-lenI] + bp
                #Indent
                elif ind_lvl > ordered_ind_lvl and ordering:
                    ordering = True
                    bp = ' -'
##                    print('\n--l > ordered list--\n')
                    pretext = pretext[:-lenI] + bp
                #Increase Number
                elif ind_lvl == ordered_ind_lvl and ordering:
                    key = False
                    for k in key_commands:
                        if string == k:
                            key=True
                    if not key:
                        current_number += 1
                    bp = str(current_number) + ')'
##                    print('\nind_lvl = ordered list\n')
                    pretext = pretext[:-lenI] + bp

                variables = [bp,
                             ind_lvl,
                             ordered_ind_lvl,
                             current_number,
                             temp_bp,
                             ordering,
                             pretext,
                             start_order,
                             lenI]
                return variables

            #Open File
            with open(file, 'w') as f:
                f.write(t)
            f.close()


            if indent_bool:
                inner_width = 55
                inner_width -= (self.last_indented_level*2)
                var = adjust_indent(ind_lvl=self.last_indented_level,
                                    spaces='',
                                    width=inner_width,
                                    bp=bp,
                                    pretext=pretext)
                ind_lvl = var[0]
                spaces = var[1]
                width = var[2]
                pretext = var[4]
                
                

                            
            #This checks if the last time modified was on
            #the same date as the current date..
            #This is to separate your notes by day.
            #It returns true if last modified date is
            #current date.
            def lastDateMatches(string):
                strStart=t.rfind(string)
                date = t[(strStart+20-1):(strStart+26-1)]
                initDate = str(self.InitializeTimeStamp)[4:10]

                if date == initDate:
                    return True
                else:
                    return False
                    

            timestampstring = "TIMESTAMPSTR: "+\
                              ' '+\
                              str(self.InitializeTimeStamp)+\
                              ' '
            
            if not lastDateMatches('TIMESTAMPSTR'):
                long_line = ''
                for s in range(54):
                    long_line += '+'
                t += '\n' + long_line
                t += '\n' + \
                     '\t' + timestampstring + \
                     '\n' + \
                     '\tLast Save:     ' + \
                     time.asctime() + \
                     ' \n'
                t += long_line + '\n\n\n'

    ####################--LOOP--####################
         
            while 1: 
                try:
                    if pretext == '' :
                        pretext = bp
                        width = 55

                    elif tagging:
                        tagging = False
                        pretext = taggingPretext

                    elif ordering:
##                        bp = str(current_number) + ')'
##                        pretext = pretext[:-lenI] + bp
                        var = Ordered(bp,
                                      ind_lvl,
                                      ordered_ind_lvl,
                                      current_number,
                                      temp_bp,
                                      ordering,
                                      pretext,
                                      start_order,
                                      lenI,
                                      string,
                                      key_commands)
                        bp = var[0]
                        ordered_ind_lvl = var[2]
                        current_number = var[3]
                        temp_bp = var[4]
                        ordering = var[5]
                        pretext = var[6]


                        
                    string = input(str(pretext))
                    lenI = len(bp)

                    
                    
                    #key_commands
                    if string == 'DONE':
                        break
                    #indent
                    elif string == '-->' or \
                         string == '--->' or \
                         string == '->':
                        spaces = '  '
                        for i in range(lenI):
                            spaces += ' '
                        pretext = spaces + pretext
                        ind_lvl += 1
                        width -= len(spaces) #2

                        indent_vars = [pretext,
                                       ind_lvl,
                                       width,
                                       spaces]
                    #dedent
                    elif string == '<--' or \
                         string == '<---' or \
                         string == '<-':
                        if ind_lvl > 0:
                            pretext = pretext[lenI+2:]
                            ind_lvl -= 1
                            width += len(spaces) #2

                            indent_vars = [pretext,
                                           ind_lvl,
                                           width,
                                           spaces]
                    #change bullet
                    elif string == 'CHBP' or \
                         string == 'CHPB':
                        char = input('input bullet point: ')
                        newbp = testchar(char)
                        pretext = pretext[:-lenI] + newbp
                        bp = newbp

                    #user error message
                    elif string in user_errors:
                        print("\t-----input not recorded-----")

                    #help
                    elif string == 'HELP':
                        edit_functions()
                        print()
                    
                    #title        
                    elif string == 'TITLELINE':
                        ind_lvl = 0
                        pretext = ''
                        string2 = input('input title: ')
                        string = "--[" + string2 + "]--"
                        print(string)
                    #subtitle
                    elif string == 'SUBTITLE':
                        ind_lvl = 0 #change this...do tagstring for this
                        pretext = ''
                        string2 = input('input subtitle: ')
                        string = "[" + string2 + "]"
                        print(string)
                    #header
                    elif string == 'HEADER':
                        var = tag_string(True,
                                         "[", "]",
                                         pretext=pretext,
                                         lenI=lenI,
                                         double=False)
                        taggingPretext = var[0]
                        tagging = var[1]
                        string = var[2]
                        pretext = var[3]
                        
                    #codemode
                    elif string == 'CODEMODE':
                        ind_lvl = 0
                        pretext = ''
                        savedBp = bp
                        bp = '.'
                    #codeexit
                    elif string == 'CODEEXIT':
                        pretext = ''
                        bp = savedBp

                    #bullet point list
                    elif string == 'BULLETS':
                        specialPoints()

                    #tell the time until class ends
                    elif string == 'TIME':                        
                        current_time = str(time.asctime())[11:16]
                        end_time = self.end_time
                        cminutes = convert_to_min(current_time)
                        eminutes = convert_to_min(end_time)
                        min_left = eminutes-cminutes
                        print('\n\t\tTime:  '+\
                              str(min_left)+\
                              ' Minutes Remaining\n')

                    #line break
                    elif string == 'LINEBREAK':
                        pretext=''
                        linestring=''
                        for i in range(54):
                            linestring+=('#')
                        print(linestring)
                        string=linestring

                    #underline
                    elif string == 'UNDERLINE':
                        pretext = ''
                        var=Underline(last_string_array[-1],pretext)
                        string = var[0]

                    #link
                    elif string == 'LINK':
                        pretext=''
                        border = '++++++++'
                        ltype = input('input type: ')
                        lname = input('input name: ')
                        for i in range(len(ltype)):
                            border += '+'
                        for i in range(len(lname)):
                            border += '+'
                        print(border)
                        print('++ '+ltype.upper()+': '+lname+' ++')
                        print(border)
                        string=border+'\n'+\
                                '++ '+ltype.upper()+': '+lname+' ++'+'\n'+\
                                border+'\n'
                            
                            

                    #tag string
                    elif string == 'TAGSTRING':
                        var = tag_string(pretext=pretext,
                                         lenI=lenI)
                        taggingPretext = var[0]
                        tagging = var[1]
                        string = var[2]
                        pretext = var[3]
                    elif string == 'SIDENOTE':
                        var = tag_string(True,
                                         "{", "}",
                                         pretext=pretext,
                                         lenI=lenI)
                        taggingPretext = var[0]
                        tagging = var[1]
                        string = var[2]
                        pretext = var[3]
                    elif string == 'HIGHLIGHT':
                        var = tag_string(True,
                                         chr(4), chr(4),
                                         pretext=pretext,
                                         lenI=lenI,
                                         double=True)
                        taggingPretext = var[0]
                        tagging = var[1]
                        string = var[2]
                        pretext = var[3]

                    #delete last line
                    elif string == 'DELETE_LAST_LINE':
                        if len(last_string_array) > 1:
                            try:
                                t = t[0:-len(last_string_array[-1])]
                                print(pretext[:lenI] +\
                                      'deleted string:' +\
                                      last_string_array[-1])
                                last_string_array.pop()
                            except IndexError:
##                                print('You\'ve erased all of the lines')
                                print('Cannot Erase')
                                print('you are not supposed to  be here')
                        else:
                            print('Cannot Erase')

                    #ordered bullets
                    elif string == 'ORDERED':# or ordering:
                        if not ordering:
                            start_order = True
                            bp = temp_bp

##                        print('\nordering from string')
                        ordering = True
                        if ordering:
                            var = Ordered(bp,
                                          ind_lvl,
                                          ordered_ind_lvl,
                                          current_number,
                                          temp_bp,
                                          ordering,
                                          pretext,
                                          start_order,
                                          lenI,
                                          string,
                                          key_commands)
                            bp = var[0]
                            ind_lvl = var[1]
                            ordered_ind_lvl = var[2]
                            current_number = var[3]
                            temp_bp = var[4]
                            ordering = var[5]
                            pretext = var[6]
                            start_order = var[7]
                            lenI = var[8]
                            
                    elif string == 'ORDERED END':
                        ordering = False
##                        bp = temp_bp #this breaks it
                        


                    #Text Wrap
                    #This must be last conditional
                    elif len(string) > width:
                        var = textwrap_function(string, width, pretext, lenI)
                        string = var[0]
                        width = var[1]
                        pretext = var[2]
                        lenI = var[3]
                        
                            
                    
                    #does not write key commands
                    key_match = 1
                    self.last_indented_line = lenI
                    self.last_indented_level = ind_lvl
                    
                    for k in key_commands:
                        if string == k:
                            key_match -= 1
                            
                    if key_match < 1:
                        t += ''
                        

                    #finalizes text variable "t"
                    #creates "last_string" variable
                    else:
                        if string == '':
                            t += '\n'
                            last_string = '\n'
                            
                        elif len(string) > width:
                            t += pretext + string
                            last_string = pretext + string
                        else:
                            t += pretext + string + '\n'
                            last_string = pretext + string + '\n'

                        last_string_array.append(last_string)


                #Break Loop    
                except KeyboardInterrupt:
                    break
                    
            else:
                t += 'SYSTEM\t'+message+'\n'


        #This shows the time of the last save,
        #if savebool is true.

        if savebool:
            t += '\n\tLast Save: [' + \
                 time.asctime() + \
                 ']\n\n'
            

        #Ask to backup file
        try:
            backupText = str(input('BackUp File?(y/n)'))
            backup = True
            if backupText.lower() == 'n' or backupText.lower() == 'no':
                backup = False
        except KeyboardInterrupt:
            backup=True
            print('---Keyboard Interrupted---')
            
        #Save File
        with open(file, 'w') as f:
            f.write(t)
        f.close()

        #Write to file backup location too, if backup=True
        if backup:
            
            #Changes file name in backup
            month_int=str(time.gmtime().tm_mon)
            if len(month_int)<2:
                month_int="0"+month_int
            day_int=str(time.gmtime().tm_mday)
            if len(day_int)<2:
                day_int="0"+day_int
            time_string = str(month_int+\
                              day_int+\
                              time.asctime()[11:13]+\
                              time.asctime()[14:16]+\
                              time.asctime()[17:19])
            #backup path
            f_index=str(self.path).rindex('\\')
            folder = self.path[f_index+1:]
            
            currentCwd = self.cwd
            os.chdir(self.MainCwd)
            os.chdir('Backup')
            
            try:
                os.mkdir(folder)
                os.chdir(folder)
            except FileExistsError:
                os.chdir(folder)
            
            new_filename = file[:-4]+\
                           '_'+time_string+\
                           '.txt'
            
            with open(new_filename, 'w') as f:
                f.write(t)
            f.close()
            os.chdir(currentCwd)
            print("\n\tFILENAME: "+new_filename)
            print("\tBackup Successful!\n")

        #Set current text to text in the file
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

    def bugs(self):
        #Bug Tracker
        #... I lost track of the bugs... oops
        #guess it failed to do its job
        print('''

            ------Bugs------
            01  ###FIXED###
                Indentation with numbered bullets
                
                getting rid of it breaks numbered indent
                    but fixes overall indent
                keeping it breaks overall indent
                    but fixes numbered indent

            02  ###FIXED###
                Saved Indent
                    not tested for bullet points longer
                     than one character long

            03  ###FIXED###
                Saved Indent
                    textwrap broken if used.
                TRY TO ADD WIDTH TO LAST INDENT IF USED

            04
                Underline
                    not built for textwrap function
                    Just use for one liners

            05
                Underline
                    gives an extra line, need to fix
                    line spacing

            06  ###FIXED###
                Delete last line
                    does not work if you are not deleting
                    from the same indent

            07  ###FIXED###
                Delete last line
                    if used more that once it will erase
                    again, but using the previous text
                    length
                    ... perhaps fix this by turning the
                    last lines into an array and deleting
                    from the array as a line is deleted.

            08  ###FIXED###
                Underline
                    substring not in previous string raises
                    value error. Now it doesnt, but it's a
                    bit glitchy without it.

            09  Header
                    indenting directly after using header function
                    does not work if current indent level is 0

            


            ''')


    def VersionLog(self):
        print('''
        All indenting and bullet point editing will be
        done and implemented in the GUI version of
        PyNotes, expected to be in version v1.

        since the program uses textwrap, which reads and
        edits the text that was inputed...
        use that ability to do bulletpoints/indentation

        this above statement has been officially completed
        as of version 0.1.08.


        ##replace last index[-1] with [-(len(bp))]

        ##implement code key_command, for code input
            this will have no bullet points
            indents will be either 2 or 4
            textwrap will be turned off

        ##add subtitle key_command

        pySlideShow
            clear screen for each slide
            include margins/borders
            -text version
            -PySlides is pygame version

        ##Shorten the read text
            make it in the  past 50 lines
            or in the past 300 characters
            ##or since the last TIMESTAMPSTR

        ##put the timestampstr at before rest of text

        ##Make a new file for the outline.
            this will use the bp pretty much.
            import the new data class, and
            modify so:
                class outliner(data):
                    def EditFile() #this is only
                                   #thing changed

        ##needs modify previous lines
            erase lines..
            maybe not break on input.........
                This can cause a TON of problems..
                if it is even possible in the first place

        ##Add SideNote Capability
            if there is something not related to the topic

        #<REVISIT> Implement a Highlight Mode(
            It would make the object more noticible
            try to use fonts or abstract characters
            try using Colorama
                (only works in system console)

            Use Error Text Colors, special colors.
                needs to make a custom font for this

            #use <>[]{}()//\\||(make tags)

        0.3.02(incomplete)
        AUTOSAVE
            an autosave feature to pretty much run the
            editfile function multiple times.
                editFile(inloop=False):
                    ...
                    editFile(inloop=True)
                    ...
        0.3.05
        Implement Search feature
            display all TITLELINEs
            add tags
            allow the user to search for a title/tags
            

        Look into Ipython/jupyter
            ipython is a website for Jupyter
        
        ###Custom Made Warning    
        import warnings as w
        >>> w.showwarning("message", Warning, "mod", 21)



        Add a spell checker feature
            This will be able to edit everything up to
            the top
            Use a text file for reference, maybe one for
            each topic or study.
                place a text file in the corresponding
                subject

        
        ##Add a command to entirely delete the above line
            make it easy not to mistake it, or call it
            accidentally
        look for a bullet point, so that other lines
        can be deleted


        Create a few custom errors for more specific
            error handling
            predefined variables in function
                bullet point, save



        --->>>Tables and simple graphs (for econ)

        


        0.3.04
        TextWrap Function
        Hightlight and sidenote are pretty much identical.
            Make it a function, maybe with the textwrap
            function.

        0.3.03
        Allow subtitle to be indented

        0.3.05.1    
        add a numbered bullet point function
            input number of bullets
        self.NewFile() now selects the file when created
            
        0.3.05
        Simplified self.readF() function
            got rid of useless code

        0.3.06
        add bug tracker

        0.3.06.1 (planned)
        Raise an error where the bug is.

        0.3.08
        Continue from last indent.
            use for frequently saving while taking notes
            (since it kept crashing while note taking)
--------------------------------------------------
        0.3.09
        Fall 2016 Semester
        0.3.09.1 
        Include a time for classes
            current time, time until end
            implement this with notes function
            #or time function with editfile.
        0.3.09.2
        give editfile a "class" mode
            -will determine time remaining
            
        0.3.10
        Completion of 0.3.09.x
        0.3.10.1 (planned) #IMPORTANT
        for backup, keep multiple files stored
            use different names based on time it was saved
            No overwriting the backup file.
            
        0.3.11
        Completion of 0.3.10.x
            back up files are now actual backups
        0.3.11.1
        [tables using ascii.
        [basic calculations.
            [does this in a different program]
        (for now build it for econ)
            Line Break?
                -make a line long as the width of the screen
                -for separating sections of the notes
        for backups, use a file folder for the backup file
            to eliminate clutter of files
        0.3.11.2
        use hyperlink to go to a pypaint picture.
            for diagrams
            #perhaps link through html/filepath?
            #screenshot picture by pressing s to save it.
        #just name it in the notes, then just find the
            file in the folder
            
        0.3.12
        Completion of Backup folders
        Completion of PyPaint opening files
        Linebreak (does not save to file, just display)
        0.3.12.1
        UNDERLINE!!!
            use ^^ as the next line somehow, this may take
            a while to figure out
            Does not work with current set up.
                perhaps if underline was for current line
        linebreak writes to file.
        image text more clear.. (figure reference)
        help function to edit file
        0.3.12.2
        link to excel/google sheets


        
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         !0.4.00!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



        0.4.00
        !!Link Update!!
        ie: picture
        UNDERLINE IDEA:
            delete last line, then find which line it is on (no "last" text)
            then find text in that line, insert underline for that line, and
            continue with rest of text!

        0.4.01
        -Hitting keyboard interrupt while checking backup
            this does lead to back it up, rather than
            delete the entire file
        -Default backup boolean is now True
        -Added Header
            this is for a title that is under an indent
            broad subject, easier categorization
        0.4.01.1
        -make a box around text
            Do function first, then input string so that
            the box can account for the multiple lines
            Do this in a similar fashion as the link
            function.

            
        0.4.02
        -2017 Spring Semester
        0.4.02.1
        -modify delete_last_line function
            -turn it into an array
            -when the function is called delete it from
              the array as well

        0.4.03
        -Stabilized and fixed bugs with the Delete last line
        function, it works flawlessly without any bugs.
        -Added a clear function, to clear the screen.

        0.4.04
        -replaces month string with integer value in backup
        -does same for day
        -for both: if single digit, makes it 2 digit

        0.4.05
        -will use web_browser class more often
            -make options to link to:
                -blackboard
                -wingspan
                -winthrop
        0.4.06
        -FALL 2017
        -simplified notes function

        0.4.07
        -built in keyboard interrupt exception catch
            for the edit file 3 initial input variables.
            -prevents crash

        0.4.08
        -2017 Spring Semester

        0.4.08.1
        -Added error handling to underline function


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                         !0.5.00!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        0.5.01
        -Fall 2018 Update
        -initial settings displays confirmation message.

        0.5.01.1
        -add a check for user error and response. this will
         prevent the user from deleting last line on
         user error bullet points. a message will pop up
         when the user inputs a user error

        0.5.02
        -user error successfully implemented and tested.

        0.5.02.1
        -changing codemode and codeexit
            codemode changes bullet point to ' '
            codeexit changes bullet point to the original
             which will have been saved

        0.5.03
        -codemode and codeexit updated.
            bugs fixed by
                changing pretext to ''
                changing bp from ' ' to '.'
                    this fixes indentation lock bug
            learned that Coding bool doesnt do anything.
                removed it!

        0.5.04
        -Updated for Spring 2019
        


            
            









        -------------------------------
        1.0.00
        -this will have a multi-tiered "PyApps"
            -PY APPS
            -will include slides, notes, paint, outline, (pandas?)
            -maybe include graph as well? that is finicky
            perhaps just a pycalculator
            -simple scientific calculator
            -have a time at the side
                -have a time till end of class at side too
        -going to need to do a separate program entirely
            -This separate program will eventually be
            turned into the program PyApps GUI

        -------------------------------
        2.0.00
        -by this time PyNotes will be in GUI form

        0.2.03
        -has a base text editor
        -saves basic .txt files
        -can do other types of files

        0.2.04
        -File/pdf opener? tkinter project perhaps

        0.2.04.1
        -Attempt to move PyNotes to its own, import it
         through another programe.
            -Other program will have schedule and focus more
             on user customization.
        -This will allow updates to the schedule separate
         from the actual development, therefore less
         version progression.
        
        
        
        
        
        
                     
        ''')


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
        
        sf(filename)
        -Selects a file. This file is stored and saved 
        until a new file is selected.

        cd(path)
        -Changes current directory. If left blank, it will
        return to the original directory. Type '..' to
        move up one level in the directory.

        NewFile(filename, title, extension=txt)
        -Creates a new file.
        WARNING: IF THE FILE EXISTS, THEN THE ORIGINAL
        WILL BE DELETED

        EditFile()
        -Edits the current file.
        NOTICE: This only works for txt files.

        lp()
        -Lists all folders and files in the current
        directory.

        search(string='',display_section=100)
        -Search for a string. Can have a set amount of
        characters displayed on both sides of the string.
        display_section is characters on both sides
        displayed.

        OpenPicture(filename='')
        -Opens a picture to be displayed. The picture must
        be saved in the PAINT path in Files.

        bugs()
        -Displays a list of current bugs in the code

        VersionLog()
        -Displays version log of this program

        open_site()
        -Opens a specific website in a browser



        help()
        -Uhh, How did you get here in the first place?

        ''')

    def open_site(self):
        print("""

        type a number to go to a website:
        [1] Winthrop
        [2] Wingspan
        [3] BlackBoard
        [4] Custom URL

        """)
        choice = int(input('Selection: '))
        #Winthrop
        if choice==1:
            webbrowser.open('https://www.winthrop.edu')
        #Wingspan
        elif choice==2:
            webbrowser.open('https://ssb.winthrop.edu/prod/twbkwbis.P_WWWLogin')
        #BlackBoard
        elif choice==3:
            webbrowser.open('https://bb-winthrop.blackboard.com/')
        #Custom URL
        elif choice==4:
            custom_url=input("Input the URL you wish to open: \n\t")
            webbrowser.open(custom_url)


    def __str__(self):
        return '---------File Name: ' + str(self.FileName) + '\n' +\
               '---------Main cwd: ' + str(self.MainCwd) + '\n' +\
               '---------Current cwd: ' + str(self.cwd) + '\n' +\
               '---------Current path: ' + str(self.path) + '\n' +\
               '---------Time Stamp: ' + str(self.InitializeTimeStamp) + '\n' +\
               '---------Version: v' + str(self.version) + '\n' +\
               '---------Version Log: ' + '\n'
               
        

        


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
        for i in range(8):
            print()
        print("""
        --------------------
        Welcome to PyNotes V0.5.04
        
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
        --------------------

        for help, type py.help()
        """)
        for i in range(4):
            print()
    titleDisplay()


startUp()
py = PyNotes()


#This is only if you have subdirectories in your 'files'
#folder

def quickstart(path,
               system=False,
               file=None,
               end_time='00:00'):
    global py
    
    py = PyNotes()
    py.end_time = end_time
    py.cd()
    py.cd('Files')
    py.cd(path)
    if not system:
        pass
    if system:
        py.sf(file, show_text=False)
        py.EditFile()
        
        
    
    

def notes():
    
    
    #Wed Oct 28 08:34:13 2015
    day = time.asctime()[:3]
    hour = time.asctime()[11:13]
    minute = time.asctime()[14:16]
    str_time = time.asctime()[11:16]
    
    day = day.lower()
    hour = int(hour)
    minute = int(minute)


    def convert_time(time='08:00'):
        time_hour = int(time[0:2])
        time_min = int(time[3:])

        minutes = 0
        minutes += (time_hour * 60) + time_min

        return minutes
        

    def is_in_time(days=['mon', 'tue', 'wed', 'thu', 'fri'],
                   starttime='08:00',
                   endtime='21:30',
                   minutes_before_start=30):
        
        start_minutes = convert_time(starttime)
        current_minutes = convert_time(str_time)
        end_minutes = convert_time(endtime)
        
        for d in days:
            if day == d:
                if current_minutes >= (start_minutes - minutes_before_start) and \
                   current_minutes <= end_minutes:
                    return True
                else:
                    return False

    #classes

    #Computer Science
    if is_in_time(['tue', 'thu'],'09:30','10:45',15):
        quickstart('CSCI', True, 'csci_243.txt', '10:45')
    #Digital Information Design
    elif is_in_time(['tue','thu'],'12:30','14:20',15):
        quickstart('DIFD', True, 'difd_311.txt', '14:20')
    #Geology Lecture
    elif is_in_time(['mon', 'wed'],'12:30','13:45',10):
        quickstart('GEOL', True, 'geol_110.txt', '13:45')
    #Geology Lab
    elif is_in_time(['wed'],'14:30','17:20',10):
        quickstart('GEOL', True, 'geol_113.txt', '17:20')
    #Visual Communications
    elif is_in_time(['mon','wed'],'18:30','21:15',15):
        quickstart('VCOM', True, 'vcom_262.txt', '21:15')

    else:
        print("you are not in class right now.")
        print("use: quickstart(path) to see notes.")
        



def convert_to_min(time_string):
    hour = int(time_string[:2])
    minute = int(time_string[3:])
    total = (hour*60) + minute
    return total
    
    
def clear(lines=30):
    for i in range(lines):print()


