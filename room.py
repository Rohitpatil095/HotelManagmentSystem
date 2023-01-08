from logging import exception
from tkinter import *
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class roomDetails:                                        
    def __init__(self, roomWindow):
        self.roomWindow = roomWindow
        self.roomWindow.title("Hotel Admin Settings")
        self.roomWindow.geometry("1150x513+210+220") 


        ############################# Title ##########################
        customerWinTxt = Label(self.roomWindow,text="ROOM DETAILS", font=("times new roman" ,20, "bold"), bg="black", fg="pink", bd=4, relief=RIDGE)
        customerWinTxt.place(x=0, y=0, height=40, width=1150)

        ############################# Title ##########################
        custFrame= LabelFrame(self.roomWindow, bd=2, relief=RIDGE ,text="ROOM Details", font=("times new roman",15, "bold"), padx=2, pady=5)
        custFrame.place(x=0, y=40, height=510, width=340)


        ##################### Variables Declare #########################
        self.cust_contact = StringVar()
        self.cust_checkin = StringVar()
        self.cust_checkout = StringVar()
        self.cust_roomtype = StringVar()
        self.cust_roomavailable = StringVar()
        self.cust_meal = StringVar()
        self.cust_noofdays = StringVar()
        self.cust_paidtax = StringVar()
        self.cust_actualtotal = StringVar()
        self.cust_total = StringVar()

        ############################# Labels And Entry ##########################

        #cust contact
        custRefTxt = Label(custFrame,text="Customer Contact", font=("arial" ,12, "bold"), padx=2, pady=5)
        custRefTxt.grid(row=0, column=0, sticky=W)
        custRefeEntry = ttk.Entry(custFrame, textvariable=self.cust_contact,font=("arial", 13,"bold"), width=12 )
        custRefeEntry.grid(row=0, column=1,sticky=W)

        # Fetch Data button
        addButton = Button(custFrame,command=self.fetch_contact, text="Fetch", font=("Arial",13, "bold"), bg= "black", fg="pink", width=5)
        addButton.place(x=270, y=1  )

        # cust checkin date
        custNameTxt = Label(custFrame,text="Check_in Date", font=("arial" ,12, "bold"), padx=2, pady=5)
        custNameTxt.grid(row=1, column=0, sticky=W)
        custNameEntry = ttk.Entry(custFrame,textvariable=self.cust_checkin, font=("arial", 13,"bold"), width=20)
        custNameEntry.grid(row=1, column=1)

        #cust check out date
        motherNameTxt = Label(custFrame,text="Check_out Date", font=("arial" ,12, "bold"), padx=2, pady=5)
        motherNameTxt.grid(row=2, column=0, sticky=W)
        motherNameEntry = ttk.Entry(custFrame, textvariable=self.cust_checkout,font=("arial", 13,"bold"), width=20)
        motherNameEntry.grid(row=2, column=1)

        #Room Type
        genderTxt = Label(custFrame,text="Room Type", font=("arial" ,12, "bold"), padx=2, pady=5)
        genderTxt.grid(row=3, column=0, sticky=W)
        genderSelect = ttk.Combobox(custFrame,textvariable=self.cust_roomtype,font=("arial" ,13, "bold"), width=18, state="readonly")
        genderSelect["values"] = ("Single", "Double", "Luxury")
        genderSelect.current(0)
        genderSelect.grid(row=3, column=1)
    

        #available rooms 
        postcodeTxt = Label(custFrame,text="Available Rooms", font=("arial" ,12, "bold"), padx=2, pady=5)
        postcodeTxt.grid(row=4, column=0, sticky=W)
        postcodeEntry = ttk.Entry(custFrame, textvariable=self.cust_roomavailable,font=("arial", 13,"bold"), width=20)
        postcodeEntry.grid(row=4, column=1)

        #Meal
        mobileTxt = Label(custFrame,text="Meal", font=("arial" ,12, "bold"), padx=2, pady=5)
        mobileTxt.grid(row=5, column=0, sticky=W)
        mobileEntry = ttk.Entry(custFrame,textvariable=self.cust_meal, font=("arial", 13,"bold"), width=20)
        mobileEntry.grid(row=5, column=1)

        #num of days
        emailTxt = Label(custFrame,text="Num Of Days", font=("arial" ,12, "bold"), padx=2, pady=5)
        emailTxt.grid(row=6, column=0, sticky=W)
        emailEntry = ttk.Entry(custFrame, textvariable=self.cust_noofdays,font=("arial", 13,"bold"), width=20)
        emailEntry.grid(row=6, column=1)

        #tax paid
        nationalityTxt = Label(custFrame,text="Paid Tax", font=("arial" ,12, "bold"), padx=2, pady=5)
        nationalityTxt.grid(row=7, column=0, sticky=W)
        nationalitySelect = ttk.Entry(custFrame,textvariable=self.cust_paidtax,font=("arial" ,13, "bold"), width=20)
        nationalitySelect.grid(row=7, column=1)
        

        #sub total
        idTxt = Label(custFrame,text="Sub Total", font=("arial" ,12, "bold"), padx=2, pady=5)
        idTxt.grid(row=8, column=0, sticky=W)
        IDSelect = ttk.Entry(custFrame, textvariable=self.cust_actualtotal, font=("arial" ,13, "bold"), width=20)
        IDSelect.grid(row=8, column=1)
        

        #Total Cost
        idnumTxt = Label(custFrame,text="Total Cos", font=("arial" ,12, "bold"), padx=2, pady=5)
        idnumTxt.grid(row=9, column=0, sticky=W)
        idnumEntry = ttk.Entry(custFrame,textvariable=self.cust_total,font=("arial", 13,"bold"), width=20)
        idnumEntry.grid(row=9, column=1)


        ################ Bill BUTTON ####################
        billButton = Button(custFrame, text="Bill", font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        billButton.grid(row=10 ,column=0 ,padx=1, sticky=W)

        ################ ADD DELETE UPDATE BUTTONS####################
        buttonFrame = Frame(custFrame, bd=4, relief=RIDGE)
        buttonFrame.place(x=0, y=370 , height=30, width=490)

        # Add button
        addButton = Button(buttonFrame,command=self.add_details, text="Add", font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        addButton.grid(row=0 ,column=0 ,padx=1)

        # Delete Button
        deleteButton = Button(buttonFrame,text="Delete", font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        deleteButton.grid(row=0 ,column=1,padx=1)

        #Update Button
        updateButton = Button(buttonFrame, command=self.update_data,text="Update", font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        updateButton.grid(row=0 ,column=2,padx=1)

        #Reset Button
        resetButton = Button(buttonFrame ,text="Reset", font=("Arial",13, "bold"), bg= "black", fg="pink", width=7)
        resetButton.grid(row=0 ,column=3,padx=1)

        ########################### tABLE TO SHOW DETAILS ####################
        TableFrame= LabelFrame(self.roomWindow, bd=2, relief=RIDGE ,text="View Details And Search System", font=("arial",15, "bold"), padx=2, pady=5)
        TableFrame.place(x=350, y=250, height=250, width=785)

        #Search By 

        self.search_var= StringVar()

        searchByTxt = Label(TableFrame,text="Search By", font=("arial" ,12, "bold"),bg="green", fg='white')
        searchByTxt.grid(row=0, column=0, sticky=W, padx=2)

        selectBy = ttk.Combobox(TableFrame,  textvariable=self.search_var , font=("arial" ,13, "bold"), width=18, state="readonly")
        selectBy["values"] = ("Contact", "Room")
        selectBy.current(0)
        selectBy.grid(row=0, column=1, padx=2)

        self.search_text = StringVar()
        searchBytxt = ttk.Entry(TableFrame,textvariable=self.search_text, font=("arial", 13,"bold"), width=20)
        searchBytxt.grid(row=0, column=2, padx=2)
        
        #Search  Button
        updateButton = Button(TableFrame,text="Search", font=("Arial",13, "bold"), bg= "black", fg="pink", height=1, width=7)
        updateButton.grid(row=0 ,column=3,padx=1)

        #Show All Button
        resetButton = Button(TableFrame, text="Show All", font=("Arial",13, "bold"), bg= "black", fg="pink", height=1, width=7)
        resetButton.grid(row=0 ,column=4,padx=1)


        ########################### tABLE TO SHOW ALL DETAILS ####################
        showDetailsFrame= Frame(TableFrame, bd=2, relief=RIDGE, bg="black")
        showDetailsFrame.place(x=0, y=50, height=150, width=785)

        scrollX = Scrollbar(showDetailsFrame, orient=HORIZONTAL)
        scrollY = Scrollbar(showDetailsFrame, orient=VERTICAL)

        self.roomDetailsTable = ttk.Treeview(showDetailsFrame, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable","meal","noofdays"), xscrollcommand=scrollX.set, yscrollcommand= scrollY.set)

        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        scrollX.config(command=self.roomDetailsTable.xview)
        scrollY.config(command=self.roomDetailsTable.yview)

        self.roomDetailsTable.heading("contact", text="Contact No")
        self.roomDetailsTable.heading("checkin", text="Check In")
        self.roomDetailsTable.heading("checkout", text="Check Out")
        self.roomDetailsTable.heading("roomtype", text="Room Type")
        self.roomDetailsTable.heading("roomavailable", text="Available Rooms")
        self.roomDetailsTable.heading("meal", text="Meal")
        self.roomDetailsTable.heading("noofdays", text="No Of Days")

        self.roomDetailsTable["show"]= "headings"

        self.roomDetailsTable.column("contact", width=100)
        self.roomDetailsTable.column("checkin", width=100)
        self.roomDetailsTable.column("checkout", width=100)
        self.roomDetailsTable.column("roomtype", width=100)
        self.roomDetailsTable.column("roomavailable", width=100)
        self.roomDetailsTable.column("meal", width=100)

        self.roomDetailsTable.pack(fill=BOTH,  expand=1)
        self.roomDetailsTable.bind("<Button-1>", self.get_cursor)

        self.fetch_data() 

    ############### Add data #########################
    def add_details(self):
        if self.cust_contact.get() =="" or self.cust_checkin.get() =="":
            messagebox.showerror("Error","Fields Cannot Be Left Empty" ,parent=self.custWindow)
        else:
            try:
                newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
                newCursor= newConnector.cursor()
                newCursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.cust_contact.get(),
                                                                                        self.cust_checkin.get(),
                                                                                        self.cust_checkout.get(),
                                                                                        self.cust_roomtype.get(),
                                                                                        self.cust_roomavailable.get(),
                                                                                        self.cust_meal.get(),
                                                                                        self.cust_noofdays.get()
                                                                                ))
                                                                                       
                newConnector.commit()
                self.fetch_data()
                newConnector.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.custWindow)

            except Exception as e:
                messagebox.showerror("Error", f"Something Went Wrong {str(e)}", parent = self.custWindow)

    def fetch_data(self):
        newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
        newCursor= newConnector.cursor()
        newCursor.execute("select * from room")
        rows = newCursor.fetchall()

        if len(rows) !=0:
            self.roomDetailsTable.delete(*self.roomDetailsTable.get_children())
            for o in rows:
                self.roomDetailsTable.insert("",END,values=o)
                newConnector.commit()
        newConnector.close()


    def get_cursor(self,event=""):
        cursor_row = self.roomDetailsTable.focus()
        content = self.roomDetailsTable.item(cursor_row)
        row = content["values"]

        self.cust_contact.set(row[0])
        self.cust_checkin.set(row[1])
        self.cust_checkout.set(row[2])
        self.cust_roomtype.set(row[3])
        self.cust_roomavailable.set(row[4])
        self.cust_meal.set(row[5])
        self.cust_noofdays.set(row[6])

        self.fetch_data()

    ############ Update Data #####################
    def update_data(self):
        if self.mobile.get() =="":
            messagebox.showerror("Error", "Mobile Number Field Cannot Be Left Empty", parent = self.custWindow)
        else:
            new_Connector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
            new_Cursor= new_Connector.cursor()
            new_Cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                self.check_in.get(),
                                                self.check_out.get(),
                                                self.roomtype.get(),
                                                self.roomavailable.get(),
                                                self.meal.get(),
                                                self.noOfdays.get(),
                                                self.Contact.get()
                                                ))
            new_Connector.commit()
            self.fetch_data()
            new_Connector.close()
            messagebox.showinfo("Update","Room Details Updated Successfully")


    ############## Fetching data from mobile num ###################  
    def fetch_contact(self):
        if(self.cust_contact.get() ==""):
            messagebox.showerror("Error", "Please Enter Mobile Number",parent= self.roomWindow)
        else:
            newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
            newCursor= newConnector.cursor()
            query =("select Name from customer where Mobile=%s")
            value= (self.cust_contact.get(),)
            newCursor.execute(query, value)
            row = newCursor.fetchone()

            if(row==0):
                messagebox.showerror("Error","Please Enter A Valid Number",parent=self.roomWindow)
            else:
                newConnector.commit()
                newConnector.close()

                showRoomDataFrame =Frame(self.roomWindow, bd=3,relief=RIDGE, padx=1)
                showRoomDataFrame.place(x=355,y=49, width=785, height=189)

                #Name data
                roomLable = Label(showRoomDataFrame, text="Name", font=("arial", 12, "bold"))
                roomLable.place(x=0,y=0)
                
                roomData =Label(showRoomDataFrame, text=row, font=("aerial", 12, "bold"))
                roomData.place(x=75,y=0)

                #Gender data
                newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
                newCursor= newConnector.cursor()
                query =("select Gender from customer where Mobile=%s")
                value= (self.cust_contact.get(),)
                newCursor.execute(query, value)
                row = newCursor.fetchone()

                roomLable = Label(showRoomDataFrame, text="Gender", font=("arial", 12, "bold"))
                roomLable.place(x=0,y=30)
                
                roomData =Label(showRoomDataFrame, text=row, font=("aerial", 12, "bold"))
                roomData.place(x=75,y=30)
                
                #Email data
                newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
                newCursor= newConnector.cursor()
                query =("select Email from customer where Mobile=%s")
                value= (self.cust_contact.get(),)
                newCursor.execute(query, value)
                row = newCursor.fetchone()

                roomLable = Label(showRoomDataFrame, text="Email Id", font=("arial", 12, "bold"))
                roomLable.place(x=0,y=60)
                
                roomData =Label(showRoomDataFrame, text=row, font=("arial", 12, "bold"))
                roomData.place(x=75,y=60)
                
                #Nationality data
                newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
                newCursor= newConnector.cursor()
                query =("select Nationality from customer where Mobile=%s")
                value= (self.cust_contact.get(),)
                newCursor.execute(query, value)
                row = newCursor.fetchone()

                roomLable = Label(showRoomDataFrame, text="Nationality", font=("arial", 12, "bold"))
                roomLable.place(x=0,y=90)
                
                roomData =Label(showRoomDataFrame, text=row, font=("aerial", 12, "bold"))
                roomData.place(x=75,y=90)

                #Address data
                newConnector= mysql.connector.connect(host = "localhost", username= "root", password="root", database="hotelmanagment")
                newCursor= newConnector.cursor()
                query =("select Address from customer where Mobile=%s")
                value= (self.cust_contact.get(),)
                newCursor.execute(query, value)
                row = newCursor.fetchone()

                roomLable = Label(showRoomDataFrame, text="Address", font=("arial", 12, "bold"))
                roomLable.place(x=0,y=120)
                
                roomData =Label(showRoomDataFrame, text=row, font=("aerial", 12, "bold"))
                roomData.place(x=75,y=120)
            





if __name__ == "__main__":
    roomWindow = Tk()
    custWindowObj = roomDetails(roomWindow)
    roomWindow.mainloop()
        