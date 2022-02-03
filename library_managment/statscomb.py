# --------------------------------------------------------------------------------------------------
# Statistics function
# DATABASE   : library
# TABLES     : BOOKS, BOOKS_ISSUED
# DESCRIPTION: Module which display the statistics of books issued per month and most popular genre
#             Copyright Group 3 2022. All rights reserved.
#
# AUTHORS    : Arturo, Nazneen
#
# REF NO     DATE
# Group 3    26/01/2022
# --------------------------------------------------------------------------------------------------


# import libraries
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt


# Stats function for issued books per month
def Stats():
    count = []
    month = []

    con = sqlite3.connect("library.db")  # connect to library database
    cur = con.cursor()  # define cursor

    # select count of issued books per month from books_issued table
    sel = "SELECT count(issuedto), strftime('%m-%Y', Issued_date) as month FROM books_issued GROUP BY month "
    cur.execute(sel)
    rows = cur.fetchall()
    for row in rows:
        count.append(row[0])
        month.append(row[1])

    # bar graph to show number of books issued per month
    pos = list(range(12))
    plt.bar(pos, count, color='grey')
    plt.xticks(ticks=pos, labels=month)
    plt.title('Number of Books issued per month')
    plt.xlabel('month')
    plt.ylabel('count of issued books')
    plt.show()
    con.close()  # close database connection


# Stats function for most popular books based on genre
def Stats1():
    count1 = []
    genre = []

    con = sqlite3.connect("library.db")  # connect to library database
    cur = con.cursor()  # define cursor

    # select count of students
    sel1 = "SELECT count(bid), Category FROM books where status = 'issued' GROUP BY Category"
    cur.execute(sel1)
    rows = cur.fetchall()
    for row in rows:
        count1.append(row[0])
        genre.append(row[1])

    # Pie chart to display the most popular genre
    fig1, ax1 = plt.subplots()
    ax1.pie(count1, labels=genre, autopct='%1.1f%%')
    ax1.set_title('Most popular genre')
    plt.show()
    con.close()


# Statistics window
def Statistics():
    global bookInfo10, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Statistics", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="1. Issued books per month", bg='black', fg='white', command=Stats)
    btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="2. Popular genre", bg='black', fg='white', command=Stats1)
    btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    root.mainloop()
