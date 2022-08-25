from tkinter import *
from tkinter import ttk


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1530x1530")

        Title_label = Label(self.root, text="Pharmacy Management System",bd=15,relief=RIDGE,fg="white",bg="green",padx=2,pady=4)
        Title_label.pack(side=TOP,fill=X)

        #Data frame
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,text="Medicine Information",bd=10,relief=RIDGE)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight = LabelFrame(DataFrame, text="Medicine Add Department", bd=10, relief=RIDGE)
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        #Button frame
        ButtonDataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonDataFrame.place(x=0, y=520, width=1530, height=65)

        #Buttons
        btnAdd=Button(ButtonDataFrame,text="Add Medicine").grid(row=0,column=0)
        btnUpdate = Button(ButtonDataFrame, text="Update Medicine").grid(row=0, column=1)
        btnDelete = Button(ButtonDataFrame, text="Delete Medicine").grid(row=0, column=2)

        #search by
        btnSearch = Button(ButtonDataFrame, text="Search Medicine").grid(row=0, column=3)

def main():
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
