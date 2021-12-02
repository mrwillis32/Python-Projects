





import sqlite3

conn = sqlite3.connect('tables.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_ext( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_docx TEXT, \
        col_txt TEXT, \
        col_png TEXT, \
        col_mpg TEXT, \
        col_pdf TEXT, \
        col_jpg TEXT \
        )")
    conn.commit()
conn.close()


