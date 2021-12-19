




import sqlite3

conn = sqlite3.connect('extensions.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_extensions( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txt TEXT, \
        col_docx TEXT, \
        col_png TEXT, \
        col_mpg TEXT, \
        col_pdf TEXT, \
        col_jpg TEXT \
        )")
    conn.commit()
conn.close()
   

    
conn = sqlite3.connect('extensions.db')


with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_extensions(col_txt) VALUES (?)", \
                ('Hello.txt'))
    conn.commit()
