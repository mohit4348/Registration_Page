from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox as tmsg
import calendar


class registration:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1370x700")
        self.root.title("Registration Form")

        self.salvar = StringVar()
        self.fnamevar =StringVar()
        self.lnamevar = StringVar()
        self.emailvar = StringVar()
        self.ccvar = IntVar()
        self.mobnovar = IntVar()
        self.passvar = StringVar()
        self.confimpassvar = StringVar()
        self.dobvar = StringVar()
        self.squesvar = StringVar()
        self.sqanswervar = StringVar()
        self.checkvar = IntVar()


        self.root.iconbitmap(r"C:\Users\Mohit Sharma\OneDrive\Desktop\New folder\Registration_Page\1.ico")
        self.mainbg = ImageTk.PhotoImage(Image.open("5.jpg").resize((1380,720)))
        lblmainbg = Label(self.root,image=self.mainbg)
        lblmainbg.pack()

        self.bg1 = ImageTk.PhotoImage(Image.open("8.jpg").resize((400,550)))
        lblbg1 = Label(lblmainbg,image=self.bg1,bd=0)
        lblbg1.place(x=800,y=80)

        frameform = Frame(self.root,bg="white",bd=0)
        frameform.place(x=152,y=80,height=550,width=650)

        self.hibg = ImageTk.PhotoImage(Image.open("3.jpg").resize((100,100)))
        lblhi = Label(frameform,image=self.hibg,bd=0)
        lblhi.place(x=10,y=10)

        txtlbl = Label(frameform,text="Please Enter The Following Details!",bg="white",fg="Black",font="georgia 15 bold")
        txtlbl.place(x=110,y=45)

        lblsalutation = Label(frameform,text="Mr./Mrs./Ms.",bg="white",fg="Black",font="georgia 10 bold")
        lblsalutation.place(x=60,y=120)

        options = ["Select","Mr","Mrs","Ms"]
        salutationbox = ttk.Combobox(frameform,values=options,state="readonly",font="georgia 10",cursor="hand2",textvariable=self.salvar)
        salutationbox.current(0)
        salutationbox.place(x=60,y=145,width=80)

        lblfirstname = Label(frameform,text="First Name",bg="white",fg="Black",font="georgia 10 bold")
        lblfirstname.place(x=200,y=120)

        entryfirstname = ttk.Entry(frameform,textvariable=self.fnamevar)
        entryfirstname.place(x=200,y=145,width=170)

        lbllastname = Label(frameform,text="Last Name",bg="white",fg="Black",font="georgia 10 bold")
        lbllastname.place(x=420,y=120)

        entrylastname = ttk.Entry(frameform,textvariable=self.lnamevar)
        entrylastname.place(x=420,y=145,width=170)

        lblemail = Label(frameform,text="Email",bg="white",fg="Black",font="georgia 10 bold")
        lblemail.place(x=60,y=210)

        entryemail = ttk.Entry(frameform,textvariable=self.emailvar)
        entryemail.place(x=60,y=235,width=230)

        lblcode = Label(frameform,text="CC",bg="white",fg="Black",font="georgia 10 bold")
        lblcode.place(x=330,y=210)

        entrycode = ttk.Entry(frameform,textvariable=self.ccvar)
        entrycode.place(x=330,y=235,width=50)

        lblmobno = Label(frameform,text="Mob. No.",bg="white",fg="Black",font="georgia 10 bold")
        lblmobno.place(x=390,y=210)

        entrymobno = ttk.Entry(frameform,textvariable=self.mobnovar)
        entrymobno.place(x=390,y=235,width=200)

        lblpassword = Label(frameform,text="Password",bg="white",fg="Black",font="georgia 10 bold")
        lblpassword.place(x=60,y=290)

        entrypassword = ttk.Entry(frameform,textvariable=self.passvar)
        entrypassword.place(x=60,y=315,width=155)

        lblconfirmpassword = Label(frameform,text="Confirm Password",bg="white",fg="Black",font="georgia 10 bold")
        lblconfirmpassword.place(x=250,y=290)

        entryconfirmpassword = ttk.Entry(frameform,textvariable=self.confimpassvar)
        entryconfirmpassword.place(x=250,y=315,width=155)

        lbldob = Label(frameform,text="D.O.B.(DD/MM/YYYY)",bg="white",fg="Black",font="georgia 10 bold")
        lbldob.place(x=450,y=290)

        entrydob = ttk.Entry(frameform,textvariable=self.dobvar)
        entrydob.place(x=450,y=315,width=140)

        lblquetion = Label(frameform,text="Security Q.",bg="white",fg="Black",font="georgia 10 bold")
        lblquetion.place(x=60,y=360)

        Questions = ["Select","What is your mother's maiden name?",    
                        "What is your pet's name?",
                        "What is your favorite food?",
                        "What was the name of your first school?",
                        "What was your first job?",
                        "What is your favorite book?",
                        "What is your favorite movie?",
                        ]
        
        questioncombo = ttk.Combobox(frameform,values=Questions,font="georgia 10",state="readonly",cursor="hand2",textvariable=self.squesvar)
        questioncombo.current(0)
        questioncombo.place(x=60,y=385,width=300)

        lblsq = Label(frameform,text="Security Answer",font="georgia 10 bold",bg="white")
        lblsq.place(x=370,y=360)

        entrsqanswer = ttk.Entry(frameform,font="georgia 10",textvariable=self.sqanswervar)
        entrsqanswer.place(x=370,y=385,width=220)

        checkbuton = Checkbutton(frameform,text="I Agree Terms & Conditions!",font="goergia 8",bg="white",activebackground="white",onvalue=1,offvalue=0,cursor="hand2",variable=self.checkvar)
        checkbuton.place(x=60,y=425)

        Signupbuton = Button(frameform,text="Register!",font="georgia 15 bold",bg="green",fg="white",activebackground="green",activeforeground="white",relief=GROOVE,borderwidth=0,cursor="hand2",command=self.registerfunc)
        Signupbuton.place(x=259,y=430)

        Alreadylbl = Label(frameform,text="Already Have An ACCOUNT?",font="georgia 10",bg="white",fg="black")
        Alreadylbl.place(x=60,y=490)

        clickherebuton = Button(frameform,text="Click Here!",fg="blue",bg="white",bd=0,font="georgia 10 bold",activebackground="white",activeforeground="blue",cursor="hand2")
        clickherebuton.place(x=240,y=490)

    def registerfunc(self):
        if self.fnamevar.get()=="" or self.emailvar.get()=="" or self.squesvar.get()=="Select":
            tmsg.showerror("Error","Please Fill The Required Fields!")
        elif self.salvar.get()=="Select":
            tmsg.showerror("Error","Please Select The Salutation!")
        elif self.passvar.get()!=self.confimpassvar.get():
            tmsg.showerror("Error","Password & Confirm Password Are Not Same.")
        elif self.checkvar.get()==0:
            tmsg.showerror("Error","Please Accept Our Terms & Conditions!")
        else:
            conn = mysql.connector.connect(host="localhost", user = "root", password = "mohit123", database = "signindata")
            my_cursor = conn.cursor()
            query = ("select * from registerdata where Email = %s")
            value = (self.emailvar.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                tmsg.showerror("Error","Email Already Exists! Please Try With Another Email.")
            else:
                my_cursor.execute("Insert Into registerdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.salvar.get(),
            self.fnamevar.get(),
            self.lnamevar.get(),
            self.emailvar.get(),
            self.ccvar.get(),
            self.mobnovar.get(),
            self.passvar.get(),
            self.confimpassvar.get(),
            self.dobvar.get(),
            self.squesvar.get(),
            self.sqanswervar.get(),
            self.checkvar.get(),
            
            ))
                conn.commit()
                conn.close()
                tmsg.showinfo("Success","You Are Successfully Registered!")



        
if __name__=="__main__":

    root = Tk()
    app = registration(root)
    root.mainloop()