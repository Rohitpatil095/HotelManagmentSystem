from tkinter import *                  # pip install tkinter 
from PIL import Image, ImageTk        # pip install pillow to use PIL. Both import handles images for tkinter
from customer import Customer_Window 
from room import roomDetails


class RTect:                                         #main hotel class
    def __init__(self, mWindow):
        self.mWindow = mWindow
        self.mWindow.title("Welcome To RTect Hotels")
        self.mWindow.geometry("1350x800+0+0")               # window size 1350x800 


        #############################Top Image##########################
        topImg= Image.open(r"F:\Rohit\Software\python\HotelManagmentSystem\Images\topimg.jpg")   #accesing topimg 
        topImg=topImg.resize((1350,150),Image.ANTIALIAS)                                          #antialias convert high grade img to low grade
        self.topimg = ImageTk.PhotoImage(topImg)
        topimgLabel = Label(self.mWindow, image=self.topimg, bd=4, relief=RIDGE)
        topimgLabel.place(x=0,y=0, width=1350, height=140)

        #############################Hotel Logo Image##########################
        logoImg= Image.open(r"F:\Rohit\Software\python\HotelManagmentSystem\Images\hotelLogo.png")  
        logoImg=logoImg.resize((300,150),Image.ANTIALIAS)                                          
        self.logoimg = ImageTk.PhotoImage(logoImg)
        logoimgLabel = Label(self.mWindow, image=self.logoimg, bd=4, relief=RIDGE)
        logoimgLabel.place(x=0,y=0, width=300, height=140)

        ############################# Title ##########################
        welcomeTxt = Label(self.mWindow,text="RTECT HOTEL MANAGMENT", font=("times new roman" ,30, "bold"), bg="black", fg="pink", bd=4, relief=RIDGE)
        welcomeTxt.place(x=0, y=150, height=40, width=1350)

        ############################# Main Frame ##########################
        mFrame = Frame(self.mWindow, bd=4, relief=RIDGE)
        mFrame.place(x=0, y= 190 , height=610, width=1350)

        ############################# Menu ##########################
        menuTxt = Label(mFrame,text="Menu", font=("times new roman" ,20, "bold"), bg="black", fg="pink", bd=4, relief=RIDGE)
        menuTxt.place(x=0, y=0, height=40, width=200)

        ############################# Menu Button Frame ##########################
        buttonFrame = Frame(mFrame, bd=4, relief=RIDGE)
        buttonFrame.place(x=0, y=40 , height=215, width=200)

        ############################# customer Button ##########################
        custButton =Button(buttonFrame, command=self.customerDetails,text="Customer", width=14, font=("times new roman" ,17, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        custButton.grid(row=0, column=0, pady=1)

        ############################# Room Button ##########################
        roomButton =Button(buttonFrame, command=self.roomInfo, text="Room", width=14, font=("times new roman" ,17, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        roomButton.grid(row=1, column=0, pady=1)

        ############################# Details Button ##########################
        detailButton =Button(buttonFrame, text="Details", width=14, font=("times new roman" ,17, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        detailButton.grid(row=2, column=0, pady=1)

        ############################# Report Button ##########################
        reportButton =Button(buttonFrame, text="Report", width=14, font=("times new roman" ,17, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        reportButton.grid(row=3, column=0, pady=1)

        ############################# Logout Button ##########################
        custButton =Button(buttonFrame, text="Logout", width=14, font=("times new roman" ,17, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        custButton.grid(row=4, column=0, pady=1)


        ############################# Center Image##########################
        centerImg= Image.open(r"F:\Rohit\Software\python\HotelManagmentSystem\Images\centerImg.jpg")  
        centerImg=  centerImg.resize((1130,550),Image.ANTIALIAS)                                          
        self.centerimg = ImageTk.PhotoImage(centerImg)
        centerimgLabel = Label(mFrame, image=self.centerimg, bd=4, relief=RIDGE)
        centerimgLabel.place(x=215,y=0, width=1130, height=550)

        ############################# Corner Images ##########################
        dinnerImg= Image.open(r"F:\Rohit\Software\python\HotelManagmentSystem\Images\dinnerImg.jpg")  
        dinnerImg= dinnerImg.resize((200,150),Image.ANTIALIAS)                                          
        self.dinnerimg = ImageTk.PhotoImage(dinnerImg)
        dinnerimgLabel = Label(mFrame, image=self.dinnerimg, bd=4, relief=RIDGE)
        dinnerimgLabel.place(x=0,y=210, width=200, height=150)

        poolImg= Image.open(r"F:\Rohit\Software\python\HotelManagmentSystem\Images\poolImg.jpg")  
        poolImg=  poolImg.resize((200,150),Image.ANTIALIAS)                                          
        self.poolimg = ImageTk.PhotoImage(poolImg)
        poolimgLabel = Label(mFrame, image=self.poolimg, bd=4, relief=RIDGE)
        poolimgLabel.place(x=0,y=360, width=200, height=150)
 
    def customerDetails(self):
        self.customerWindow = Toplevel(self.mWindow)
        self.customer = Customer_Window(self.customerWindow)

    def roomInfo(self):
        self.RoomWindow = Toplevel(self.mWindow)
        self.room = roomDetails(self.RoomWindow)


        
        


if __name__ == "__main__":
    mWindow = Tk()
    mWindowObj = RTect(mWindow)
    mWindow.mainloop()
        