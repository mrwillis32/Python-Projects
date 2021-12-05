



# Here I'll import sqlite for use in the database
import sqlite3

conn = sqlite3.connect('tables2.db')
# Then we'll connect our tables2.db so it works with sqlite
with conn:
    cur = conn.cursor()
    # the syntax below will create our database and add the columns that we will need
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                  col_txt TEXT)")
    conn.commit()
    # conn.commit() commits the changes we just made to our database 
conn.close()
# here we are closing the connection thus putting an end to our commands

conn = sqlite3.connect('tables2.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# loop through each object in the tuple to find the names that end in .txt.
for x in fileList:
  if x.endswith('.txt'):
    with conn:
      cur = conn.cursor()
    # the value for each row will be one name out of the tuple therefore (x,)
    # will denote a one element tuple for each name ening with .txt.
      cur.execute("INSERT INTO tbl_fileList (col_txt) VALUES (?)", (x,))
      print(x)
conn.close()
