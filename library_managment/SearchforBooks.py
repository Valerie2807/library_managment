from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('library.db')
cur = con.cursor()
bookTable = "books"

def searchbook():
    global bookInfo10
    Category = bookInfo10.get()
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Search Result", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s %-30s %-20s %-20s %-20s" % ('BID', 'Title', 'Author','Status','Category'), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)

    try:
        #cur.execute("select * from " + bookTable)
        cur.execute("select * from  "+bookTable+" where Category = '"+Category+"'")
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-20s%-20s%-20s" % (i[0], i[1],i[2], i[3], i[4]), bg='black',
                    fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)



def SearchforBooks():
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

    headingLabel = Label(headingFrame1, text="Search for Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='green')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
    # Book Category
    lb5 = Label(labelFrame, text=" Search Category: ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.55, relheight=0.08)

    SubmitBtn8 = Button(root, text="Search Now", bg='#d1ccc0', fg='black', command=searchbook)
    SubmitBtn8.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    bookInfo10 = Entry(labelFrame)
    bookInfo10.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)
    #Category = bookInfo10.get()


    root.mainloop()