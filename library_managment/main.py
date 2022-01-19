from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox
import matplotlib.pyplot as plt
from library_managment.AddBook import *
from library_managment.ViewBooks import *
from library_managment.DeleteBook import *
from library_managment.IssueBook import *
from library_managment.ReturnBook import *
from library_managment.Stats import *



root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")
same = True
n = 0.5
# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)


headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Readers Hub", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="Stats", bg='black', fg='white', command=Stats)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

'''con = sqlite3.connect("library.db")
cur = con.cursor()
sel = "SELECT * FROM books_issued"
cur.execute(sel)
rows = cur.fetchall()
for row in rows:
    print(row)
con.close()'''



root.mainloop()
