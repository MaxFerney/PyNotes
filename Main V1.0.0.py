#Author: Max Ferney
#Date Created: 1.14.2019
#Date Modified: 1.14.2019
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
    elif is_in_time(['mon','wed'],'18:30','21:15',20):
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

