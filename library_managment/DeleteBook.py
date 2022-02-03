# -----------------------------------------------------------------------------------
# DeleteBook function
# DATABASE   : library
# TABLES     : BOOKS, BOOKS_ISSUED
# DESCRIPTION: Module which deletes book entries from books table
#             Copyright Group 3 2022. All rights reserved.
#
# AUTHORS    : Valeria
#
# REF NO     DATE
# Group 3    12/01/2022
# -----------------------------------------------------------------------------------


# import libraries
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')  # connect to library database
cur = con.cursor()  # define cursor

# Enter Table Names here
issueTable = "books_issued"  # Books_issued Table
bookTable = "books"  # Book Table


# Delete books from library
def deleteBook():
    # Enter book id to be deleted
    bid = bookInfo1.get()

    # delete from books and books_issued tables
    deleteSql = "delete from " + bookTable + " where bid = '" + bid + "'"
    deleteIssue = "delete from " + issueTable + " where bid = '" + bid + "'"
    try:
        messagebox.showinfo("Alert")
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    bookInfo1.delete(0, END)
    root.destroy()


def delete():
    # define global variables
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    # library window
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
