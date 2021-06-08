"""
    INVENTORY MANAGEMENT SYSTEM
    Developed By->PJ28105
    Started On ->08/11/18
"""
# coding : utf-8
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Admin_menu import Admin


# LOGIN CLASS
class Login:

    def __init__(self):
        self.loginw = Tk()
        self.loginw.title("تسجيل الدخول")
        width = 500
        height = 600
        screen_width = self.loginw.winfo_screenwidth()
        screen_height = self.loginw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.loginw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg="#4267b2")
        self.logintable()
        self.username = StringVar()
        self.password = StringVar()
        self.obj()

    def __login_del__(self):
        if messagebox.askyesno("خروج", " مغادرة البرنامج؟"):
            self.loginw.destroy()
            exit(0)                   # FORCE SYSTEM TO EXIT

    # LOGIN TABLE
    def logintable(self):
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
        self.cur.execute("CREATE TABLE if not exists users ("
                         "username varchar (20),"
                         "password varchar (20) NOT NULL,"
                         "account_type varchar ( 10 ) NOT NULL,"
                         "PRIMARY KEY(username));")


    # WIDGET FUNCTION
    def obj(self):
        self.loginframe = LabelFrame(self.loginw, bg="#4267b2", height=410, width=310)
        self.loginw.bind('<Return>', self.checkuser)
        self.loginframe.place(x=100, y=95)
        self.toplabel = Label(self.loginframe, fg="white", bg="#4267b2", anchor="center", text="تسجيل الدخول", font="Roboto 25 bold")
        self.toplabel.place(x=75, y=25)
        self.usename_label = Label(self.loginframe, text="اسم المستخدم", fg="white", bg="#4267b2", anchor="e", font="Roboto 16 bold")
        self.usename_label.place(x=175, y=110)
        self.us = ttk.Entry(self.loginframe, width=20, textvariable=self.username, font="Roboto 14 ")
        self.us.place(x=35, y=145, height=40)
        self.password_label = Label(self.loginframe, text="كلمة المرور",  fg="white", bg="#4267b2", anchor="e", font="Roboto 16 bold")
        self.password_label.place(x=180, y=190)
        self.pa = ttk.Entry(self.loginframe, width=20, textvariable=self.password, show="*", font="Roboto 14 ")
        self.pa.place(x=35, y=220, height=40)
        self.us.bind('<Button-1>', self.onclick)
        self.pa.bind('<Button-1>', self.onclick1)
        self.signin = Button(self.loginframe, width=20, text="تسجيل الدخول", bg="lightblue2", fg="dimgray", command=self.checkuser, font="Roboto 14")
        self.signin.place(x=35,y=290)
     #  self.register = Button(self.loginframe,width=20, text = "Register",bg="lightblue2",fg="dimgray",command = self.reguser,font="Roboto")
     #   self.register.place(x=35,y=320)

    # CHECK USER IN DATABASE
    def checkuser(self, event=0):
        s = self.username.get()
        s1 = self.password.get()
        s = s.upper()
        s1 = s1.upper()
        self.cur.execute("select * from users where username=? and password=? ", (s, s1))
        l = self.cur.fetchall()
        if(len(l)>0):
            self.success()
        else:
            self.fail()

    # LOGIN SUCCESS
    def success(self):
       # messagebox.showinfo(عملية ناجحة","تم تسجيل الدخول بنجاح")
        self.loginw.quit()

    # LOGIN FAILURE
    def fail(self):
        messagebox.showerror("خطأ", "هناك خطأ في اسم المستخدم او كلمة المرور")

    # USER REGISTRATION && LOGIN->REGISTER
    def reguser(self):
        self.toplabel.config(text="التسجيل")
        self.toplabel.place(x=40,y =25)
        self.username.set("")
        self.password.set("")
        self.signin.config(text="Ok", command=self.insert)
       # ADD
        self.register = Button(self.loginframe, width=20, text="عودة", bg="lightblue2",fg="dimgray",command = self.revert,font="Roboto 14")
        self.register.place(x=35, y=320)
       # self.register.config(text="Back",command=self.revert)
        self.signin.config()
        self.signin.place(x=35, y=260)
        self.pa.config(show='')
        self.loginw.focus()
        self.loginw.bind('<Return>', self.insert)
        self.loginw.title('تسجيل')

    # REGISTER USER TO DATABASE
    def insert(self,event=0):
        s = self.username.get()
        s1 = self.password.get()
        s = s.upper()
        s1 = s1.upper()
        self.cur.execute("select username from users where username = ?", (s,))
        l = self.cur.fetchall()

        if(len(l)>0 ):
            messagebox.showerror("خطأ", "اسم المستخدم موجود بالفعل")
            self.username.set('اختر اسم المستخدم')
            self.loginw.focus()
            return
        if len(s) == 0 or len(s1) == 0 or len(s) > 20 or len(s1) > 20 or s1 == "CREATE A PASSWORD" or s == 'CHOOSE YOUR USERNAME':
            messagebox.showerror("Error", "Invalid username or password")
            self.username.set('اختر اسم المستخدم')
            self.password.set('انشاء كلمة المرور')
            self.pa.config(show='*')
            self.loginw.focus()
            return
        else:
            self.cur.execute("insert into users values(?,?,?)", (s,s1,'USER'))
            messagebox.showinfo("عملية ناجحة", "تم تسجيل الحساب بنجاح")
            self.base.commit()
            self.revert()
            # ADD
            self.loginw.state('withdraw')
            self.tree.delete(*self.tree.get_children())
            self.getusers()

    # REGISTER->LOGIN
    def revert(self):
        self.toplabel.config(text="دخول")
        self.toplabel.place(x=75,y=25)
        self.signin.config(text="Sign in", command=self.checkuser)
        self.register.config(text="Register", command=self.reguser)
        self.username.set('Username')
        self.password.set('Password')
        self.pa.config(show='')
        self.signin.config(state=NORMAL)
        self.loginw.focus()
        self.loginw.bind('<Return>',self.checkuser)
        # ADD
        self.signin.place(x=35, y=290)
        self.loginw.title('Login')
        self.loginw.state('withdraw')

    # ONCLICK EVENTS
    def onclick(self,event):
        if (self.username.get() == "Username" or self.username.get() == "Choose your username"):
            self.us.delete(0, "end")

    def onclick1(self,event):
        if (self.password.get() == "Password" or self.password.get() == "Create a password"):
            self.pa.delete(0, "end")
            self.pa.config(show="*")

'''           
#TEST LOGIN
w=login()
w.base.commit()
w.loginw.mainloop()
'''



