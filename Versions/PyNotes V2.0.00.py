


"""
######################################

IDEA:
current users:
add the joined users to a list, if they leave, then
remove them from the list

######################################
"""

'''
-------------------------------------------------------
from tkinter import *

root = Tk()


label1 = Label( root, text="Month(MM)")
E1 = Entry(root, bd =5)

label2 = Label( root, text="Day(DD)")
E2 = Entry(root, bd =5)

label3 = Label( root, text="Year(YYYY)")
E3 = Entry(root, bd =5)

def getDate():
    print (E1.get())
    print (E2.get())
    print (E3.get())

submit = Button(root, text ="Submit", command = getDate)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
submit.pack(side =BOTTOM) 
root.mainloop()
'''



'''
-------------------------------------------------------
from tkinter import *
root = Tk()
class Application(Frame):
    root = Tk()
    entrytxt = None
##    def say_hi(self):
##        root = self.root
##        print("hi there, everyone!")

##    def user(self):
##        pass
    
    def chat(self):
        root = self.root
        self.entrytxt = Entry()
        #self.entrytxt.pack()
        
        self.root.geometry("400x200")
        
        self.contents = StringVar()
        self.contents.set("text")
        self.entrytxt["textvariable"] = self.contents
        self.entrytxt.bind('<Key-Return>',
                              self.uploadText)
        
        

    def uploadText(self, event):
        root = self.root
        print(self.contents.get())
        

    def createWidgets(self):
        root = self.root
##        self.QUIT = Button(self)
##        self.QUIT["text"] = "Leave Chat"
##        self.QUIT["fg"]   = "red"
##        self.QUIT["command"] =  self.quit
##
##        self.QUIT.pack({"side": "left"})

        self.Speak = Button(self)
        self.Speak["text"]  = "Enter"
        self.Speak["fg"]    = "green"
        self.Speak["command"] = self.chat
        
        self.root.geometry("400x200")
        self.Speak.pack({"side": "bottom"})




        
##        self.hi_there = Button(self)
##        self.hi_there["text"] = "Hello",
##        self.hi_there["command"] = self.say_hi
##
##        self.hi_there.pack({"side": "left"})
        

    def __init__(self, master=Tk()):
        root = self.root
        
        Frame.__init__(self, master)
        
        self.createWidgets()
        self.root.geometry("400x200")
        self.pack()


root = Tk()
app = Application(master=root)
#app.geometry("400x200")
app.mainloop()


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
print("text widget")
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()



-------------------------------------------------------

# use Tkinter to show a digital clock
# tested with Python24    vegaseat    10sep2006
 
from Tkinter import *
import time
 
root = Tk()
time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)
 
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
 
tick()
root.mainloop(  )
-------------------------------------------------------
'''
#Created by: Max Ferney
#tkinter windows... http://www.python-course.eu/tkinter_menus.php
print("input name:\n")
name = input('\t')

print("\nclear on enter?(yes/no)")
auto_clear_ask = input('\t')
if auto_clear_ask.lower() == "yes" or auto_clear_ask.lower() == "y":
    auto_clear = True
else:
    auto_clear = False



##print("\nAuto-Update?(yes/no)")
##AU = {"state":False,"AUI":5}
##auto_update_ask = input('\t')
##if auto_update_ask.lower() == "yes" or auto_update_ask.lower() == "y":
##    AU["state"] = True
##    
##    print("\ntime interval(in seconds, min=2, max=20, and default=5)[WIP and not working at moment]:")
##    AUI_ask = input('\t')
##    if int(AUI_ask) < 2 or int(AUI_ask) > 20:
##        AU["AUI"] = 5
##    else:
##        AU["AUI"] = int(AUI_ask)
##    
##else:
##    AU["state"] = False

AU = {"state":False,"AUI":5}
##print("\ngroup chat:")
##c_group_ask = input()
##if c_group_ask == None:
##    c_group = c_group_ask
print()
#from game_menu import GameMenu

import sys
import os
import time
##import pygame
from tkinter import *
root = Tk()
class App(Frame):
    name=""
    autoClear = False
    c_group = '__PYNOTES_GUI_'
    chats = []
    chat_buttons = []
    #chat_menus = []
    
##    autoUpdate = False
##    AUI = 5
##    start = 0
##    elapsed = 0
    
    text = None
    def __init__(self, name,
                 autoClear=True,       #autoUpdate=False,AUI=5,
                 master=None):          #all new variables directly before this
        Frame.__init__(self, master)
        self.pack()

        
##        start_group = '_Main Chat_'
##        if self.c_group == 'DEBUG' or self.c_group == '':
##            self.c_group = '_Main Chat_'

        
        self.UFL()
        
        self.name = name
        self.autoClear = autoClear
##        self.autoUpdate = autoUpdate
##        self.AUI = AUI

        self.readF()

        self.entrythingy = Entry()
        self.entrythingy.pack()
