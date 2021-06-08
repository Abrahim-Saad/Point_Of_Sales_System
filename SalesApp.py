"""
    INVENTORY MANAGEMENT SYSTEM
    Developed By-> Ibrahim Saad, Ahmed Samir, Yossef Ibrahim
    Started On ->08/11/18
"""

import sqlite3
from datetime import datetime
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Userlogin import Login
from Admin_menu import Admin
from User_menu import User
from Intro import splash


# MAIN WINDOW
class Main(splash, Login, Admin, User):
    def __init__(self):
        global b
        if b == 0:
            super().__init__()
            b = 1
        Login.__init__(self)
        self.loginw.mainloop()
        self.loginw.state('withdraw')  # LOGIN WINDOW EXITS
        self.mainw = Toplevel(bg="#FFFFFF")
        width = 1400
        height = 780
        screen_width = self.mainw.winfo_screenwidth()
        screen_height = self.mainw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainw.title("ابو حمزة ماركت")
        self.mainw.resizable(0, 0)
        self.mainw.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        self.getdetails()

    # OVERRIDING CLOSE BUTTON && DESTRUCTOR FOR CLASS LOGIN AND MAIN WINDOW
    def __Main_del__(self):
        if messagebox.askyesno("خروج", "هل تريد الخروج من البرنامج؟"):
            self.loginw.quit()
            self.mainw.quit()
            exit(0)
        else:
            pass

    # FETCH USER DETAILS FROM PRODUCTS,USERS AND INVENTORY TABLE
    def getdetails(self):
        self.cur.execute("")


        self.cur.execute("CREATE TABLE if not exists sales (Trans_id	INTEGER,"
                         "invoice	INTEGER NOT NULL,"
                         "Product_id	varchar (20),"
                         "Quantity INTEGER NOT NULL,"
                         "Date	varchar (20),"
                         "Time varchar (20),"
                         "PRIMARY KEY(Trans_id));")

        capuser = self.username.get()
        capuser = capuser.upper()
        self.cur.execute("select account_type from users where username= ? ", (capuser,))
        l = self.cur.fetchall()
        self.account_type = l[0][0]
        self.buildmain()

    #  ADD WIDGETS TO TOP OF MAIN WINDOW
    def buildmain(self):
        if self.account_type == 'ADMIN':
            super(Admin).__init__()
            self.admin_mainmenu(8, 8)
        else:
            super(User).__init__()
            self.user_mainmenu(8, 8)
        self.logout.config(command=self.__Main_del__)
        self.changeuser.config(command=self.change_user)
        self.topframe = LabelFrame(self.mainw, width=1400, height=120, bg="#4267b2")
        self.topframe.place(x=0, y=0)

        self.storelable=Label(self.topframe, text="أبو حمزة ماركت", bg="#4267b2", anchor="center")
        self.storelable.config(font="Roboto 48 bold", fg="black")
        self.storelable.place(x=520, y=30)


        if self.account_type == 'ADMIN':
            self.adminlabel= Label(self.topframe, text=" Admin", font="Roboto 10 bold",bg="#4267b2")
        else:
            self.adminlabel = Label(self.topframe, text=" User", font="Roboto 10 bold", bg="#4267b2")
        self.adminlabel.place(x=1300, y=80)

        # DATE TIME LABEL


        now = datetime.now()

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.datetimelabel = Label(self.topframe, text=dt_string, font="Roboto 10 bold", bg="#4267b2")
        self.datetimelabel.place(x=1270, y=60)



    # METHODS FOR ITEMS AND CHANGE USER BUTTONS
    def change_user(self):
        if messagebox.askyesno("تنبيه!", "هل تريد تبديل الحساب؟"):
            self.base.commit()
            self.mainw.destroy()
            self.loginw.destroy()
            self.__init__()


if __name__ == '__main__':
    b = 0
    w = Main()
    w.base.commit()
    w.mainw.mainloop()
