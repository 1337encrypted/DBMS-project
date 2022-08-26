# +-------------+-------------+------+-----+---------+-------+
# | Field       | Type        | Null | Key | Default | Extra |
# +-------------+-------------+------+-----+---------+-------+
# | NAME        | varchar(20) | YES  |     | NULL    |       |
# | AGE         | int         | YES  |     | NULL    |       |
# | PH_NO       | varchar(10) | YES  |     | NULL    |       |
# | EMPLOYEE_ID | int         | NO   | PRI | NULL    |       |
# | SHIFT_TIME  | varchar(20) | YES  |     | NULL    |       |
# +-------------+-------------+------+-----+---------+-------+

from tkinter import *
from tkinter import ttk
import mysql.connector as connector
from connectionModule import dbConnect
from insertModule import insert
from deleteModule import deleteRecord
from selectModule import read
from updateModule import update
import time

print("Initializing Pharmacy database...")
time.sleep(3)
print(dbConnect())
root = Tk()
root.title("Pharmacy database")
root.geometry("1100x360")
my_tree = ttk.Treeview(root)
storeName = "EMPLOYEE TABLE"                      #name of the table
titleFont = ('Arial bold', 30)                    #Title font

#====================================Text box (entry) parameters========================
bdwid = 2                                       #text box width
entrywid = 25                                   #text boxes containers width
tbbgclr = '#fef2c9'                              #text box background color
#====================================label parameters===================================
lpadval = 5                                     #label pad value
labelFont = ('Helvetica bold', 15)                #label font
#labelbgcolor = "cyan"                            #label background color
#====================================button paramaters==================================
btnwidth = 5
btnbgcolor = "red"
#=========================================flags==========================================
flag = False

def exit():
    print("==========================================EXITING==========================================")
    root.destroy()
    
def clrBoxes():
    #Clear the text boxes
    entryName.delete(0,END)
    entryAge.delete(0,END)
    entryPhone.delete(0,END)
    entryId.delete(0,END)
    entryShift.delete(0,END)

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def insertData():
    employeeName = str(entryName.get())
    employeeAge = str(entryAge.get())
    employeePhone = str(entryPhone.get())
    employeeId = str(entryId.get())
    employeeShift = str(entryShift.get())
    print("+++++++++++++++++++++++++++++++++++++++++USER DEFINED EXCEPTION+++++++++++++++++++++++++++++++++++++++++")
    if employeeId == "" or employeeId == " " :
        print("Error Inserting employee id")
    if employeeName == "" or employeeName == " ":
        print("Error Inserting employee name")
    if employeeAge == "" or employeeAge == " ":
        print("Error Inserting employee age")
    if employeePhone == "" or employeePhone == " ":
        print("Error Inserting Phone number")
    if employeeShift == "" or employeeShift == " ":
        print("Error Inserting employee shift time")

    else:
        flag = insert(str(employeeName), str(employeeAge), str(employeePhone), str(employeeId), str(employeeShift))
        if(flag):
            flag=False
            clrBoxes()
        
    my_tree.tag_configure('grey', background='lightgrey')
    my_tree.tag_configure('normal', background='white')
    
    myTag='normal'
    
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        if(myTag=='grey'):
            myTag='normal'
        else:
            myTag='grey'
        my_tree.insert("",'end', iid=result, text="", values=(result), tag=(myTag))

    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
    

def deleteData():
    try:
        selected_item = my_tree.selection()[0]
        deleteData = int(my_tree.item(selected_item)['values'][3])
        deleteRecord(deleteData)
    except IndexError:
        print("+++++++++++++++++++++++++++++++++++++++++USER DEFINED EXCEPTION+++++++++++++++++++++++++++++++++++++++++")
        print('Please select a tuple to delete')
        print("+++++++++++++++++++++++++++++++++++++++++++END OF EXCEPTION+++++++++++++++++++++++++++++++++++++++++++++")

    myTag='normal'
        
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        if(myTag=='grey'):
            myTag='normal'
        else:
            myTag='grey'
        my_tree.insert("",'end', iid=result, text="", values=(result), tag=(myTag))
        
    my_tree.tag_configure('grey', background='lightgrey')
    my_tree.tag_configure('normal', background='white')
    
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


