# -----------------------------------------------------------------------------------
# AddBook function
# DATABASE   : library
# TABLES     : BOOKS, BOOKS_ISSUED
# DESCRIPTION: Module which adds new book entries to the library database
#             Copyright Group 3 2022. All rights reserved.
#
# AUTHORS    : Nazneen
#
# REF NO     DATE
# Group 3    12/01/2022
# -----------------------------------------------------------------------------------


# import python libraries
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3


# BookRegister function
def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    category = bookInfo5.get()
    status = status.lower()

    conn = sqlite3.connect('library.db')  # connect to library database
    cur = conn.cursor()  # define cursor

    # Enter Table Names here
    bookTable = "books"  # Book Table

    insertBooks = "insert into " + bookTable + " values('" + bid + "','" + title + "','" + author + "','" + status + "','" + category + "')"

    cur.execute(insertBooks)  # execute insert query
    conn.commit()
    conn.close()  # close database connection
    messagebox.showinfo('Success', "Book added successfully")

    root.destroy()


# Add books into library
def addBook():
    # define global variables
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, bookInfo5, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Book Category
    lb5 = Label(labelFrame, text="Category: ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.85, relheight=0.08)

    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3, rely=0.85, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
