#Author: Max Ferney
#Date Created: 1.14.2019
#Date Modified: 8.21.2019
#Version: 1.0.0
#Description: Using the PyNotes class, this program mostly
#               uses a schedule function. Rather than
#               having the function in pynotes class.
#Bugs: 0


#imports
from PyNotes import *


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
        Welcome to PyNotes V0.5.05

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

        Eventually properly set up on github...
        [this is first attempt using with github]
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


    #time variable has to be both 24 hour and double digit
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
    if is_in_time(['tue', 'thu'],'12:30','13:45',15):
        quickstart('CSCI', True, 'csci475.txt', '13:45')
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


def StartLoop():
    while True:
        try:
            print("""
            Type 'help' for more commands. ctrl+c to quit. Basic Commands:
            notes | quickstart | cd | sf | edit

            """)
            String = input(">>>")
            if (String.lower() == "notes"):
                notes()
            elif (String.lower() == "quickstart"):
                Param1 = input("Path: ")
                quickstart(Param1)
            elif (String.lower() == "help"):
                print("""

                notes
                quickstart
                help
                cd
                sf
                lp
                readf
                newfile
                editfile
                clear

                """)
            elif (String.lower() == "readf"):
                Param1 = input("STS (True | False): ")
                if Param1.lower() == "true":
                    Param1 = True
                else:
                    Param1 = False
                py.readF(Param1)
            elif (String.lower() == "cd"):
                Param1 = input("Path: ")
                py.cd(Param1)
            elif (String.lower() == "lp"):
                py.lp()
            elif (String.lower() == "sf"):
                Param1 = input("FileName (with extension): ")
                py.sf(Param1)
            elif (String.lower() == "newfile"):
                Param1 = input("FileName (without extension): ")
                Param2 = input("Title: ")
                Param3 = input("Extension (default=txt): ")
                py.NewFile(Param1, Param2, Param3)
            elif (String.lower() == "editfile"):
                Param1 = input("FileName (optional): ")
                py.EditFile(file=Param1)
            elif (String.lower() == "clear"):
                clear()
            else:
                print("Something went wrong...")



        except KeyboardInterrupt:
            print("To open again, type StartLoop()")
            break;

#StartLoop()
