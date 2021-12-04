



# Here I'll import sqlite for use in the database
import sqlite3

conn = sqlite3.connect('tables2.db')
# Then we'll connect our tables2.db so it works with sqlite
with conn:
    cur = conn.cursor()
    # the syntax below will create our database and add the columns that we will need
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileLists( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_docx TEXT, \
        col_txt TEXT, \
        col_png TEXT, \
        col_mpg TEXT, \
        col_pdf TEXT, \
        col_jpg TEXT \
        )")
    conn.commit()
    # conn.commit() commits the changes we just made to our database 
conn.close()
# here we are closing the connection thus putting an end to our commands

conn = sqlite3.connect('tables2.db')


with conn:# with conn let's us know that as long as we are connected to our database run the below code.
    # here I iterated through the function to select our two file ext with '.txt'
     fileList = ('information.docx', 'Hello.txt', 'myImage.png', \ 'myMovie.mpg', 'World.txt','data.pdf','myPhoto.jpg')
for extensions in fileList:
  print('Hello.txt','World.txt')
        conn.commit()
conn.close()
# here we will be adding our values into our table


conn = sqlite3.connect('tables2.db')


with conn:  
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_fileLists(col_txt) VALUES (?)"
                ( 'Hello.txt'))
    conn.commit()
conn.close()


conn = sqlite3.connect('tables2.db')


with conn:  
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_fileLists(col_txt) VALUES (?)"
                ('World.txt'))
    conn.commit()
conn.close()
