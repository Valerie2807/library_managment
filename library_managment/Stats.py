from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import time
import matplotlib.pyplot as plt

def Stats():


    count = []
    month = []

    con = sqlite3.connect("library.db")
    cur = con.cursor()

    sel = "SELECT count(issuedto), strftime('%m-%Y', Issued_date) FROM books_issued GROUP BY strftime('%m-%Y', Issued_date) "
    cur.execute(sel)
    rows = cur.fetchall()
    for row in rows:
    #print(row)
        count.append(row[0])
        month.append(row[1])

    pos = list(range(12))
    plt.bar(pos,count,color='grey')
    plt.xticks(ticks=pos,labels=month)
    plt.title('Number of Books issued per month')
    plt.xlabel('month')
    plt.ylabel('count of issued books')
    plt.show()
    con.close()



