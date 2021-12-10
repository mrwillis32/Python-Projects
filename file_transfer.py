




import shutil
import os




#set where the source of the files are
source = '/Users/mr.willis/Desktop/Folder A/'

#set the destination path to folder b
destination = '/Users/mr.willis/Desktop/Folder B/'
files = os.listdir(source)

for i in files:
    #We are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

import shutil
import os


#set where the source of the files are
source = '/Users/mr.willis/Desktop/Daily Files/'

destination = '/Users/mr.willis/Desktop/Home Office Files/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)


#Python program to create
# a file explorer in Tkinter

# import all componets
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "**.*")))

    # Create label contents
    label_file_explorer.configure(text="File Opened: "+filename)



# Create the root window
window = Tk()


# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")

button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)

button_exit = Button(window,
                     text = "Exit",
                     command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column =1, row = 2)

# Let the window wait for any events
window.mainloop()