##        self.entrythingy["yscrollcommand"] = self.text

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("") #this is a variable
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

        
        ''' manually clear text '''
        self.hi_there = Button(self)
        self.hi_there["text"]       = "Clear"
        self.hi_there["fg"]         = "red"
        self.hi_there["command"]    = self.clear_text

        self.hi_there.pack({"side": "left"})

        ''' refresh '''
        self.refresh = Button(self)
        self.refresh["text"]    = "Refresh"
        self.refresh["fg"]      = "green"
        self.refresh["command"] = self.update
        
        self.refresh.pack({"side": "left"})

        ''' Quit '''
        self.QUIT = Button(self)
        self.QUIT["text"] = "Leave Chat"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.leave_chat

        self.QUIT.pack({"side": "left"})

        ''' New Chat '''
        self.NewChat = Button(self)
        self.NewChat["text"] = "New Chat"
        self.NewChat["fg"] = "blue"
        self.NewChat["command"] = self.Make_Chat

        self.NewChat.pack({"side": "left"})
        
        ''' Chats '''
##        self.UFL()
        for c in self.chats:
            
            if c["name"]==self.c_group:
                c["joined"]=True
                c["color"]="green"
                #self.c_group = c["name"]
                
            else:
                c["joined"]=False
                c["color"]="red"
            
            self.chat_buttons.append(self.chat_button(c))
                    
        for cb in self.chat_buttons:
            index = self.chat_buttons.index(cb)
            if cb["text"] == "DEBUG":
                self.chat_buttons[index].configure(state=DISABLED)
            cb.pack({"side": "bottom", "pady": 1})


##        ''' Menu Bar '''
##        menubar = Menu(root)
##
##        self.menu_buttons(self.chats).add_cascade(label="Chats", menu=MENU)
##        menubar.add_cascade(label="chats", menu=self.menu_buttons(self.chats))
##        menubar.add_cascade(label="Chats", menu=MENU)
##            

##        ''' Scroll Bar '''
##        if self.text_window:
##            self.scrlbar = ScrolledText(self, text=self.text)
##            self.scrlbar["yscrollcommand"] = None
##            self.scrlbar.pack({"side": "right",
##                               "expand": True,
##                               "in":master,
##                               "fill":"y",})

##        if autoUpdate:
##            self.start = time.time()
##            self.elapsed = time.time()-self.start
##            if self.elapsed>=AUI:
##                self.start = time.time()
##                self.update()
##                print(str(time.time()))

    


                
    ''' General Functions '''
    def upload_contents(self, string="", mode="user"):
        c_group = self.c_group
        # opens file and saves a text variable
        # this variable is the "old" text
        file = 'Files/Tests/'+str(c_group)+'.txt'
        with open(file) as f:
            t = f.read()
        f.close()

        #records text and adds to "old"
        t+=string
        t+="\n"
        
        #saves
        with open(file, 'w') as f:
            f.write(t)
        f.close()

        #text variable is now "read"
        with open(file) as f:
            text = f.read()
            self.text = text
        f.close()

        #updated AFTER text, so text is displayed with it
        if mode == "user":
            self.update()

            #automatically clears text, if clear_text is true
            if self.autoClear:
                self.clear_text()

        if mode == "join":
            self.update()
            #automatically clears text
            self.clear_text()
        
        if mode == "quit":
            self.update()
            self.quit()

    def clear_text(self):
        self.contents.set("")

    def readF(self):
        c_group = self.c_group
        text = self.text
        FileName = 'Files/Tests/' + str(c_group) + '.txt'

        
        with open(FileName, 'r') as f:
            text = f.read()
            self.text = text
        f.close()

    def update(self):
        c_group = self.c_group
        file = 'Files/Tests/'+str(c_group)+'.txt'
        with open(file) as f:
            display = f.read()
            self.text = display
        f.close()

        print("############UPDATED############")
        print(display)
        print()
        print("---notice---")
        print("When changing chats, make sure to go to main chat first, then your chat. \nYou must do this every time you switch.")


    def UFL(self):
        self.chats = list()
        cwd = os.getcwd()
        path = os.path.join(cwd, "Files\\Tests\\")
        #print("------------FILES------------")
        for c in os.walk(path).__next__()[2]:
            #print(c)
            self.chats.append({"file":c,
                               "name":str(c)[:-4],
                               "joined":False,
                               "color":"red"})
            for ch in self.chats:
                if ch["name"]==self.c_group:
                    ch["joined"]=True
                    ch["color"]="green"
                    #self.c_group = ch["name"]
                else:
                    ch["joined"]=False
                    ch["color"]="red"

                    

    def chat_button(self, config):
        return Button(self,
                      text=str(config["name"]),
                      fg=str(config["color"]),
                      command=lambda: self.switch_chat(config))

##    def menu_buttons(self, cfglst):
##        menubar = Menu(root)
##        MENU = Menu(self, menubar, tearoff=0)
##        for cfg in cfglst:
##            MENU.add_command(label=str(cfg["name"]),
##                             command=lambda: self.change_chat(cfg))
##
##        return MENU
##        
        
        


    def switch_chat(self, config):
        
        for c in self.chats:
            self.change_color(config)
            index = self.chats.index(c)
            if self.chats[index]["joined"]:
