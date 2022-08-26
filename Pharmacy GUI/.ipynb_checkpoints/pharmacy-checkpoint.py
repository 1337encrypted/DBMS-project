from tkinter import *
from tkinter import ttk
import sqlite3
from connection import dbConnect
#from customer import *
#from doctor import *
#from drug import *
#from employee import *
#from supplier import *
#from manufacturer import *
#from warehouse import *

class pharmacyManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1535x1000+0+0")

        # -------------------------DBVariables-----------------------

        self.buttonColor = "red"
        self.textColor = "red"
        
        lableTitle = Label(self.root, text=" PHARMACY MANAGEMENT SYSTEM ", bd=15, relief=RIDGE, bg='white',
                           fg="darkgreen", font=("times now roman", 50, "bold"), padx=2, pady=4)
        lableTitle.pack(side=TOP, fill=X)

        # ------------------------DataFrame-----------------------

        dataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=2, pady=4)
        dataFrame.place(x=0, y=120, height=550, width=1535)

        # ------------------------ChangesFrame----------------------

        changesFrame = LabelFrame(dataFrame, text="CHANGES", bd=15, relief=RIDGE, padx=2, pady=4,
                                  font=("arial", 12, "bold"), fg="darkgreen")
        changesFrame.place(x=0, y=0, height=516, width=750)


        # -----------------------ChangesFrameLabels-----------------
        #EmployeeChanges
        
        #=================================insert function=======================================
        
            
        
        def employee():
            # destroys all widgets in previously opened frame
            for widget in changesFrame.winfo_children():
                widget.destroy()

            addNameemployee = StringVar()
            addAgeemployee = IntVar()
            addPhoneemployee = StringVar()
            addIDemployee = IntVar()
            addShifTimeemployee = StringVar()

            def EmployeeInsert():
                try:
                    con = connector.connect(host='localhost', port='3306', user='root', password='root', database='pharmacydb')
                    cur = con.cursor()
                    print(con)
                except:
                    print("Dbconnect error")
                    
                query = "insert into employee(name,age,ph_no,employee_id,shift_time) values(addNameemployee.get(),int(addAgeemployee.get()),addPhoneemployee.get(),int(addIDemployee.get()),addShifTimeemployee.get()));"
                
                cur.execute(query)
                con.commmit()

            #Name
            labelName = Label(changesFrame, text="Name:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelName.grid(row=0, column=0)
            entryName = Entry(changesFrame,textvariable=addNameemployee, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryName.grid(row=0, column=1)

            #Phone
            labelPhone = Label(changesFrame, text="Phone No:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelPhone.grid(row=1, column=0)
            entryPhone = Entry(changesFrame,textvariable=addPhoneemployee, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryPhone.grid(row=1, column=1)


            # Age
            labelAge = Label(changesFrame, text="Age:", font=("arial", 12, "bold"), bg="blue", fg="white",
                                 width=10, height=1)
            labelAge.grid(row=2, column=0)
            entryAge = Entry(changesFrame,textvariable=addAgeemployee, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryAge.grid(row=2, column=1)

            #ID
            labelID = Label(changesFrame, text="Employee ID:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelID.grid(row=3, column=0)
            entryID = Entry(changesFrame, textvariable=addIDemployee, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryID.grid(row=3, column=1)

            #Shift
            labelShift = Label(changesFrame, text="Shift Time:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelShift.grid(row=4, column=0)
            entryShift = Entry(changesFrame, textvariable=addShifTimeemployee, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryShift.grid(row=4, column=1)
            
            

            #FunctionButtons

            insertEmployee = Button(changesFrame, text="Insert", font=("arial", 12, "bold"), bg="darkgreen",fg="white",width=10, command=EmployeeInsert)
            insertEmployee.grid(row=5, column=0)



            deleteEmployee = Button(changesFrame, text="Delete", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            deleteEmployee.grid(row=5, column=1)

            updateEmployee = Button(changesFrame, text="Update", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            updateEmployee.grid(row=5, column=2)

        #EmployeeTreeView
        def employeeTreeView():
            displayTableFrame = LabelFrame(displayFrame, bd=15, relief=RIDGE)
            displayTableFrame.place(x=0, y=0, height=475, width=715)

            scroll_x = ttk.Scrollbar(displayTableFrame, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y = ttk.Scrollbar(displayTableFrame, orient=VERTICAL)
            scroll_y.pack(side=RIGHT, fill=Y)

            self.employeeTable = ttk.Treeview(displayTableFrame, columns=("Name", "Phone", "Age", "ID", "Shift"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=self.employeeTable.xview)
            scroll_y.config(command=self.employeeTable.yview)

            self.employeeTable["show"] = "headings"

            self.employeeTable.heading("Name", text="Name")
            self.employeeTable.heading("Phone", text="Phone")
            self.employeeTable.heading("Age", text="Age")
            self.employeeTable.heading("ID", text="ID")
            self.employeeTable.heading("Shift", text="Shift")
            self.employeeTable.pack(fill=BOTH,expand=1)

        #CustomerChanges
        def customer():
            # destroys all widgets in previously opened frame
            for widget in changesFrame.winfo_children():
                widget.destroy()

            #Name
            labelName = Label(changesFrame, text="Name:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelName.grid(row=0, column=0)
            entryName = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryName.grid(row=0, column=1)

            #Phone
            labelPhone = Label(changesFrame, text="Phone No:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelPhone.grid(row=1, column=0)
            entryPhone = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryPhone.grid(row=1, column=1)

            #Address
            labelAddress = Label(changesFrame, text="Address:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelAddress.grid(row=2, column=0)
            entryAddress = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryAddress.grid(row=2, column=1)

            #ID
            labelID = Label(changesFrame, text="Customer ID:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelID.grid(row=3, column=0)
            entryID = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryID.grid(row=3, column=1)

            #Gender
            labelGender = Label(changesFrame, text="Gender:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelGender.grid(row=4, column=0)
            entryGender = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryGender.grid(row=4, column=1)

            # FunctionButtons
            insertCustomer = Button(changesFrame, text="Insert", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            insertCustomer.grid(row=5, column=0)

            deleteCustomer = Button(changesFrame, text="Delete", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            deleteCustomer.grid(row=5, column=1)

            updateCustomer = Button(changesFrame, text="Update", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            updateCustomer.grid(row=5, column=2)

        #CustomerTreeView
        def customerTreeView():
            displayTableFrame = LabelFrame(displayFrame, bd=15, relief=RIDGE)
            displayTableFrame.place(x=0, y=0, height=475, width=715)

            scroll_x = ttk.Scrollbar(displayTableFrame, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y = ttk.Scrollbar(displayTableFrame, orient=VERTICAL)
            scroll_y.pack(side=RIGHT, fill=Y)

            self.customerTable = ttk.Treeview(displayTableFrame, columns=("Name", "Phone", "ID", "Gender"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=self.customerTable.xview)
            scroll_y.config(command=self.customerTable.yview)

            self.customerTable["show"] = "headings"

            self.customerTable.heading("Name", text="Name")
            self.customerTable.heading("Phone", text="Phone")
            self.customerTable.heading("ID", text="ID")
            self.customerTable.heading("Gender", text="Gender")
            self.customerTable.pack(fill=BOTH, expand=1)

        #DoctorChanges
        def doctor():
            # destroys all widgets in previously opened frame
            for widget in changesFrame.winfo_children():
                widget.destroy()

            #Name
            labelName = Label(changesFrame, text="Name:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelName.grid(row=0, column=0)
            entryName = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryName.grid(row=0, column=1)

            # Age
            labelAge = Label(changesFrame, text="Age:", font=("arial", 12, "bold"), bg="blue", fg="white",
                                 width=10, height=1)
            labelAge.grid(row=1, column=0)
            entryAge = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryAge.grid(row=1, column=1)

            #Phone
            labelPhone = Label(changesFrame, text="Phone No:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelPhone.grid(row=2, column=0)
            entryPhone = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryPhone.grid(row=2, column=1)

            #Licence
            labelLicence = Label(changesFrame, text="Licence:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelLicence.grid(row=3, column=0)
            entryLicence = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryLicence.grid(row=3, column=1)

            #Clinci Address
            labelClinicAddress = Label(changesFrame, text="Address:", font=("arial", 12, "bold"), bg="blue", fg="white",
                                 width=10, height=1)
            labelClinicAddress.grid(row=4, column=0)
            entryClinicAddress = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryClinicAddress.grid(row=4, column=1)

            # FunctionButtons
            insertDoctor = Button(changesFrame, text="Insert", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            insertDoctor.grid(row=5, column=0)

            deleteDoctor = Button(changesFrame, text="Delete", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            deleteDoctor.grid(row=5, column=1)

            updateDoctor = Button(changesFrame, text="Update", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            updateDoctor.grid(row=5, column=2)

        #DoctorTreeView
        def doctorTreeView():
            displayTableFrame = LabelFrame(displayFrame, bd=15, relief=RIDGE)
            displayTableFrame.place(x=0, y=0, height=475, width=715)

            scroll_x = ttk.Scrollbar(displayTableFrame, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y = ttk.Scrollbar(displayTableFrame, orient=VERTICAL)
            scroll_y.pack(side=RIGHT, fill=Y)

            self.doctorTable = ttk.Treeview(displayTableFrame, columns=("Name", "Age", "Phone", "Licence", "ClinicAddress"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=self.doctorTable.xview)
            scroll_y.config(command=self.doctorTable.yview)

            self.doctorTable["show"] = "headings"

            self.doctorTable.heading("Name", text="Name")
            self.doctorTable.heading("Age", text="Age")
            self.doctorTable.heading("Phone", text="Phone")
            self.doctorTable.heading("Licence", text="Licence")
            self.doctorTable.heading("ClinicAddress", text="ClinicAddress")
            self.doctorTable.pack(fill=BOTH,expand=1)

        #WarehouseChanges
        def warehouse():
            #destroys all widgets in previously opened frame
            for widget in changesFrame.winfo_children():
                widget.destroy()

            # ID
            labelID = Label(changesFrame, text="Customer ID:", font=("arial", 12, "bold"), bg="blue", fg="white",
                            width=10, height=1)
            labelID.grid(row=0, column=0)
            entryID = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryID.grid(row=0, column=1)

            #Name
            labelName = Label(changesFrame, text="Name:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelName.grid(row=1, column=0)
            entryName = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryName.grid(row=1, column=1)

            #Location
            labelLocation = Label(changesFrame, text="Location:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelLocation.grid(row=2, column=0)
            entryLocation = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryLocation.grid(row=2, column=1)

            # FunctionButtons
            insertWarehouse = Button(changesFrame, text="Insert", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            insertWarehouse.grid(row=3, column=0)

            deleteWarehouse = Button(changesFrame, text="Delete", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            deleteWarehouse.grid(row=3, column=1)

            updateWarehouse = Button(changesFrame, text="Update", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            updateWarehouse.grid(row=3, column=2)

        #WarehouseTreeView
        def warehouseTreeView():
            displayTableFrame = LabelFrame(displayFrame, bd=15, relief=RIDGE)
            displayTableFrame.place(x=0, y=0, height=475, width=715)

            scroll_x = ttk.Scrollbar(displayTableFrame, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y = ttk.Scrollbar(displayTableFrame, orient=VERTICAL)
            scroll_y.pack(side=RIGHT, fill=Y)

            self.warehouseTable = ttk.Treeview(displayTableFrame, columns=("ID", "Name", "Location"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=self.warehouseTable.xview)
            scroll_y.config(command=self.warehouseTable.yview)

            self.warehouseTable["show"] = "headings"

            self.warehouseTable.heading("ID", text="ID")
            self.warehouseTable.heading("Name", text="Name")
            self.warehouseTable.heading("Location", text="Location")
            self.warehouseTable.pack(fill=BOTH,expand=1)

        #DrugChanges
        def drug():
            # destroys all widgets in previously opened frame
            for widget in changesFrame.winfo_children():
                widget.destroy()

            #Name
            labelName = Label(changesFrame, text="Name:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelName.grid(row=0, column=0)
            entryName = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryName.grid(row=0, column=1)

            #Cost
            labelCost = Label(changesFrame, text="Cost:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelCost.grid(row=1, column=0)
            entryCost = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryCost.grid(row=1, column=1)

            #Type
            labelType = Label(changesFrame, text="Type:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelType.grid(row=2, column=0)
            entryType = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryType.grid(row=2, column=1)

            #Barcode
            labelBarcode = Label(changesFrame, text="Barcode:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelBarcode.grid(row=3, column=0)
            entryBarcode = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryBarcode.grid(row=3, column=1)

            #Manufacturing Date
            labelManufacturingDate = Label(changesFrame, text="Manufacturing Date:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelManufacturingDate.grid(row=4, column=0)
            entryManufacturingDate = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryManufacturingDate.grid(row=4, column=1)

            # Manufacturer Name
            labelManufacturerName = Label(changesFrame, text="Manufacturer Name:", font=("arial", 12, "bold"),
                                           bg="blue", fg="white",
                                           width=10, height=1)
            labelManufacturerName.grid(row=5, column=0)
            entryManufacturerName = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryManufacturerName.grid(row=5, column=1)

            # Expiry Date
            labelExpiryDate = Label(changesFrame, text="Expiry Date:", font=("arial", 12, "bold"),
                                           bg="blue", fg="white",
                                           width=10, height=1)
            labelExpiryDate.grid(row=6, column=0)
            entryExpiryDate = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryExpiryDate.grid(row=6, column=1)

            # FunctionButtons
            insertDrug = Button(changesFrame, text="Insert", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            insertDrug.grid(row=7, column=0)

            deleteDrug = Button(changesFrame, text="Delete", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            deleteDrug.grid(row=7, column=1)

            updateDrug = Button(changesFrame, text="Update", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            updateDrug.grid(row=7, column=2)

        #DrugeTreeView
        def drugTreeView():
            displayTableFrame = LabelFrame(displayFrame, bd=15, relief=RIDGE)
            displayTableFrame.place(x=0, y=0, height=475, width=715)

            scroll_x = ttk.Scrollbar(displayTableFrame, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y = ttk.Scrollbar(displayTableFrame, orient=VERTICAL)
            scroll_y.pack(side=RIGHT, fill=Y)

            self.drugTable = ttk.Treeview(displayTableFrame, columns=("Name", "Cost", "Type", "Barcode", "ManufacturingDate", "ManufacturerName", "ExpiryDate"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=self.drugTable.xview)
            scroll_y.config(command=self.drugTable.yview)

            self.drugTable["show"] = "headings"

            self.drugTable.heading("Name", text="Name")
            self.drugTable.heading("Cost", text="Cost")
            self.drugTable.heading("Type", text="Type")
            self.drugTable.heading("Barcode", text="Barcode")
            self.drugTable.heading("ManufacturingDate", text="ManufacturingDate")
            self.drugTable.heading("ManufacturerName", text="ManufacturerName")
            self.drugTable.heading("ExpiryDate", text="ExpiryDate")
            self.drugTable.pack(fill=BOTH, expand=1)

        #ManufacturerChanges
        def manufacturer():
            # destroys all widgets in previously opened frame
            for widget in changesFrame.winfo_children():
                widget.destroy()

            # Name
            labelName = Label(changesFrame, text="Name:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelName.grid(row=0, column=0)
            entryName = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryName.grid(row=0, column=1)

            # Address
            labelAddress = Label(changesFrame, text="Address:", font=("arial", 12, "bold"), bg="blue", fg="white",
                                 width=10, height=1)
            labelAddress.grid(row=1, column=0)
            entryAddress = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryAddress.grid(row=1, column=1)

            # Licence
            labelLicence = Label(changesFrame, text="Licence:", font=("arial", 12, "bold"), bg="blue", fg="white",
                                 width=10, height=1)
            labelLicence.grid(row=2, column=0)
            entryLicence = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryLicence.grid(row=2, column=1)

            # FunctionButtons
            insertManufacturer = Button(changesFrame, text="Insert", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            insertManufacturer.grid(row=3, column=0)

            deleteManufacturer = Button(changesFrame, text="Delete", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            deleteManufacturer.grid(row=3, column=1)

            updateManufacturer = Button(changesFrame, text="Update", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            updateManufacturer.grid(row=3, column=2)

        #ManufacturerTreeView
        def manufacturerTreeView():
            displayTableFrame = LabelFrame(displayFrame, bd=15, relief=RIDGE)
            displayTableFrame.place(x=0, y=0, height=475, width=715)

            scroll_x = ttk.Scrollbar(displayTableFrame, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y = ttk.Scrollbar(displayTableFrame, orient=VERTICAL)
            scroll_y.pack(side=RIGHT, fill=Y)

            self.manufacturerTable = ttk.Treeview(displayTableFrame, columns=("Name", "Address", "Licence"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=self.manufacturerTable.xview)
            scroll_y.config(command=self.manufacturerTable.yview)

            self.manufacturerTable["show"] = "headings"

            self.manufacturerTable.heading("Name", text="Name")
            self.manufacturerTable.heading("Address", text="Address")
            self.manufacturerTable.heading("Licence", text="Licence")
            self.manufacturerTable.pack(fill=BOTH, expand=1)

        #SupplierChanges
        def supplier():
            # destroys all widgets in previously opened frame
            for widget in changesFrame.winfo_children():
                widget.destroy()

            # Name
            labelName = Label(changesFrame, text="Name:", font=("arial", 12, "bold"), bg="blue", fg="white",
                              width=10, height=1)
            labelName.grid(row=0, column=0)
            entryName = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryName.grid(row=0, column=1)

            # Address
            labelAddress = Label(changesFrame, text="Address:", font=("arial", 12, "bold"), bg="blue", fg="white",
                                 width=10, height=1)
            labelAddress.grid(row=1, column=0)
            entryAddress = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryAddress.grid(row=1, column=1)

            # Licence
            labelLicence = Label(changesFrame, text="Licence:", font=("arial", 12, "bold"), bg="blue", fg="white",
                                 width=10, height=1)
            labelLicence.grid(row=2, column=0)
            entryLicence = Entry(changesFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            entryLicence.grid(row=2, column=1)

            # FunctionButtons
            insertSupplier = Button(changesFrame, text="Insert", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            insertSupplier.grid(row=3, column=0)

            deleteSupplier = Button(changesFrame, text="Delete", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            deleteSupplier.grid(row=3, column=1)

            updateSupplier = Button(changesFrame, text="Update", font=("arial", 12, "bold"), bg="darkgreen",
                                    fg="white",
                                    width=10)
            updateSupplier.grid(row=3, column=2)

        #SupplierTreeView
        def supplierTreeView():
            displayTableFrame = LabelFrame(displayFrame, bd=15, relief=RIDGE)
            displayTableFrame.place(x=0, y=0, height=475, width=715)

            scroll_x = ttk.Scrollbar(displayTableFrame, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y = ttk.Scrollbar(displayTableFrame, orient=VERTICAL)
            scroll_y.pack(side=RIGHT, fill=Y)

            self.supplierTable = ttk.Treeview(displayTableFrame, columns=("Name", "Address", "Licence"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=self.supplierTable.xview)
            scroll_y.config(command=self.supplierTable.yview)

            self.supplierTable["show"] = "headings"

            self.supplierTable.heading("Name", text="Name")
            self.supplierTable.heading("Address", text="Address")
            self.supplierTable.heading("Licence", text="Licence")
            self.supplierTable.pack(fill=BOTH, expand=1)

        # --------------------------------SearchBy------------------------

        # EmployeeSearchBy
        def employeeSearchBY():
            labelSearch = Label(buttonFrame, text="Search By", font=("arial", 12, "bold"), bg="blue", fg="white",
                                    width=10,
                                    height=1)
            labelSearch.grid(row=0, column=8, sticky=W)

            searchCombo = ttk.Combobox(buttonFrame, width=10, font=("arial", 12, "bold"), state="readonly")
            searchCombo["values"] = ("name", "age", "phone", "id", "shift_time")
            searchCombo.grid(row=0, column=9)
            searchCombo.current(0)

            searchEntry = Entry(buttonFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            searchEntry.grid(row=0, column=10)

            buttonSearch = Button(buttonFrame, text="SEARCH", font=("arial", 12, "bold"), bg="blue", fg="white",
                                      width=10)
            buttonSearch.grid(row=0, column=11)

            buttonSearchAll = Button(buttonFrame, text="SEARCH ALL", font=("arial", 12, "bold"), bg="blue", fg="white",
                                         width=10)
            buttonSearchAll.grid(row=0, column=12)

        #CustomerSearchBy
        def customerSearchBY():
            labelSearch = Label(buttonFrame, text="Search By", font=("arial", 12, "bold"), bg="blue", fg="white",
                                    width=10,
                                    height=1)
            labelSearch.grid(row=0, column=8, sticky=W)

            searchCombo = ttk.Combobox(buttonFrame, width=10, font=("arial", 12, "bold"), state="readonly")
            searchCombo["values"] = ("name", "phone", "address", "id", "gender")
            searchCombo.grid(row=0, column=9)
            searchCombo.current(0)

            searchEntry = Entry(buttonFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            searchEntry.grid(row=0, column=10)

            buttonSearch = Button(buttonFrame, text="SEARCH", font=("arial", 12, "bold"), bg="blue", fg="white",
                                      width=10)
            buttonSearch.grid(row=0, column=11)

            buttonSearchAll = Button(buttonFrame, text="SEARCH ALL", font=("arial", 12, "bold"), bg="blue", fg="white",
                                         width=10)
            buttonSearchAll.grid(row=0, column=12)

        #DoctorSearchBy
        def doctorSearchBY():
            labelSearch = Label(buttonFrame, text="Search By", font=("arial", 12, "bold"), bg="blue", fg="white",
                                    width=10,
                                    height=1)
            labelSearch.grid(row=0, column=8, sticky=W)

            searchCombo = ttk.Combobox(buttonFrame, width=10, font=("arial", 12, "bold"), state="readonly")
            searchCombo["values"] = ("name", "age", "phone", "licence")
            searchCombo.grid(row=0, column=9)
            searchCombo.current(0)

            searchEntry = Entry(buttonFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            searchEntry.grid(row=0, column=10)

            buttonSearch = Button(buttonFrame, text="SEARCH", font=("arial", 12, "bold"), bg="blue", fg="white",
                                      width=10)
            buttonSearch.grid(row=0, column=11)

            buttonSearchAll = Button(buttonFrame, text="SEARCH ALL", font=("arial", 12, "bold"), bg="blue", fg="white",
                                         width=10)
            buttonSearchAll.grid(row=0, column=12)

        #WarehouseSearchBy
        def warehouseSearchBY():
            labelSearch = Label(buttonFrame, text="Search By", font=("arial", 12, "bold"), bg="blue", fg="white",
                                    width=10,
                                    height=1)
            labelSearch.grid(row=0, column=8, sticky=W)

            searchCombo = ttk.Combobox(buttonFrame, width=10, font=("arial", 12, "bold"), state="readonly")
            searchCombo["values"] = ("id", "name", "location")
            searchCombo.grid(row=0, column=9)
            searchCombo.current(0)

            searchEntry = Entry(buttonFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            searchEntry.grid(row=0, column=10)

            buttonSearch = Button(buttonFrame, text="SEARCH", font=("arial", 12, "bold"), bg="blue", fg="white",
                                      width=10)
            buttonSearch.grid(row=0, column=11)

            buttonSearchAll = Button(buttonFrame, text="SEARCH ALL", font=("arial", 12, "bold"), bg="blue", fg="white",
                                         width=10)
            buttonSearchAll.grid(row=0, column=12)

        #DrugSearchBy
        def drugSearchBY():
            labelSearch = Label(buttonFrame, text="Search By", font=("arial", 12, "bold"), bg="blue", fg="white",
                                    width=10,
                                    height=1)
            labelSearch.grid(row=0, column=8, sticky=W)

            searchCombo = ttk.Combobox(buttonFrame, width=10, font=("arial", 12, "bold"), state="readonly")
            searchCombo["values"] = ("name", "type", "barcode", "manufacturing_date", "manufacturer_name", "expiry_date")
            searchCombo.grid(row=0, column=9)
            searchCombo.current(0)

            searchEntry = Entry(buttonFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            searchEntry.grid(row=0, column=10)

            buttonSearch = Button(buttonFrame, text="SEARCH", font=("arial", 12, "bold"), bg="blue", fg="white",
                                      width=10)
            buttonSearch.grid(row=0, column=11)

            buttonSearchAll = Button(buttonFrame, text="SEARCH ALL", font=("arial", 12, "bold"), bg="blue", fg="white",
                                         width=10)
            buttonSearchAll.grid(row=0, column=12)

        #manufacturerSearchBy
        def manufacturerSearchBy():
            labelSearch = Label(buttonFrame, text="Search By", font=("arial", 12, "bold"), bg="blue", fg="white",
                                width=10,
                                height=1)
            labelSearch.grid(row=0, column=8, sticky=W)

            searchCombo = ttk.Combobox(buttonFrame, width=10, font=("arial", 12, "bold"), state="readonly")
            searchCombo["values"] = ("name", "address", "licence")
            searchCombo.grid(row=0, column=9)
            searchCombo.current(0)

            searchEntry = Entry(buttonFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            searchEntry.grid(row=0, column=10)

            buttonSearch = Button(buttonFrame, text="SEARCH", font=("arial", 12, "bold"), bg="blue", fg="white",
                                  width=10)
            buttonSearch.grid(row=0, column=11)

            buttonSearchAll = Button(buttonFrame, text="SEARCH ALL", font=("arial", 12, "bold"), bg="blue", fg="white",
                                     width=10)
            buttonSearchAll.grid(row=0, column=12)

        #SupplierSearchBy
        def supplierSearchBy():
            labelSearch = Label(buttonFrame, text="Search By", font=("arial", 12, "bold"), bg="blue", fg="white",
                                width=10,
                                height=1)
            labelSearch.grid(row=0, column=8, sticky=W)

            searchCombo = ttk.Combobox(buttonFrame, width=10, font=("arial", 12, "bold"), state="readonly")
            searchCombo["values"] = ("name", "address", "licence")
            searchCombo.grid(row=0, column=9)
            searchCombo.current(0)

            searchEntry = Entry(buttonFrame, bd=3, relief=RIDGE, width=15, font=("arial", 12, "bold"))
            searchEntry.grid(row=0, column=10)

            buttonSearch = Button(buttonFrame, text="SEARCH", font=("arial", 12, "bold"), bg="blue", fg="white",
                                  width=10)
            buttonSearch.grid(row=0, column=11)

            buttonSearchAll = Button(buttonFrame, text="SEARCH ALL", font=("arial", 12, "bold"), bg="blue", fg="white",
                                     width=10)
            buttonSearchAll.grid(row=0, column=12)

        # ------------------------DisplayFrame----------------------

        displayFrame = LabelFrame(dataFrame, text="DISPLAY", bd=15, relief=RIDGE, padx=2, pady=4,
                                  font=("arial", 12, "bold"), fg="darkgreen")
        displayFrame.place(x=750, y=0, height=516, width=750)

        # -----------------------ButtonFrame----------------------

        buttonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=2, pady=4)
        buttonFrame.place(x=0, y=670, height=65, width=1535)

        # ----------------------FrameButton------------------------------------------

        buttonEmployee = Button(buttonFrame, text="EMPLOYEE", font=("arial", 12, "bold"), bg="darkgreen", fg=self.buttonColor,
                                width=10,command=lambda:[f() for f in [employee,employeeTreeView,employeeSearchBY]])
        buttonEmployee.grid(row=0, column=0)

        buttonCustomer = Button(buttonFrame, text="CUSTOMER", font=("arial", 12, "bold"), bg="darkgreen", fg=self.buttonColor,
                                width=10,command=lambda:[f() for f in [customer,customerTreeView,customerSearchBY]])
        buttonCustomer.grid(row=0, column=1)

        buttonDoctor = Button(buttonFrame, text="DOCTOR", font=("arial", 12, "bold"), bg="darkgreen", fg=self.buttonColor,
                              width=10,command=lambda:[f() for f in [doctor,doctorTreeView,doctorSearchBY]])
        buttonDoctor.grid(row=0, column=2)

        buttonDrug = Button(buttonFrame, text="DRUG", font=("arial", 12, "bold"), bg="darkgreen", fg=self.buttonColor, width=10,command=lambda:[f() for f in [drug,drugTreeView,drugSearchBY]])
        buttonDrug.grid(row=0, column=3)

        buttonWarehouse = Button(buttonFrame, text="WAREHOUSE", font=("arial", 12, "bold"), bg="darkgreen", fg=self.buttonColor,
                              width=10,command=lambda:[f() for f in [warehouse,warehouseTreeView,warehouseSearchBY]])
        buttonWarehouse.grid(row=0, column=4)

        buttonManufacturer = Button(buttonFrame, text="MANUFACTURER", font=("arial", 12, "bold"), bg=self.buttonColor,
                                    fg=self.buttonColor, width=14,command=lambda:[f() for f in [manufacturer,manufacturerTreeView,manufacturerSearchBy]])
        buttonManufacturer.grid(row=0, column=5)

        buttonSupplier = Button(buttonFrame, text="SUPPLIER", font=("arial", 12, "bold"), bg=self.buttonColor, fg=self.buttonColor,
                                width=10,command=lambda:[f() for f in [supplier,supplierTreeView,supplierSearchBy]])
        buttonSupplier.grid(row=0, column=6)

        buttonExit = Button(buttonFrame, command=root.destroy, text="EXIT", font=("arial", 12, "bold"), bg="red", fg=self.buttonColor, width=10)
        buttonExit.grid(row=0, column=7)


        # ------------------------DBConnection----------------------
        # ------InsertFunctions------
        def addEmployee(self):
            conn = sqlite3.connect("pharmacyDatabase.db")
            cur = conn.cursor()
            query = "INSERT INTO CUSTOMERS VALUES(?,?,?,?,?)"
            cur.execute(query,(self.addName.get(),self.addAge.get()))


if __name__ == "__main__":
    root = Tk()
    obj = pharmacyManagementSystem(root)
    root.mainloop()
