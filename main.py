from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self,root):
        self.root = root
        # ----- Initialize the hight and width of window.
        self.root.geometry("900x740+200+50")
        self.root.title("QR generator | Developed by A.")

        # Disable the windows resizable button.
        self.root.resizable(False,False)

        # Added title here.
        title = Label(self.root,text="QR for RC book",font=("times new roman",40),bg='#00b894',fg='white').place(x=0,y=0, relwidth=1)

        # ================== Variable for storing data ===============
        self.ChassisNumbervalue = StringVar()
        self.engineNumbervalue = StringVar()
        self.registeredNumbervalue = StringVar()
        self.registeredDatevalue = StringVar()
        self.registerOwnerNamevalue = StringVar()
        self.addressvalue = StringVar()
        self.makerNamevalue = StringVar()
        self.classOfVehiclevalue = StringVar()
        self.makerClassvalue = StringVar()
        self.monthYearMfgvalue = StringVar()
        self.motorVehileIsvalue = StringVar()
        self.certificatiValidUptovalue = StringVar()
        self.wheelBasevalue = StringVar()
        self.colourvalue = StringVar()
        self.fuelUsedvalue = StringVar()

        # ================== RC-book detail window ===================
        rc_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        rc_frame.place(x=50,y=80,width=500,height=650)

        # Inside the RC frame title.
        rc_title = Label(rc_frame, text="Vehicle details", font=("goudy old style", 15,"bold"), bg='#6c5ce7', fg='white').place(x=0,y=0,relwidth=1)

        # Added Label for each field.
        ChassisNumber = Label(rc_frame, text="ChassisNumber", font=("goudy old style", 15,"bold"), bg='white', ).place(x=20,y=50)
        engineNumber = Label(rc_frame, text="engineNumber", font=("goudy old style", 15,"bold"), bg='white', ).place(x=20,y=90)
        registeredNumber = Label(rc_frame, text="Registered Number", font=("goudy old style", 15,"bold"), bg='white', ).place(x=20,y=130)
        registeredDate = Label(rc_frame, text='RegisteredDate', font=("goudy old style", 15,"bold"), bg='white', ).place(x=20,y=170)
        registerOwnerName = Label(rc_frame, text='Reg. Owner Name', font=("goudy old style", 15, "bold"),bg='white', ).place(x=20, y=210)
        address = Label(rc_frame, text='Address', font=("goudy old style", 15, "bold"),bg='white', ).place(x=20, y=250)
        makerName= Label(rc_frame, text='Maker\'s Name', font=("goudy old style", 15, "bold"), bg='white', ).place(x=20, y=290)
        classOfVehicle = Label(rc_frame, text='Class of vehicle', font=("goudy old style", 15, "bold"), bg='white', ).place(x=20, y=330)
        makerClass = Label(rc_frame, text='Maker\'s Class', font=("goudy old style", 15, "bold"), bg='white', ).place(x=20, y=370)
        monthYearMfg = Label(rc_frame, text='Month & Year Mfg.', font=("goudy old style", 15, "bold"), bg='white', ).place(x=20, y=410)
        motorVehileIs = Label(rc_frame, text='Motor vehicle is', font=("goudy old style", 15, "bold"), bg='white', ).place(x=20, y=450)
        certificatiValidUpto = Label(rc_frame, text='Original date of reg.', font=("goudy old style", 15, "bold"),bg='white', ).place(x=20, y=490)
        wheelBase = Label(rc_frame, text='Wheel-base(mm)',font=("goudy old style", 15, "bold"), bg='white', ).place(x=20, y=530)
        colour= Label(rc_frame, text='Color', font=("goudy old style", 15, "bold"), bg='white', ).place(x=20, y=570)
        fuelUsed = Label(rc_frame, text='Fuel Used', font=("goudy old style", 15, "bold"), bg='white', ).place(x=20, y=610)


        #Entry fields for each label.
        txt_ChassisNumber = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.ChassisNumbervalue, bg='white').place(x=220, y=50)
        txt_engineNumber = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.engineNumbervalue,bg='white').place(x=220, y=90)
        txt_registeredNumber = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.registeredNumbervalue,bg='white').place(x=220, y=130)
        txt_registeredDate = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.registeredDatevalue, bg='white').place(x=220, y=170)
        txt_registerOwnerName = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.registerOwnerNamevalue, bg='white').place(x=220, y=210)
        txt_address = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.addressvalue, bg='white').place(x=220, y=250)
        txt_makerName = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.makerNamevalue, bg='white').place(x=220, y=290)
        txt_classOfVehicle = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.classOfVehiclevalue, bg='white').place(x=220, y=330)
        txt_makerClass = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.makerClassvalue, bg='white').place(x=220, y=370)
        txt_monthYearMfg = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.monthYearMfgvalue, bg='white').place(x=220, y=410)
        txt_motorVehileIs = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.motorVehileIsvalue, bg='white').place(x=220, y=450)
        txt_certificatiValidUpto = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.certificatiValidUptovalue, bg='white').place(x=220, y=490)
        txt_wheelBase = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.wheelBasevalue, bg='white').place(x=220, y=530)
        txt_colour = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.colourvalue, bg='white').place(x=220, y=570)
        txt_fuelUsed = Entry(rc_frame, font=("goudy old style", 15),textvariable=self.fuelUsedvalue, bg='white').place(x=220, y=610)

        # ================== RC-book QR code window ===================
        # Generated QR code will be shown here.
        # defined frame.
        qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_frame.place(x=600, y=100, width=250, height=380)

        qr_title = Label(qr_frame, text="QR Code", font=("goudy old style", 15, "bold"), bg='#6c5ce7',fg='white').place(x=0, y=0, relwidth=1)
        self.qr_code=Label(qr_frame,text="No QR code\n Available",font=('times new roman',15),bg='blue')
        self.qr_code.place(x=35,y=100,width=180,height=180)

        # Button to generate the qr code.
        btn_generate = Button(qr_frame,text="QR Generate",command=self.generate).place(x=35,y=290)

        # Button to clear the all entered data inside the textfield.
        btn_clear = Button(qr_frame,text='Clear',command=self.clear_data).place(x=140,y=290)

        # Initialize the variable to print the message after taken any action.
        self.msg = ""
        self.lbl_msg = Label(qr_frame, text=self.msg)
        self.lbl_msg.place(x=35, y=340)

    # function to clear fields.
    def clear_data(self):
        self.ChassisNumbervalue.set('')
        self.engineNumbervalue.set('')
        self.registeredNumbervalue.set('')
        self.registeredDatevalue.set('')
        self.registerOwnerNamevalue.set('')
        self.addressvalue.set('')
        self.makerNamevalue.set('')
        self.classOfVehiclevalue.set('')
        self.makerClassvalue.set('')
        self.monthYearMfgvalue.set('')
        self.motorVehileIsvalue.set('')
        self.certificatiValidUptovalue.set('')
        self.wheelBasevalue.set('')
        self.colourvalue.set('')
        self.fuelUsedvalue.set('')
        self.msg = ""
        self.lbl_msg.config(text=self.msg)

    # This is a Magic function to create/generate the qr code.
    def generate(self):
        #print(self.chaseNumbervalue.get())
        if self.ChassisNumbervalue.get()=='' or self.engineNumbervalue.get()=='' or self.registeredNumbervalue.get()=='' \
                or self.registeredDatevalue.get()== '' or self.registerOwnerNamevalue.get()=='' or self.addressvalue.get() == ''\
                or self.makerNamevalue.get()=='' or self.classOfVehiclevalue.get()=='' or self.makerClassvalue.get()=='' or self.monthYearMfgvalue.get()==''\
                or self.motorVehileIsvalue.get()=='' or self.certificatiValidUptovalue.get()=='' or self.wheelBasevalue.get()=='' or self.colourvalue.get()==''\
                or self.fuelUsedvalue.get()== '':
            self.msg = "All Fields are mandatory..!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            #====== updating data =======
            qr_data =(f"Chassis Number: {self.ChassisNumbervalue.get()}\n Engine Number: {self.engineNumbervalue.get()}\n Registered Number:{self.registeredNumbervalue.get()}"
                      f"\n Maker Name: {self.makerNamevalue.get()}\n Class Of Vehicle: {self.classOfVehiclevalue.get()}\n Maker Class: {self.makerClassvalue.get()}"
                      f"\n Month & Year Mfg.: {self.monthYearMfgvalue.get()}\n Motor Vehicle Is: {self.motorVehileIsvalue.get()}"
                      f"\n Certificate Valid Upto: {self.certificatiValidUptovalue.get()}\n Wheel Base: {self.wheelBasevalue.get()}"
                      f"\n Color: {self.colourvalue.get()}\n Fuel Used: {self.fuelUsedvalue.get()}")
            qr_code = qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])

            #======= QR code Image update ========
            self.img = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.img)

            #saving the generated qr_code into system in .png format.
            qr_code.save('RC_'+str(self.registerOwnerNamevalue.get())+'.png')
            self.msg = "QR Generated successfully..!"
            self.lbl_msg.config(text=self.msg, fg='green')

root = Tk()
obj = Qr_Generator(root)
root.mainloop()