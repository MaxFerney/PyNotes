#Author: Max Ferney
#Date Created: 8.12.2015
#Date Created(GUI): 2.14.2017
#Date Modified: 2.16.2017
#Version: 2.0.03
#Description: Organize and take notes with PyNotes!
#Bugs: 0

import os

import tkinter
from tkinter import *
import tkinter.scrolledtext as ScrolledText
import tkinter.filedialog as tkFileDialog
import tkinter.messagebox as tkMessageBox

##def copy_text(text):
##    command='echo '+text.strip()+'| clip'
##    os.system(command)    

root = tkinter.Tk(className=" PyNotes ")
textPad = ScrolledText.ScrolledText(root, width=100, height=80)

# create a menu & define functions for each menu item

def open_command():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()

def save_command():
    file = tkFileDialog.asksaveasfile(mode='w',defaultextension=".txt")
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve \n Now owned by Max Ferney")

def link_command():
    link_text = "http://knowpapa.com/text-editor/"
    label = tkMessageBox
    label.showinfo("Link", link_text)
##    result = label.askyesno("Copy", message="Copy to Clipboard?")
##    if result:
##        copy_text(link_text)
##        #be careful with this..


def new_command():
    file = tkFileDialog.asksaveasfile(mode='w',defaultextension=".txt")
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def dummy():
    print("I am a Dummy Command, I will be removed in the next step")


    
# Initialize Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)

# File Menu
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_command)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)

# Help Menu
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
helpmenu.add_command(label="Links",command=link_command)

# Run
textPad.pack()
root.mainloop()
