from tkinter import *
from tkinter import ttk
#from connection import dbConnect
#from customer import *
#from doctor import *
#from drug import *
#from employee import *
#from supplier import *
#from manufacturer import *
#from warehouse import *

from tkinter import *

root=Tk()
Title_label= Label(root,text="Pharmacy Database ").grid(row=0,column=1)
root.geometry("400x400")

#new windows
def open_insert():
    top = Toplevel()
    top.title("Insert")
    top.geometry("250x250")
    label1 = Label(top, text="Insert").pack()
    btn1 = Button(top, text="Close Window", command=top.destroy).pack()

def open_delete():
    top = Toplevel()
    top.title("Delete")
    top.geometry("250x250")
    label1 = Label(top, text="Delete").pack()
    btn1 = Button(top, text="Close Window", command=top.destroy).pack()

def open_Select():
    top = Toplevel()
    top.title("Select")
    top.geometry("250x250")
    label1 = Label(top, text="Select").pack()
    btn1 = Button(top, text="Close Window", command=top.destroy).pack()

def open_update():
    top = Toplevel()
    top.title("Update")
    top.geometry("250x250")
    label1 = Label(top, text="Update").pack()
    btn1 = Button(top, text="Close Window", command=top.destroy).pack()

#buttons
Insert_button=Button(root,text="Insert",padx=50,pady=10,fg="white",bg="black",comman=open_insert).grid(row=1,column=1)
Select_button=Button(root,text="Select",padx=50,pady=10,fg="white",bg="black",command=open_Select).grid(row=2,column=1)
Delete_button=Button(root,text="Delete",padx=50,pady=10,fg="white",bg="black",command=open_delete).grid(row=3,column=1)
Update_button=Button(root,text="Update",padx=50,pady=10,fg="white",bg="black",command=open_update).grid(row=4,column=1)

# shoving it onto the screen
# Title_label.pack()
# Insert_button.pack()
# Delete_button.pack()
# Select_button.pack()
# Update_button.pack()
root.mainloop()



if __name__ == "__main__":
    main()