####                if self.chats[index]["name"] == config["name"]:
####                    break
##                if self.chats[index]["name"] != "_Main Chat_":
##                    self.c_group = "_Main Chat_"
                
                
                string = "SYSTEM\tUSER: ["+self.name+"] HAS LEFT THE CHAT"
                self.upload_contents(string, "join")
                self.chats[index]["joined"] = False
                self.chats[index]["color"] = "red"
                
                self.c_group = config["name"]
                
                print("##########################")
                string = "SYSTEM\tUSER: ["+self.name+"] HAS JOINED CHAT: "+self.c_group     #config["name"]
                self.upload_contents(string, "join")
                config["joined"] = True
                config["color"] = "green"
                
        
        
    def change_chat(self, cfg):
        print("button", str(cfg["name"]))
        self.change_color(cfg)


        
    def change_color(self, cfg):
        for cb in self.chat_buttons:
            index = self.chat_buttons.index(cb)
            if cfg["name"] == cb["text"]:
                cfg["color"] = "green"
                cfg["joined"] = True
                self.chat_buttons[index].configure(fg=cfg["color"])
            else:
                cfg["color"] = "red"
                cfg["joined"] = False
                self.chat_buttons[index].configure(fg=cfg["color"])


    def Make_Chat(self):
        filewin = Toplevel(self)
        label = Label(self, text="Chat Name")
        E = Entry(self)
        
        label.pack()
        E.pack()
        
##        def doesExist():
##            for c in self.chats:
##                if c["file"]==file:
##                    return True
##                else:
##                    return False
##        if doesExist():
##            label.configure(text="Error: File Already Exists")
##            E.set("")
##            E = Entry(self)
##            file = str(E.get())+".txt"
            
        def create():
            file = E.get()+".txt"
            with open('Files/Tests/'+file, 'w') as f:
                f.write("Welcome to the "+str(file)[:-4]+" chat\n")
            f.close()
                
        Submit = Button(filewin, text="Create", command=create)
        Submit.pack()


        self.UFL()


    ''' chatting '''
    def leave_chat(self):
        #Time String
        string = "SYSTEM\tUSER: ["+self.name+"] HAS LEFT THE CHAT"
        self.upload_contents(string, "quit")

    def join_chat(self):
        #Time String
        string = "SYSTEM\tUSER: ["+self.name+"] HAS JOINED THE CHAT"
        self.upload_contents(string, "join")

    def print_contents(self, event):
        if self.contents.get() == '':
            self.update()
        else:
            string = self.name+": "+self.contents.get()
            self.upload_contents(string, "user")



    ''' return values '''
    def getText(self):
        return self.text

    def values(self):
        self.readF()
        #"auto clear":self.autoClear,
        #"auto update":self.autoUpdate,
        #"auto update interval":self.AUI
        return {"name":self.name,
                "c_group":self.c_group,
                "chats":self.chats}

    
        
        
##    def running(self, event):
##        start = time.time()
##        if not self.autoUpdate:
##            self.autoUpdate = True
##        while True:
##            if self.autoUpdate:
##                elapsed = time.time()-start
##                if elapsed>=self.AUI:
##                    elapsed = 0
##                    start = time.time()
##                    self.update()
##                    #print(str(time.time()))
##            if self.contents.get() == '':
##                break
##            else:
##                break
##            
##        self.autoUpdate = False
    


myapp = App(name, auto_clear)
stats = myapp.values()
height = (len(stats["chats"])*40) + 50
#
# here are method calls to the window manager class
#

strH = str(height)

winsize = "450x"+strH
myapp.master.title("Pychat")
myapp.master.geometry(winsize)
myapp.master.maxsize(1000, 800)

# start the program
myapp.join_chat()
myapp.mainloop()
try:
    root.destroy()
except TclError:
    myapp.leave_chat()
##    try:
##        myapp.leave_chat()
##    except NameError:
##        myapp.leave_chat()

#TclError













##from tkinter import *
##class App:
##  def __init__(self, master):
##    frame = Frame(master)
##    frame.pack()
##    self.button = Button(frame, 
##                         text="QUIT", fg="red",
##                         command=frame.quit)
##    self.button.pack(side=LEFT)
##    self.slogan = Button(frame,
##                         text="Hello",
##                         command=self.write_slogan)
##    self.slogan.pack(side=LEFT)
##  def write_slogan(self):
##    print("Tkinter is easy to use!")
##
##root = Tk()
##app = App(root)
##root.mainloop()
##
##
##
##
##



##import tkinter as tk
##
##class Demo1:
##    def __init__(self, master):
##        self.master = master
##        self.frame = tk.Frame(self.master)
##        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
##        self.button1.pack()
##        self.frame.pack()
##    def new_window(self):
##        self.newWindow = tk.Toplevel(self.master)
##        self.app = Demo2(self.newWindow)
##
##class Demo2:
##    def __init__(self, master):
##        self.master = master
##        self.frame = tk.Frame(self.master)
##        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
##        self.quitButton.pack()
##        self.frame.pack()
##    def close_windows(self):
##        self.master.destroy()
##
##def main(): 
##    root = tk.Tk()
##    app = Demo1(root)
##    root.mainloop()
##
##if __name__ == '__main__':
##    main()
