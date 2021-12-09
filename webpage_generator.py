# import module
import codecs
  
# to open/create a new html file in the write mode
f = open('webpage_generator.html', 'w')
  
# the html code which will go in the file GFG.html
html_template = """
<html>
<body>
    <h1>
        Stay tuned for our amazing summer sale!
    </h1>
</body>
</html>
"""
  
# writing the code into the file
f.write('Stay tuned for our amazing summer sale!')
  
# close the file
f.close()
  
# viewing html files
# below code creates a 
# codecs.StreamReaderWriter object
file = codecs.open("webpage_generator.html", 'r', "utf-8")
  
# using .read method to view the html 
# code from our object
print(file.read())





# Import Module
from tkinter import *

 
# create root window
root = Tk()
 
# root window title and dimension
root.title("")
# Set geometry(widthxheight)
root.geometry('350x200')
 
# adding a label to the root window
lbl = Label(root, text = "Add Sale Item!")
lbl.grid()
 
# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)
 
 
# function to display user text when
# button is clicked
def clicked():
 
    res = "You wrote " + txt.get()
    lbl.configure(text = res)
 
# button widget with red color text inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)
 
# Execute Tkinter
root.mainloop()
        



