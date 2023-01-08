from logging import exception
from tkinter import *
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Customer_Window:                                         #main customer class
    def __init__(self, custWindow):
        self.custWindow = custWindow
        self.custWindow.title("Welcome To RTect Hotels")
        self.custWindow.geometry("1150x513+210+220") 


        ############################# Title ##########################
        customerWinTxt = Label(self.custWindow,text="CUSTOMER DETAILS", font=("times new roman" ,20, "bold"), bg="black", fg="pink", bd=4, relief=RIDGE)
        customerWinTxt.place(x=0, y=0, height=40, width=1150)

        ############################# Title ##########################
        custFrame= LabelFrame(self.custWindow, bd=2, relief=RIDGE ,text="Customer Details", font=("times new roman",15, "bold"), padx=2, pady=5)
        custFrame.place(x=0, y=40, height=510, width=340)


        ############################# Variables ##########################
        self.ref_num = StringVar()
        randomNum = random.randint(100,1000)
        self.ref_num.set(str(randomNum))

        self.cust_name = StringVar()
        self.mother_name = StringVar()
        self.gender = StringVar()
        self.post = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.nationality = StringVar()
        self.address = StringVar()
        self.id_proof = StringVar()
        self.id_num = StringVar()
        

        ############################# Labels And Entry ##########################

        #cust ref
        custRefTxt = Label(custFrame,text="Customer Ref", font=("arial" ,12, "bold"), padx=2, pady=5)
        custRefTxt.grid(row=0, column=0, sticky=W)
        custRefeEntry = ttk.Entry(custFrame, textvariable= self.ref_num, font=("arial", 13,"bold"), width=20 , state="readonly")
        custRefeEntry.grid(row=0, column=1)

        # cust name
        custNameTxt = Label(custFrame,text="Customer Name", font=("arial" ,12, "bold"), padx=2, pady=5)
        custNameTxt.grid(row=1, column=0, sticky=W)
        custNameEntry = ttk.Entry(custFrame, textvariable=self.cust_name, font=("arial", 13,"bold"), width=20)
        custNameEntry.grid(row=1, column=1)

        #mother name
        motherNameTxt = Label(custFrame,text="Mother Name", font=("arial" ,12, "bold"), padx=2, pady=5)
        motherNameTxt.grid(row=2, column=0, sticky=W)
        motherNameEntry = ttk.Entry(custFrame, textvariable= self.mother_name, font=("arial", 13,"bold"), width=20)
        motherNameEntry.grid(row=2, column=1)

        #Gender
        genderTxt = Label(custFrame,text="Gender", font=("arial" ,12, "bold"), padx=2, pady=5)
        genderTxt.grid(row=3, column=0, sticky=W)
        genderSelect = ttk.Combobox(custFrame, textvariable=self.gender ,font=("arial" ,13, "bold"), width=18, state="readonly")
        genderSelect["values"] = ("Male", "Female", "Other")
        genderSelect.current(0)
        genderSelect.grid(row=3, column=1)
    

        #mPost code 
        postcodeTxt = Label(custFrame,text="Post Code", font=("arial" ,12, "bold"), padx=2, pady=5)
        postcodeTxt.grid(row=4, column=0, sticky=W)
        postcodeEntry = ttk.Entry(custFrame, textvariable= self.post, font=("arial", 13,"bold"), width=20)
        postcodeEntry.grid(row=4, column=1)

        #Mobile
        mobileTxt = Label(custFrame,text="Mobile", font=("arial" ,12, "bold"), padx=2, pady=5)
        mobileTxt.grid(row=5, column=0, sticky=W)
        mobileEntry = ttk.Entry(custFrame, textvariable= self.mobile, font=("arial", 13,"bold"), width=20)
        mobileEntry.grid(row=5, column=1)

        #Email
        emailTxt = Label(custFrame,text="Email", font=("arial" ,12, "bold"), padx=2, pady=5)
        emailTxt.grid(row=6, column=0, sticky=W)
        emailEntry = ttk.Entry(custFrame, textvariable= self.email, font=("arial", 13,"bold"), width=20)
        emailEntry.grid(row=6, column=1)

        #Nationality
        nationalityTxt = Label(custFrame,text="Nationality", font=("arial" ,12, "bold"), padx=2, pady=5)
        nationalityTxt.grid(row=7, column=0, sticky=W)
        nationalitySelect = ttk.Combobox(custFrame, textvariable=self.nationality,font=("arial" ,13, "bold"), width=18, state="readonly")
        nationalitySelect["values"] = ("Indian", "Japan", "United States")
        nationalitySelect.current(0)
        nationalitySelect.grid(row=7, column=1)
        

        #ID Proof
        idTxt = Label(custFrame,text="Id Proof", font=("arial" ,12, "bold"), padx=2, pady=5)
        idTxt.grid(row=8, column=0, sticky=W)
        IDSelect = ttk.Combobox(custFrame, textvariable=self.id_proof, font=("arial" ,13, "bold"), width=18, state="readonly")
        IDSelect["values"] = ("Aadhar Card", "Passport", "Driving Liscence")
        IDSelect.current(0)
        IDSelect.grid(row=8, column=1)
        

        #Id Number
        idnumTxt = Label(custFrame,text="Id Number", font=("arial" ,12, "bold"), padx=2, pady=5)
        idnumTxt.grid(row=9, column=0, sticky=W)
        idnumEntry = ttk.Entry(custFrame,textvariable= self.id_num,font=("arial", 13,"bold"), width=20)
        idnumEntry.grid(row=9, column=1)

        #Address
        addressTxt = Label(custFrame,text="Address", font=("arial" ,12, "bold"), padx=2, pady=5)
        addressTxt.grid(row=10, column=0, sticky=W)
        addressEntry = ttk.Entry(custFrame, textvariable= self.address,font=("arial", 13,"bold"), width=20)
        addressEntry.grid(row=10, column=1)

        ################ ADD DELETE UPDATE BUTTONS####################
        buttonFrame = Frame(custFrame, bd=4, relief=RIDGE)
        buttonFrame.place(x=0, y=370 , height=30, width=490)

        # Add button
        addButton = Button(buttonFrame, text="Add", command=self.add_details, font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        addButton.grid(row=0 ,column=0 ,padx=1)

        # Delete Button
        deleteButton = Button(buttonFrame, command=self.deleteData,text="Delete", font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        deleteButton.grid(row=0 ,column=1,padx=1)

        #Update Button
        updateButton = Button(buttonFrame, command=self.update_data, text="Update", font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        updateButton.grid(row=0 ,column=2,padx=1)

        #Reset Button
        resetButton = Button(buttonFrame ,command=self.resetData,text="Reset", font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        resetButton.grid(row=0 ,column=3,padx=1)


        ########################### tABLE TO SHOW DETAILS ####################
        TableFrame= LabelFrame(self.custWindow, bd=2, relief=RIDGE ,text="View Details And Search System", font=("arial",15, "bold"), padx=2, pady=5)
        TableFrame.place(x=350, y=40, height=510, width=785)

        #Search By 

        self.search_var= StringVar()

        searchByTxt = Label(TableFrame,text="Search By", font=("arial" ,12, "bold"),bg="green", fg='white')
        searchByTxt.grid(row=0, column=0, sticky=W, padx=2)

        selectBy = ttk.Combobox(TableFrame,  textvariable=self.search_var , font=("arial" ,13, "bold"), width=18, state="readonly")
        selectBy["values"] = ("Ref", "Mobile", "Room")
        selectBy.current(0)
        selectBy.grid(row=0, column=1, padx=2)

        self.search_text = StringVar()
        searchBytxt = ttk.Entry(TableFrame,textvariable=self.search_text, font=("arial", 13,"bold"), width=20)
        searchBytxt.grid(row=0, column=2, padx=2)
        
        #Search  Button
        updateButton = Button(TableFrame, command=self.searchUser ,text="Search", font=("Arial",13, "bold"), bg= "black", fg="pink", height=1, width=7)
        updateButton.grid(row=0 ,column=3,padx=1)

        #Show All Button
        resetButton = Button(TableFrame, command=self.fetch_data, text="Show All", font=("Arial",13, "bold"), bg= "black", fg="pink", height=1, width=7)
        resetButton.grid(row=0 ,column=4,padx=1)

        ########################### tABLE TO SHOW ALL DETAILS ####################
        showDetailsFrame= Frame(TableFrame, bd=2, relief=RIDGE, bg="black")
        showDetailsFrame.place(x=0, y=50, height=345, width=785)

        scrollX = Scrollbar(showDetailsFrame, orient=HORIZONTAL)
        scrollY = Scrollbar(showDetailsFrame, orient=VERTICAL)

        self.customerDetailsTable = ttk.Treeview(showDetailsFrame, columns=("Ref", "Name", "Mother", "Gender", "Post","Mobile","Email", "Nationality", "IdProof", "IdNumber","Address"), xscrollcommand=scrollX.set, yscrollcommand= scrollY.set)

        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        scrollX.config(command=self.customerDetailsTable.xview)
        scrollY.config(command=self.customerDetailsTable.yview)

        self.customerDetailsTable.heading("Ref", text="Refer No")
        self.customerDetailsTable.heading("Name", text="Name")
        self.customerDetailsTable.heading("Mother", text="Mother Name")
        self.customerDetailsTable.heading("Gender", text="Gender")
        self.customerDetailsTable.heading("Post", text="Post")
        self.customerDetailsTable.heading("Mobile", text="Mobile No")
        self.customerDetailsTable.heading("Email", text="Email Id")
        self.customerDetailsTable.heading("Nationality", text="Nationality")
        self.customerDetailsTable.heading("IdProof", text="Id Proof")
        self.customerDetailsTable.heading("IdNumber", text="Id Number")
        self.customerDetailsTable.heading("Address", text="Address")

        self.customerDetailsTable["show"]= "headings"

        self.customerDetailsTable.column("Ref", width=100)
        self.customerDetailsTable.column("Name", width=100)
        self.customerDetailsTable.column("Mother", width=100)
        self.customerDetailsTable.column("Gender", width=100)
        self.customerDetailsTable.column("Post", width=100)
        self.customerDetailsTable.column("Mobile", width=100)
        self.customerDetailsTable.column("Email", width=100)
        self.customerDetailsTable.column("Nationality", width=100)
        self.customerDetailsTable.column("IdProof", width=100)
        self.customerDetailsTable.column("IdNumber", width=100)
        self.customerDetailsTable.column("Address", width=100)

        self.customerDetailsTable.pack(fill=BOTH,  expand=1)
        self.customerDetailsTable.bind("<Button-1>", self.get_cursor)
        self.fetch_data()


    def add_details(self):
        if self.ref_num.get() =="" or self.mobile.get() =="":
            messagebox.showerror("Error","Fields Cannot Be Left Empty" ,parent=self.custWindow)
        else:
            try:
                newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
                newCursor= newConnector.cursor()
                newCursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.ref_num.get(),
                            self.cust_name.get(),
                            self.mother_name.get(),
                            self.gender.get(),
                            self.post.get(),
                            self.mobile.get(),
                            self.email.get(),
                            self.nationality.get(),
                            self.id_proof.get(),
                            self.id_num.get(),
                            self.address.get()))

                newConnector.commit()
                self.fetch_data()
                newConnector.close()
                messagebox.showinfo("Success", "Guest Has Been Added", parent=self.custWindow)
            
            except Exception as e:
                messagebox.showerror("Error", f"Something Went Wrong {str(e)}", parent = self.custWindow)


    def fetch_data(self):
        newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
        newCursor= newConnector.cursor()
        newCursor.execute("select * from customer")
        rows = newCursor.fetchall()

        if len(rows) !=0:
            self.customerDetailsTable.delete(*self.customerDetailsTable.get_children())
            for o in rows:
                self.customerDetailsTable.insert("",END,values=o)
                newConnector.commit()
        newConnector.close()


    def get_cursor(self,event=""):
        cursor_row = self.customerDetailsTable.focus()
        content = self.customerDetailsTable.item(cursor_row)
        row = content["values"]

        self.ref_num.set(row[0]),
        self.cust_name.set(row[1]),
        self.mother_name.set(row[2]),
        self.gender.set(row[3]),
        self.post.set(row[4]),
        self.mobile.set(row[5]),
        self.email.set(row[6]),
        self.nationality.set(row[7]),
        self.id_proof.set(row[8]),
        self.id_num.set(row[9]),
        self.address.set(row[10])

      
    def update_data(self):
        if self.mobile.get() =="":
            messagebox.showerror("Error", "Mobile Number Filed Cannot Be Left Empty", parent = self.custWindow)
        else:
            new_Connector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
            new_Cursor= new_Connector.cursor()
            new_Cursor.execute("update customer set Name=%s, Mother=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s, Ref=%s",(
                                                self.cust_name.get(),
                                                self.mother_name.get(),
                                                self.gender.get(),
                                                self.post.get(),
                                                self.mobile.get(),
                                                self.email.get(),
                                                self.nationality.get(),
                                                self.id_proof.get(),
                                                self.id_num.get(),
                                                self.address.get(),
                                                self.ref_num.get() ))
            new_Connector.commit()
            self.fetch_data()
            new_Connector.close()
            messagebox.showinfo("Update","Information Updated Successfully")


    ################## Delete Data Function #########################

    def deleteData(self):
        deleteData =messagebox.askyesno("Admin Actions", "Delete User Data", parent = self.custWindow)

        if(deleteData>0):
            new_Connector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
            new_Cursor= new_Connector.cursor()
            query= ("delete from customer where Ref=%s")
            value= (self.ref_num.get(),)
            new_Cursor.execute(query,value)
        else:
            if not deleteData:
                return
        new_Connector.commit()
        self.fetch_data()
        new_Connector.close()

    def resetData(self):
        self.cust_name.set(""),
        self.mother_name.set(""),
        self.post.set(""),
        self.mobile.set(""),
        self.email.set(""),
        self.id_num.set(""),
        self.address.set("")

        randomNum = random.randint(100,1000)
        self.ref_num.set(str(randomNum))


    ############# Searching User ########################

    def searchUser(self):
        new_Connector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
        new_Cursor= new_Connector.cursor()
        new_Cursor.execute("select * from customer where"+str(self.search_var.get())+" LIKE '%"+str(self.search_text.get())+"%'")

        row= new_Cursor.fetchall()
        if len(row) !=0:
            self.customerDetailsTable.delete(*self.customerDetailsTable.get_children())
            for i in row:
                self.customerDetailsTable.insert("", END, values=i)
            new_Connector.commit()
        new_Connector.close()


if __name__ == "__main__":
    custWindow = Tk()
    custWindowObj = Customer_Window(custWindow)
    custWindow.mainloop()
        