def updateData():
    try:
        employeeName = str(entryName.get())
        employeeAge = str(entryAge.get())
        employeePhone = str(entryPhone.get())
        employeeId = str(entryId.get())
        employeeShift = str(entryShift.get())
        
        if employeeId == "" or employeeId == " " :
            print("Error Inserting employee id")
        if employeeName == "" or employeeName == " ":
            print("Error Inserting employee name")
        if employeeAge == "" or employeeAge == " ":
            print("Error Inserting employee age")
        if employeePhone == "" or employeePhone == " ":
            print("Error Inserting Phone number")
        if employeeShift == "" or employeeShift == " ":
            print("Error Inserting employee shift time")
        else:
            selected_item = my_tree.selection()[0]
            update_name = my_tree.item(selected_item)['values'][3]
            flag = update(employeeName, employeeAge, employeePhone, employeeId, employeeShift, update_name)
            if(flag):
                flag=False
                clrBoxes()
    except IndexError:
        print("+++++++++++++++++++++++++++++++++++++++++USER DEFINED EXCEPTION+++++++++++++++++++++++++++++++++++++++++")
        print('Please select a tuple to update')
        print("+++++++++++++++++++++++++++++++++++++++++++END OF EXCEPTION+++++++++++++++++++++++++++++++++++++++++++++")
        
    myTag='normal'
    
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        if(myTag=='grey'):
            myTag='normal'
        else:
            myTag='grey'
        my_tree.insert("",'end', iid=result, text="", values=(result), tag=(myTag))
        
    my_tree.tag_configure('grey', background='lightgrey')
    my_tree.tag_configure('normal', background='white')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

#==========================================Formatting of the GUI=======================================================
titleLabel = Label(root, text=storeName, font=titleFont, bd=2)
titleLabel.grid(row=0, column=1, columnspan=7, padx=20, pady=20)


employeeNameLabel = Label(root, text="Employee Name:", font = labelFont)
employeeAgeLabel = Label(root, text="Employee Age:", font = labelFont)
employeePhoneLabel = Label(root, text="Employee Phone:", font = labelFont)
employeeIdLabel = Label(root, text="Employee ID:", font = labelFont)
employeeShiftLabel = Label(root, text="Employee Shift:", font = labelFont)

employeeIdLabel.grid(row=1, column=0, padx=lpadval, pady=lpadval, sticky=W)
employeeNameLabel.grid(row=2, column=0, padx=lpadval, pady=lpadval, sticky=W)
employeeAgeLabel.grid(row=3, column=0, padx=lpadval, pady=lpadval, sticky=W)
employeePhoneLabel.grid(row=4, column=0, padx=lpadval, pady=lpadval, sticky=W)
employeeShiftLabel.grid(row=5, column=0, padx=lpadval, pady=lpadval, sticky=W)

entryId = Entry(root, width=entrywid, bd=bdwid, font=labelFont, bg=tbbgclr)
entryName = Entry(root, width=entrywid, bd=bdwid, font=labelFont, bg=tbbgclr)
entryAge = Entry(root, width=entrywid, bd=bdwid, font=labelFont, bg=tbbgclr)
entryPhone = Entry(root, width=entrywid, bd=bdwid, font=labelFont, bg=tbbgclr)
entryShift = Entry(root, width=entrywid, bd=bdwid, font=labelFont, bg=tbbgclr)

entryId.grid(row=1, column=1, columnspan=3, padx=lpadval, pady=lpadval)
entryName.grid(row=2, column=1, columnspan=3, padx=lpadval, pady=lpadval)
entryAge.grid(row=3, column=1, columnspan=3, padx=lpadval, pady=lpadval)
entryPhone.grid(row=4, column=1, columnspan=3, padx=lpadval, pady=lpadval)
entryShift.grid(row=5, column=1, columnspan=3, padx=lpadval, pady=lpadval)

buttonEnter = Button(root,text="Insert",padx=lpadval,pady=lpadval,width=btnwidth,bd=3,font=labelFont,bg=btnbgcolor,command=insertData)
buttonEnter.grid(row=6, column=1, columnspan=1)

buttonUpdate = Button(root,text="Update",padx=lpadval,pady=lpadval,width=btnwidth,bd=3,font=labelFont,bg=btnbgcolor,command=updateData)
buttonUpdate.grid(row=6, column=2, columnspan=1)

buttonDelete = Button(root,text="Delete",padx=lpadval,pady=lpadval,width=btnwidth,bd=3,font=labelFont,bg=btnbgcolor,command=deleteData)
buttonDelete.grid(row=6, column=3, columnspan=1)

buttonExit = Button(root,text="Exit",padx=lpadval,pady=lpadval,width=btnwidth,bd=3,font=labelFont,bg=btnbgcolor,command=exit)
buttonExit.grid(row=6, column=8, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font = labelFont)

#===========================================tree view=====================================================
my_tree['columns'] = ('1', '2', '3', '4', '5')
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('1', anchor=W, width=130)
my_tree.column('2', anchor=W, width=130)
my_tree.column('3', anchor=W, width=130)
my_tree.column('4', anchor=W, width=130)
my_tree.column('5', anchor=W, width=150)

my_tree.heading('1', text="employee Name", anchor=W)
my_tree.heading('2', text="employee Age", anchor=W)
my_tree.heading('3', text="employee Phone", anchor=W)
my_tree.heading('4', text="employee ID", anchor=W)
my_tree.heading('5', text="employee Shift", anchor=W)

myTag='normal'

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    if(myTag=='grey'):
        myTag='normal'
    else:
        myTag='grey'
    my_tree.insert("",'end', iid=result, text="", values=(result), tag=(myTag))

my_tree.tag_configure('grey', background='lightgrey', font=labelFont)
my_tree.tag_configure('normal', background='white', font=labelFont)
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()
