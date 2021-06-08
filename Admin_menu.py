"""
    INVENTORY MANAGEMENT SYSTEM
    Developed By->PJ28105
    Started On ->08/11/18
"""

import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from Addtional_features import mycombobox, myentry


# ADMIN MENU
class Admin:
    global merchant_name


    def __init__(self):
        self.base = None
        self.cur = None

    def _init_(self, mainw):
        self.mainw = mainw

    # ADD ADMIN MAIN MENU TO WINDOW,ALL FRAMES AND ADD IMAGE BUTTONS
    def admin_mainmenu(self, a, b):
        '''
        self.cur.execute("delete from new_income;")
        self.cur.execute("delete from today_income;")
        #self.cur.execute("delete from returns;")
        #self.cur.execute("delete from returns_history;")
        self.cur.execute("delete from total_income;")
        self.cur.execute("delete from market_table;")
        self.cur.execute("delete from market_items;")
        self.cur.execute("delete from to_market_table_new;")
        self.cur.execute("delete from sales_table;")
        self.cur.execute("delete from sales_history;")
        '''
        '''
        self.cur.execute("drop table new_income;")
        self.cur.execute("drop table today_income;")
        self.cur.execute("drop table returns;")
        self.cur.execute("drop table returns_history;")
        self.cur.execute("drop table total_income;")
        self.cur.execute("drop table market_table;")
        self.cur.execute("drop table market_items;")
        self.cur.execute("drop table to_market_table_new;")
        self.cur.execute("drop table sales_table;")
        self.cur.execute("drop table sales_history;")
        '''

        self.mainframe = LabelFrame(self.mainw, width=1400, height=145, bg="gray")
        self.mainframe.place(x=0, y=100)
        mi = PhotoImage(file="images/accounts.png")
        mi = mi.subsample(a, b)
        self.accounts = Button(self.mainframe, text="مستخدمون", font="roboto 11 bold", bd=5, image=mi, compound=TOP,
                               command=self.buildusertable)
        self.accounts.image = mi
        self.accounts.place(x=900, y=27)

        mi = PhotoImage(file="images/Contacts-512.png")
        mi = mi.subsample(a, b)
        self.accounts = Button(self.mainframe, text="عملاء", font="roboto 11 bold", bd=5, image=mi, compound=TOP,
                               command=self.build_customers_table)
        self.accounts.image = mi
        self.accounts.place(x=750, y=27)

        mi = PhotoImage(file="images/invoice2.png")
        mi = mi.subsample(a, b)
        self.aitems = Button(self.mainframe, text="بيع", bd=5, font="roboto 11 bold", image=mi, compound=TOP,
                             command=self.sales)
        self.aitems.image = mi
        self.aitems.place(x=300, y=27)

        mi = PhotoImage(file="images/Door_Out-512.png")
        mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="خروج", bd=5, font="roboto 11 bold", image=mi, compound=TOP)
        self.logout.image = mi
        self.logout.place(x=1200, y=27)
        mi = PhotoImage(file="images/change1.png")
        mi = mi.subsample(a, b)
        self.changeuser = Button(self.mainframe, text="تبديل الحساب", bd=5, font="roboto 11 bold", image=mi,
                                 compound=TOP)
        self.changeuser.image = mi
        self.changeuser.place(x=1050, y=27)
        mi = PhotoImage(file="images/items.png")
        mi = mi.subsample(a, b)
        self.items = Button(self.mainframe, text="وارد", bd=5, image=mi, font="roboto 11 bold", compound=TOP,
                            command=self.additems)
        self.items.image = mi
        self.items.place(x=150, y=27)
        mi = PhotoImage(file="images/inventory.png")
        mi = mi.subsample(a, b)
        self.stocks = Button(self.mainframe, text="تجار", bd=5, image=mi, font="roboto 11 bold", compound=TOP,
                             command=self.buildprodtable)
        self.stocks.image = mi
        self.stocks.place(x=600, y=27)
        mi = PhotoImage(file="images/sales.png")
        mi = mi.subsample(a, b)
        self.sales = Button(self.mainframe, text="مبيعات", bd=5, font="roboto 11 bold", image=mi, compound=TOP,
                            command=self.buildsalestable)

        self.sales.image = mi
        self.sales.place(x=450, y=27)
        self.formframe = Frame(self.mainw, width=500, height=550, bg="#FFFFFF")
        self.formframe.place(x=620, y=315)
        self.formframeinfo = self.formframe.place_info()
        self.tableframe1 = LabelFrame(self.mainw, width=350, height=700)
        self.tableframe1.place(x=1200, y=315, anchor=NE)
        self.tableframe1info = self.tableframe1.place_info()

        self.tableframe2 = LabelFrame(self.mainw, width=200, height=700)
        self.tableframe2.place(x=610, y=310, anchor=NE)
        self.tableframe2info = self.tableframe2.place_info()

        self.tableframe = LabelFrame(self.mainw, width=350, height=700)
        self.tableframe.place(x=500, y=315, anchor=NE)
        self.tableframeinfo = self.tableframe.place_info()
        self.itemframe = Frame(self.mainw, bg="#FFFFFF", width=1300, height=400)
        self.itemframe.place(x=620, y=310, anchor=NW)
        self.itemframeinfo = self.itemframe.place_info()

        self.salesframe = Frame(self.mainw, bg="#FFFFFF", width=1400, height=500)
        self.salesframe.place(x=0, y=250, anchor=NW)
        self.salesframeinfo = self.salesframe.place_info()

        self.salesframe2 = Frame(self.mainw, width=1300, height=480, bg="#FFFFFF")
        self.salesframe2.place(x=20, y=250, anchor=NW)
        self.salesframeinfo2 = self.salesframe2.place_info()

        self.storesframe = Frame(self.mainw, bg="#FFFFFF", width=1300, height=400)
        self.storesframe.place(x=500, y=310, anchor=NW)
        self.storesframeinfo = self.storesframe.place_info()

        self.marketfrme = Frame(self.mainw, bg="#FFFFFF", width=400, height=400)
        self.marketfrme.place(x=480, y=310, anchor=NW)
        self.marketfrmeinfo = self.marketfrme.place_info()

        self.returnframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=700)
        self.returnframe.place(x=800, y=310, anchor=NW)
        self.returnframeinfo = self.returnframe.place_info()

        self.tableframe3 = LabelFrame(self.mainw, width=350, height=700)
        self.tableframe3.place(x=620, y=320, anchor=NE)
        self.tableframe3info = self.tableframe3.place_info()

        self.tableframe4 = LabelFrame(self.mainw, width=350, height=500)
        self.tableframe4.place(x=480, y=310, anchor=NE)
        self.tableframe4info = self.tableframe4.place_info()

        self.tableframe5 = LabelFrame(self.mainw, width=180, height=700)
        self.tableframe5.place(x=1380, y=310, anchor=NE)
        self.tableframe5info = self.tableframe5.place_info()

        self.tableframe6 = LabelFrame(self.mainw, width=300, height=700)
        self.tableframe6.place(x=420, y=280, anchor=NE)
        self.tableframe6info = self.tableframe6.place_info()

        self.tableframe7 = LabelFrame(self.mainw, width=180, height=700)
        self.tableframe7.place(x=1360, y=310, anchor=NE)
        self.tableframe7info = self.tableframe7.place_info()

        self.tableframe8 = LabelFrame(self.mainw, width=180, height=700)
        self.tableframe8.place(x=1300, y=340, anchor=NE)
        self.tableframe8info = self.tableframe8.place_info()

        self.customers = LabelFrame(self.mainw, width=1355, height=498, bg="#FFFFFF")
        self.customers.place(x=1370, y=245, anchor=NE)
        self.customersinfo = self.customers.place_info()

        self.tableframe10 = LabelFrame(self.mainw, width=350, height=700)
        self.tableframe10.place(x=1200, y=315, anchor=NE)
        self.tableframe10info = self.tableframe10.place_info()

        self.formframe1 = Frame(self.mainw, width=500, height=445, bg="#FFFFFF")
        self.formframe1.place(x=100, y=275)
        self.formframe1info = self.formframe1.place_info()
        self.searchframe = Frame(self.mainw, width=720, height=70, bg="#FFFFFF")
        self.searchframe.place(x=575, y=260)
        self.searchframeinfo = self.searchframe.place_info()
        self.searchbut = Button(self.searchframe, text="Search Description", font="roboto 14", bg="#FFFFFF", bd=5,
                                command=self.searchprod)
        self.searchbut.place(x=0, y=20, height=40)
        self.searchvar = StringVar()
        self.searchentry = myentry(self.searchframe, textvariable=self.searchvar, font="roboto 14", width=25,
                                   bg="#FFFFFF")
        self.searchentry.place(x=210, y=20, height=40)
        self.cur.execute("select merchant_name from merchants")
        li = self.cur.fetchall()
        a = []
        for i in range(0, len(li)):
            a.append(li[i][0])
        self.searchentry.set_completion_list(a)
        self.resetbut = Button(self.searchframe, text="مسح", font="roboto 14", bd=5, width=8, bg="#FFFFFF",
                               command=self.resetprodtabel)
        self.resetbut.place(x=510, y=18, height=40)
        self.cond = 0
        self.buildprodtable()

    # ADMIN MAIN MENU ENDS

    # BUILD PRODUCT TABLE AT INVENTORY
    def buildprodtable(self):
        self.salesframe2.place_forget()
        self.tableframe4.place_forget()
        self.tableframe5.place_forget()
        self.tableframe6.place_forget()
        self.tableframe7.place_forget()
        self.returnframe.place_forget()
        self.searchframe.place_forget()
        self.tableframe2.place_forget()
        self.tableframe3.place_forget()
        self.salesframe.place_forget()
        self.marketfrme.place_forget()
        self.storesframe.place_forget()
        self.tableframe.place(self.tableframeinfo)
        self.formframe.place(self.formframeinfo)
        self.tableframe1.place_forget()
        self.formframe1.place_forget()
        self.itemframe.place_forget()
        self.tableframe8.place_forget()
        self.customers.place_forget()
        self.tableframe10.place_forget()


        scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe, columns=("Product ID", "Product Name", "Description"),
                                 selectmode="browse", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)

        self.tree.heading('Product ID', text="رقم التاجر", anchor=W)
        self.tree.heading('Product Name', text="اسم التاجر", anchor=W)
        self.tree.heading('Description', text="المديونية", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)

        self.tree.bind("<<TreeviewSelect>>", self.clickprodtable)
        self.formframe.focus_set()

        # new
        self.newitemcode = StringVar()
        self.newitem = StringVar()
        self.newitemcat = StringVar()

        l = ['رقم التاجر', "اسم التاجر", "المديونية"]
        for i in range(0, len(l)):
            Label(self.formframe, text=l[i], font="Roboto 14 bold", bg="#ffffff").grid(row=i, column=0, pady=15,
                                                                                       sticky="w")
        Entry(self.formframe, width=40, textvariable=self.newitemcode, font="roboto 11", bg="#ffffff").grid(row=0,
                                                                                                            column=1,
                                                                                                            pady=15,
                                                                                                            padx=10,
                                                                                                            ipady=3)
        Entry(self.formframe, width=40, textvariable=self.newitem, font="roboto 11", bg="#ffffff").grid(row=1, column=1,
                                                                                                        pady=15,
                                                                                                        padx=10,
                                                                                                        ipady=3)

        cat = myentry(self.formframe, width=40, textvariable=self.newitemcat, font="roboto 11", bg="#ffffff")
        cat.grid(row=2, column=1, pady=15, padx=10, ipady=3)

        self.cur.execute("select merchant_id,merchant_name,debt from merchants")
        li = self.cur.fetchall()
        a = []
        cat.set_completion_list(a)
        Button(self.formframe, text="اضافة تاجر", height=3, width=8, bd=6, command=self.insertitem,
               font="roboto 11 bold",
               bg="#4267b2").grid(row=1,
                                  column=4,
                                  pady=10,
                                  padx=12,
                                  sticky="w",
                                  ipadx=10)
        Button(self.formframe, text="تعديل", height=3, width=8, bd=6, command=self.changeprodtable, bg="#4267b2",
               font="roboto 11 bold").grid(
            row=2, column=4, padx=12, pady=10, sticky="w", ipadx=10)
        Button(self.formframe, text="ازالة", height=3, width=8, bd=6, command=self.delproduct, bg="#4267b2",
               font="roboto 11 bold").grid(
            row=2, column=5, padx=12, pady=10, sticky="w", ipadx=10)
        Button(self.formframe, text="سجل التاجر", height=3, width=8, bd=6, command=self.merchant_history, bg="#4267b2",
               font="roboto 11 bold").grid(
            row=1, column=5, padx=12, pady=10, sticky="w", ipadx=10)

        self.getproducts()

    def get_merchant_info(self):
        ans = ''
        self.get_merchant_name = self.newitem.get()
        self.cur.execute(
            "select * from today_income where name_of_merchant=?", (self.get_merchant_name,))
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            x = 0
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def merchant_history(self):
        self.get_merchant_name = self.newitem.get()

        if self.get_merchant_name == "":
            messagebox.showerror("خطأ", "يجب تحديد اسم التاجر")

        else:
            self.merchanthistoryw = Tk()
            width = 1400
            height = 400
            screen_width = self.merchanthistoryw.winfo_screenwidth()
            screen_height = self.merchanthistoryw.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            self.merchanthistoryw.geometry("%dx%d+%d+%d" % (width, height, x, y))
            self.history_table_frame = Frame(self.merchanthistoryw, width=1400, height=450, bg="#FFFFFF")
            self.history_table_frame.place(x=0, y=80)
            self.history_table_frame_info = self.history_table_frame.place_info()

            scrollbarx = Scrollbar(self.history_table_frame, orient=HORIZONTAL)
            scrollbary = Scrollbar(self.history_table_frame, orient=VERTICAL)
            self.tree = ttk.Treeview(self.history_table_frame,
                                     columns=("merchant_name", "receipt_date", "entered_date", "receipt_id",
                                              'supervisor', 'receipt_total_price', 'payed', 'remaining',
                                              'product_name',
                                              'quantity', 'storeroom', 'piece_price', 'unit_price', 'total_price'),
                                     selectmode="browse", height=16,
                                     yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            self.tree.column('#0', stretch=NO, minwidth=0, width=10)
            self.tree.column('#1', stretch=NO, minwidth=0, width=65)
            self.tree.column('#2', stretch=NO, minwidth=0, width=80)
            self.tree.column('#3', stretch=NO, minwidth=0, width=80)
            self.tree.column('#4', stretch=NO, minwidth=0, width=80)
            self.tree.column('#5', stretch=NO, minwidth=0, width=50)
            self.tree.column('#6', stretch=NO, minwidth=0, width=80)
            self.tree.column('#7', stretch=NO, minwidth=0, width=50)
            self.tree.column('#8', stretch=NO, minwidth=0, width=50)
            self.tree.column('#9', stretch=NO, minwidth=0, width=100)
            self.tree.column('#10', stretch=NO, minwidth=0, width=100)
            self.tree.column('#11', stretch=NO, minwidth=0, width=50)
            self.tree.column('#12', stretch=NO, minwidth=0, width=80)
            self.tree.column('#13', stretch=NO, minwidth=0, width=80)

            self.tree.heading("merchant_name", text="اسم التاجر", anchor=W)
            self.tree.heading("receipt_date", text="تاريخ الفاتورة", anchor=W)
            self.tree.heading('entered_date', text="تاريخ الادخال", anchor=W)
            self.tree.heading('receipt_id', text="رقم الفاتورة", anchor=W)
            self.tree.heading('supervisor', text="المستلم", anchor=W)
            self.tree.heading('receipt_total_price', text="اجمالي الفاتورة", anchor=W)
            self.tree.heading('payed', text="المدفوع", anchor=W)
            self.tree.heading('remaining', text="الباقي", anchor=W)

            self.tree.heading('product_name', text="اسم الصنف", anchor=W)
            self.tree.heading('quantity', text="الكمية", anchor=W)
            self.tree.heading('storeroom', text="رقم المخزن", anchor=W)
            self.tree.heading('piece_price', text="سعر القطعة", anchor=W)
            self.tree.heading('unit_price', text="سعر الوحدة", anchor=W)
            self.tree.heading('total_price', text="سعر الكمية", anchor=W)

            self.tree.grid(row=2, column=0, sticky="W")
            scrollbary.config(command=self.tree.yview)
            scrollbarx.grid(row=2, column=0, sticky="we")
            scrollbarx.config(command=self.tree.xview)
            scrollbary.grid(row=2, column=1, sticky="ns", pady=30)

            self.get_merchant_info()

            self.searchbut = Button(self.merchanthistoryw, text="بحث بالتاريخ", font="roboto 14", bg="#FFFFFF", bd=5,
                                    command=self.search_merchant_history)
            self.searchbut.place(x=350, y=10)

            self.searchbut2 = Button(self.merchanthistoryw, text="بحث بالصنف", font="roboto 14", bg='#FFFFFF', bd=5, )
            self.searchbut2.place(x=270, y=10)

            self.searchvar = StringVar()
            self.searchentry = Entry(self.merchanthistoryw, textvariable=self.searchvar, font="roboto 14", width=25,
                                     bg="#FFFFFF")
            self.searchentry.place(x=520, y=20)

            self.buildprodtable()

            self.merchanthistoryw.mainloop()

    def search_merchant_history(self):
        # cur.execute("SELECT %s FROM Data where %s=?" % (column, goal), (constrain,))
        ans = ''
        try:
            self.get_date = str(self.searchentry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل التاريخ بشكل صحيح")
            return

        if self.get_date == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة التاريخ")
            return
        self.cur.execute('select * from today_income where datetime_entered=? and name_of_merchant=?',
                         (self.get_date, self.get_merchant_name))
        result = self.cur.fetchall()
        self.income_table()
        x = 0,
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        self.buildprodtable()
        return ans

    def serch_merchant_product_history(self):

        # cur.execute("SELECT %s FROM Data where %s=?" % (column, goal), (constrain,))
        ans = ''
        try:
            self.get_product = str(self.searchentry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل اسم الصنف بشكل صحيح")
            return
        if self.get_product == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم الصنف")
            return
        self.cur.execute('select * from today_income where product_name=? and name_of_merchant=?',
                         (self.get_product, self.get_merchant_name))
        result = self.cur.fetchall()
        self.income_table()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def insertitem(self):
        try:
            self.newitemcode.set(int(self.newitemcode.get()))
            self.newitem.set(str(self.newitem.get()).upper())
            self.newitemcat.set(float(self.newitemcat.get()))
        except:
            messagebox.showerror("خطأ", "من فضلك ادخل بيانات صحيحة")
            return

        if self.newitemcode.get() == '' or self.newitem.get() == '' or self.newitemcat.get() == '':
            messagebox.showerror("خطأ", "من فضلك ادخل جميع البيانات")
            return

        else:
            l = [self.newitemcode.get(), self.newitem.get(), self.newitemcat.get()]
            for i in range(0, len(l)):
                if not l[i].isdigit():
                    if i == 0:
                        messagebox.showerror("خطأ", "من فضلك ادخل بيانات صحيحة")
                elif int(l[i]) < 0:
                    messagebox.showerror("خطأ", "من فضلك ادخل بيانات صحيحة")
                    return
        self.cur.execute('select * from merchants where merchant_id = ?', (int(self.newitemcode.get()),))
        l = self.cur.fetchall()
        if (len(l) > 0):
            messagebox.showerror("خطأ", "لا يمكن تكرار رقم التاجر")
            return

        x = int(self.newitemcode.get())
        y = str(self.newitem.get())
        z = float(self.newitemcat.get())
        self.cur.execute("insert into merchants values(?,?,?)", (x, y, z))
        self.newitem.set('')
        self.newitemcode.set('')
        self.newitemcat.set('')
        messagebox.showinfo('تنبيه', 'تم اضافة التاجر بنجاح')
        self.getproducts()
        self.buildprodtable()
        self.base.commit()

    # SEARCH FRAME FOR BOTH USER AND PRODUCT TABLE
    def mainsearch(self, f):
        self.searchvar.set('')

        if (f == 0):
            self.searchframe.place(x=661, y=245)
            self.searchframe.config(width=520)
            self.searchbut.config(command=self.searchuser)
            self.searchbut.config(text="البحث عن حساب")
            self.searchbut.place(x=0, y=23)
            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.resetusertable)
            self.resetbut.place(x=415, y=23)
            self.cur.execute("select username from users")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
        else:
            self.searchframe.place(x=138, y=245)
            self.searchframe.config(width=520)
            self.searchbut.config(command=self.searchinvoice)
            self.searchbut.config(text="Search Invoice No.")
            self.searchbut.place(x=0, y=23)
            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.buildsalestable)
            self.resetbut.place(x=415, y=23)
            self.cur.execute("select invoice from sales")
            li = self.cur.fetchall()
            a = []
            # print(li)
            for i in range(0, len(li)):
                if (a.count(str(li[i][0])) == 0):
                    a.append(str(li[i][0]))
            self.searchentry.set_completion_list(a)

    # FETCH PRODUCTS FROM PRODUCTS TABLE
    def getproducts(self, x=0):
        ans = ''
        self.cur.execute("select * from merchants")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    # MODIFIES RECORD OF PRODUCT TABLE
    def changeprodtable(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.newitemcode.set(int(self.newitemcode.get()))
        self.newitem.set(str(self.newitem.get()).upper())
        self.newitemcat.set(float(self.newitemcat.get()))
        if (len(li) == 3):
            if self.newitemcode.get() == '' or self.newitem.get() == '' or self.newitemcat.get() == '':
                messagebox.showerror("Error", "Invalid Data Provided")
                return

            self.cur.execute(
                "update merchants set merchant_name = ?,debt = ? where merchant_id = ?;", (
                    self.newitem.get(), self.newitemcat.get(), self.newitemcode.get()))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            cur = self.getproducts(li[0])
            self.tree.selection_set(cur)
        self.newitemcode.set("")
        self.newitem.set("")
        self.newitemcat.set("")

    def delproduct(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if messagebox.askyesno('Alert!', 'Do you want to remove product from inventory?') == True and len(li) == 3:
            self.cur.execute("delete from merchants where merchant_id = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getproducts()
            self.newitemcode.set('')
            self.newitem.set('')
            self.newitemcat.set('')

    def searchprod(self):
        if self.searchvar.get() == '':
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from merchants")
        li = self.cur.fetchall()
        for i in li:
            if (i[1] == self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def resetprodtabel(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getproducts()

    # ONCLICK EVENT FOR PRODUCT TABLE
    def clickprodtable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 3):
            self.newitemcode.set((li[0]))
            self.newitem.set((li[1]))
            self.newitemcat.set((li[2]))

    def Table(self):
        scrollbarx = Scrollbar(self.tableframe2, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe2, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe2,
                                 columns=("Product Name", "Storeroom", "Description", "Category", "Product Unit Price",
                                          "Merchant"),
                                 selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=70)
        self.tree.column('#2', stretch=NO, minwidth=0, width=70)
        self.tree.column('#3', stretch=NO, minwidth=0, width=70)
        self.tree.column('#4', stretch=NO, minwidth=0, width=70)
        self.tree.column('#5', stretch=NO, minwidth=0, width=70)

        self.tree.heading('Product Name', text="اسم الصنف", anchor=W)
        self.tree.heading('Storeroom', text="رقم المخزن", anchor=W)
        self.tree.heading('Description', text="الكمية", anchor=W)
        self.tree.heading('Category', text="سعر الكمية", anchor=W)
        self.tree.heading('Product Unit Price', text="سعر الوحدة", anchor=W)
        self.tree.heading('Merchant', text="اسم التاجر", anchor=W)

        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)

    # FUNCTION FOR ITEM BUTTON
    def additems(self):
        self.merchant = StringVar()
        self.tableframe8.place_forget()
        self.salesframe2.place_forget()
        self.tableframe6.place_forget()
        self.tableframe7.place_forget()
        self.returnframe.place_forget()
        self.tableframe3.place_forget()
        self.tableframe4.place_forget()
        self.tableframe5.place_forget()
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.salesframe.place_forget()
        self.marketfrme.place_forget()
        self.storesframe.place_forget()
        self.customers.place_forget()
        self.tableframe10.place_forget()
        self.itemframe.place(self.itemframeinfo)
        self.tableframe2.place(self.tableframe2info)

        # Label(self.itemframe, text="اختر اسم التاجر",font="robot 20 bold", fg="black", bg="white").grid(row=0, column=3)
        self.profiles = Entry(self.itemframe, font="robot 14", textvariable=self.merchant)
        self.profiles.grid(row=0, column=3)
        self.merchant.set("اختر اسم التاجر")

        # Table for added items
        self.Table()

        # enteries
        self.recite_date = Entry(self.itemframe, bg="light gray")
        self.recite_date.grid(row=4, column=4)
        self.entered_date = Entry(self.itemframe, bg="light gray")
        self.entered_date.grid(row=6, column=4)
        self.recite_id = Entry(self.itemframe, bg="light gray")
        self.recite_id.grid(row=8, column=4)
        self.supervisor = Entry(self.itemframe, bg="light gray")
        self.supervisor.grid(row=10, column=4)
        self.recite_total_price = Entry(self.itemframe, bg="light gray")
        self.recite_total_price.grid(row=12, column=4)
        self.payed = Entry(self.itemframe, bg="light gray")
        self.payed.grid(row=14, column=4)

        self.product_name = Entry(self.itemframe, bg="light gray")
        self.product_name.grid(row=4, column=3)
        self.quantity = Entry(self.itemframe, bg="light gray")
        self.quantity.grid(row=6, column=3)
        self.storeroom = Entry(self.itemframe, bg="light gray")
        self.storeroom.grid(row=8, column=3)
        self.piece_price = Entry(self.itemframe, bg="light gray")
        self.piece_price.grid(row=10, column=3)
        self.unit_price = Entry(self.itemframe, bg="light gray")
        self.unit_price.grid(row=12, column=3)

        self.total_price = Entry(self.itemframe, bg="light gray")
        self.total_price.grid(row=14, column=3)



        today_income = Button(self.itemframe, text="وارد اليوم", font="robot 16 bold", fg="black", bg="#4267b2",
                              command=self.Today_Income)
        today_income.grid(row=0, column=5)

        history_income = Button(self.itemframe, text="سجل الوارد", font="robot 16 bold", fg="black", bg="#4267b2",
                                command=self.income_history)
        history_income.grid(row=0, column=4)

        add_income = Button(self.itemframe, text="اضافة الصنف", font="robot 16 bold", fg="black", bg="#4267b2",
                            command=self.Add_Income)
        add_income.grid(row=0, column=2)

        add_receipt = Button(self.itemframe, text="اضافة الفاتورة", font="robot 16 bold", fg="black", bg="#4267b2",
                             command=self.Add_Recipte)
        add_receipt.grid(row=0, column=1)

        delete_item = Button(self.itemframe, text="حذف صنف", font="robot 16 bold", fg="black", bg="#4267b2",
                             command=self.delete_item)
        delete_item.grid(row=14, column=2)

        return_item = Button(self.itemframe, text="مرتجعات", font="robot 16 bold", fg="black", bg="#4267b2",
                             command=self.returns)
        return_item.grid(row=14, column=1)

        # labels

        self.recite_date_label = Label(self.itemframe, text=":تاريخ الفاتورة          ", font="roboto 14 bold")
        self.recite_date_label.grid(row=3, column=4)
        self.entered_date_label = Label(self.itemframe, text=":تاريخ ادخال الفاتورة         ", font="roboto 14 bold")
        self.entered_date_label.grid(row=5, column=4)
        self.recite_id_label = Label(self.itemframe, text=":رقم الفاتورة              ", font="roboto 14 bold")
        self.recite_id_label.grid(row=7, column=4)
        self.supervisor_label = Label(self.itemframe, text=":اسم المستلم              ", font="roboto 14 bold")
        self.supervisor_label.grid(row=9, column=4)
        self.recite_total_price_label = Label(self.itemframe, text=":اجمالي الفاتورة               ",
                                              font="roboto 14 bold")
        self.recite_total_price_label.grid(row=11, column=4)
        self.payed_label = Label(self.itemframe, text=":مدفوع                       ", font="roboto 14 bold")
        self.payed_label.grid(row=13, column=4)

        self.product_name_label = Label(self.itemframe, text=":اسم الصنف     ", font="roboto 14 bold", bg="#FFFFFF")
        self.product_name_label.grid(row=3, column=3)
        self.quantity_label = Label(self.itemframe, text=":الكمية           ", font="roboto 14 bold", bg="#FFFFFF")
        self.quantity_label.grid(row=5, column=3)
        self.storeroom_label = Label(self.itemframe, text=":رقم المخزن    ", font="roboto 14 bold", bg="#FFFFFF")
        self.storeroom_label.grid(row=7, column=3)
        self.piece_price_label = Label(self.itemframe, text=":سعر القطعة    ", font="roboto 14 bold", bg="#FFFFFF")
        self.piece_price_label.grid(row=9, column=3)
        self.unit_price_label = Label(self.itemframe, text=":سعر الوحدة           ", font="roboto 14 bold",
                                      bg="#FFFFFF")

        self.unit_price_label.grid(row=11, column=3)

        self.total_price_label = Label(self.itemframe, text=":سعر الكمية           ", font="roboto 14 bold",
                                       bg="#FFFFFF")
        self.total_price_label.grid(row=13, column=3)

        today = datetime.date(datetime.now())
        format_date = str(today.strftime("%d/%m/%Y"))
        date = format_date

        self.recite_date.delete(0, END)
        self.recite_date.insert(0, date)
        self.entered_date.delete(0, END)
        self.entered_date.insert(0, date)


    def returns(self):
        self.tableframe8.place_forget()
        self.formframe1.place_forget()
        self.salesframe2.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemframe.place_forget()
        self.tableframe2.place_forget()
        self.salesframe.place_forget()
        self.marketfrme.place_forget()
        self.storesframe.place_forget()
        self.returnframe.place(self.returnframeinfo)
        self.tableframe3.place(self.tableframe3info)
        self.tableframe4.place_forget()
        self.tableframe5.place_forget()
        self.tableframe6.place_forget()
        self.tableframe7.place_forget()
        self.customers.place_forget()
        self.tableframe10.place_forget()


        self.return_table()

        self.return_merchant = Entry(self.returnframe, bg="light gray")
        self.return_merchant.grid(row=1, column=7)

        self.return_date = Entry(self.returnframe, bg="light gray")
        self.return_date.grid(row=3, column=7)

        self.return_recite_id = Entry(self.returnframe, bg="light gray")
        self.return_recite_id.grid(row=5, column=7)

        self.return_product_name = Entry(self.returnframe, bg="light gray")
        self.return_product_name.grid(row=7, column=7)
        self.return_storeroom = Entry(self.returnframe, bg="light gray")
        self.return_storeroom.grid(row=9, column=7)
        self.return_quantity = Entry(self.returnframe, bg="light gray")
        self.return_quantity.grid(row=11, column=7)
        self.return_total_price = Entry(self.returnframe, bg="light gray")
        self.return_total_price.grid(row=13, column=7)

        self.return_merchant_label = Label(self.returnframe, text=":اسم التاجر          ", font="roboto 14 bold")
        self.return_merchant_label.grid(row=0, column=7)
        self.return_date_label = Label(self.returnframe, text=":تاريخ الارجاع         ", font="roboto 14 bold")
        self.return_date_label.grid(row=2, column=7)
        self.return_recite_id_label = Label(self.returnframe, text=":رقم الفاتورة              ", font="roboto 14 bold")
        self.return_recite_id_label.grid(row=4, column=7)
        self.return_product_name_label = Label(self.returnframe, text=":اسم الصنف        ", font="roboto 14 bold")
        self.return_product_name_label.grid(row=6, column=7)
        self.return_product_name_label = Label(self.returnframe, text=":رقم المخزن        ", font="roboto 14 bold")
        self.return_product_name_label.grid(row=8, column=7)
        self.return_quantity_label = Label(self.returnframe, text=":الكمية المرتجعة        ",
                                           font="roboto 14 bold")
        self.return_quantity_label.grid(row=10, column=7)
        self.return_total_price_label = Label(self.returnframe, text=":سعر الكمية المرتجعة              ",
                                              font="roboto 14 bold")
        self.return_total_price_label.grid(row=12, column=7)



        self.return_product_button = Button(self.returnframe, text="اضافة الصنف", font="robot 16 bold", fg="black",
                                            bg="#4267b2", width=18, command=self.Returened_product)
        self.return_product_button.grid(row=1, column=0)

        self.return_recite_button = Button(self.returnframe, text="اضافة للمرتجعات", font="robot 16 bold", fg="black",
                                           bg="#4267b2", width=18, command=self.return_recite)
        self.return_recite_button.grid(row=3, column=0)

        self.return_history_button = Button(self.returnframe, text="سجل المرتجعات", font="robot 16 bold", fg="black",
                                            bg="#4267b2", width=18, command=self.return_history)
        self.return_history_button.grid(row=5, column=0)

        self.return_delete_button = Button(self.returnframe, text="حذف", font="robot 16 bold", fg="black",
                                            bg="yellow", width=18, command=self.delete_returned_item)
        self.return_delete_button.grid(row=7, column=0)

    def return_table(self):
        scrollbarx = Scrollbar(self.tableframe3, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe3, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe3,
                                 columns=("Merchant", "Product Name", "Storeroom", "Description", "Category"),
                                 selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=80)

        self.tree.heading('Merchant', text="اسم التاجر", anchor=W)
        self.tree.heading('Product Name', text="اسم الصنف", anchor=W)
        self.tree.heading('Storeroom', text="رقم المخزن", anchor=W)
        self.tree.heading('Description', text="الكمية", anchor=W)
        self.tree.heading('Category', text="سعر الوحدة", anchor=W)

        self.tree.grid(row=0, column=2, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=1, column=2, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=0, column=3, sticky="ns", pady=30)

    def Returened_product(self):
        self.cur.execute("select merchant_name from merchants;")
        names = self.cur.fetchall()
        merchant_list = names
        merchant_list = ([tup[0] for tup in merchant_list])

        self.cur.execute("select recite_id from today_income;")
        id = self.cur.fetchall()
        id_list = id
        id_list = ([tup[0] for tup in id_list])

        self.cur.execute("select product_Storeroom from stores;")
        storeroom = self.cur.fetchall()
        storeroom_list = storeroom
        storeroom_list = ([tup[0] for tup in storeroom_list])

        try:
            self.returned_merchant = str(self.return_merchant.get())
            self.return_id = int(self.return_recite_id.get())
            self.returned_date = str(self.return_date.get())
            self.returned_product_name = str(self.return_product_name.get())
            self.returned_storeroom = int(self.return_storeroom.get())
            self.returned_quantity = int(self.return_quantity.get())
            self.returned_price = float(self.return_total_price.get())
        except:
            messagebox.showerror("خطأ", "من فضلك قم بادخال كل المعلومات صحيحة")
            return

        if self.returned_merchant not in merchant_list:
            messagebox.showerror("خطأ", "هذا الاسم غير موجود بقائمة التجار!")
            return

        if self.return_id not in id_list:
            messagebox.showerror("خطأ", "هذه الفاتورة غير مسجلة بقائمة الوارد!")
            return

        if self.returned_storeroom not in storeroom_list:
            messagebox.showerror("خطأ", "لا يوجد لديك مخزن بهذا الرقم!")
            return

        if self.returned_merchant == '' or self.return_id == '' or self.returned_date == '':
            messagebox.showerror("خطأ", "من فضلك قم بادخال كل المعلومات صحيحة")
            return
        elif self.returned_product_name == '' or self.returned_quantity == '' or self.returned_price == '':
            messagebox.showerror("خطأ", "من فضلك قم بادخال كل المعلومات صحيحة")
            return
        elif self.returned_storeroom == "":
            messagebox.showerror("خطأ", "من فضلك قم بادخال كل المعلومات صحيحة")
            return

        info_list = [self.returned_product_name, self.returned_storeroom, self.returned_price]
        #self.cur.execute("drop table returns;")
        self.cur.execute("create table if not exists returns"
                         "(return_merchant_name varchar(30) not null,"
                         "return_date varchar(30) not null,"
                         "return_recite_id int,"
                         "return_product_name varchar(30) not null,"
                         "return_storeroom integer not null,"
                         "return_quantity int not null,"
                         "return_total_price float not null,"
                         "FOREIGN KEY (return_merchant_name) REFERENCES merchants(merchant_name));")

        self.cur.execute("insert into returns values(?,?,?,?,?,?,?)", (
            str(self.returned_merchant),
            str(self.returned_date),
            int(self.return_id),
            str(self.returned_product_name),
            int(self.returned_storeroom),
            int(self.returned_quantity),
            float(self.returned_price)))

        self.cur.execute("select product_name from stores;")
        ex_product_in_stores = self.cur.fetchall()
        self.ex_product_in_stores = ([tup[0] for tup in ex_product_in_stores])

        if self.returned_product_name not in self.ex_product_in_stores:
            messagebox.showerror("خطأ", "هذا الصنف غير موجود بالمخزن")
            return

        if self.returned_product_name in self.ex_product_in_stores:
            counter = 0
            self.cur.execute("select product_name from stores where  "
                             "product_name=? and product_Storeroom=? and product_unit_price=?;",
                             (str(self.returned_product_name),
                              int(self.returned_storeroom),
                              float(self.returned_price)))
            match_name = self.cur.fetchall()
            self.match_name = ([tup[0] for tup in match_name])
            self.match_name = self.match_name[0]


            self.cur.execute("select product_Storeroom from stores where  "
                             "product_name=? and product_Storeroom =? and product_unit_price=?;",
                             (str(self.returned_product_name),
                              int(self.returned_storeroom),
                              float(self.returned_price)))

            match_storeroom = self.cur.fetchall()
            self.match_storeroom = ([tup[0] for tup in match_storeroom])
            self.match_storeroom = self.match_storeroom[0]

            self.cur.execute("select product_unit_price from stores where  "
                             "product_name=? and product_Storeroom =? and product_unit_price=?;",
                             (str(self.returned_product_name),
                              int(self.returned_storeroom),
                              float(self.returned_price)))

            match_unit_price = self.cur.fetchall()
            self.match_unit_price = ([tup[0] for tup in match_unit_price])
            self.match_unit_price = self.match_unit_price[0]

            self.match_all = [self.match_name, self.match_storeroom, self.match_unit_price]

            if self.match_all != "":
                for element in info_list:
                    if element in self.match_all:
                        counter += 1

            if counter == 3:
                self.cur.execute("select product_quantity from stores where product_name = ?"
                                 "and product_Storeroom=? and product_unit_price=?",
                                 (str(self.returned_product_name),
                                  int(self.returned_storeroom),
                                  float(self.returned_price)))
                quantity_before = self.cur.fetchall()
                self.quantity_before = ([tup[0] for tup in quantity_before])
                self.quantity_before = self.quantity_before[0]

                self.quantity_after_returning = int(abs(self.returned_quantity - self.quantity_before))

                self.cur.execute("update stores set product_quantity=? where product_name = ? and product_Storeroom=?"
                                 "and product_unit_price=?",
                                 (int(self.quantity_after_returning),
                                  str(self.returned_product_name),
                                  int(self.returned_storeroom),
                                  float(self.returned_price)))

        try:
            self.cur.execute("select recite_total_price from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?",
                             (int(self.return_id),
                              str(self.returned_product_name),
                              int(self.returned_storeroom),
                              float(self.returned_price),
                              str(self.returned_merchant)))
            total_recite_price_before = self.cur.fetchall()
            self.total_recite_price_before = ([tup[0] for tup in total_recite_price_before])
            self.total_recite_price_before = self.total_recite_price_before[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return

        try:
            self.cur.execute("select product_unit_price from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=? ",
                             (int(self.return_id),
                              str(self.returned_product_name),
                              int(self.returned_storeroom),
                              float(self.returned_price),
                              str(self.returned_merchant)))
            unit_price = self.cur.fetchall()
            self.unit_price_return = ([tup[0] for tup in unit_price])
            self.unit_price_return = self.unit_price_return[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return

        try:
            self.cur.execute("select payed from today_income where recite_id = ? and name_of_merchant=?",
                             (int(self.return_id),
                              str(self.returned_merchant)))
            payed = self.cur.fetchall()
            self.old_payed00 = ([tup[0] for tup in payed])
            self.old_payed00 = float(self.old_payed00[0])
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return

        self.cur.execute("select remaining from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?;",
                             (int(self.return_id),
                              str(self.returned_product_name),
                              int(self.returned_storeroom),
                              float(self.returned_price),
                              str(self.returned_merchant)))
        remaining_before = self.cur.fetchall()
        self.remaining_before = ([tup[0] for tup in remaining_before])
        self.remaining_before = self.remaining_before[0]

        self.total_quantity_price_returned = float((self.returned_quantity * self.unit_price_return))
        self.total_recite_price_after = float(self.total_recite_price_before - self.total_quantity_price_returned)
        self.remaining_after_return = float(self.total_recite_price_after - self.old_payed00)

        self.cur.execute("update today_income set recite_total_price = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.total_recite_price_after),
                          int(self.return_id),
                          str(self.returned_merchant)))

        self.cur.execute("update today_income set remaining = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.remaining_after_return),
                          int(self.return_id),
                          str(self.returned_merchant)))


        try:
            self.cur.execute("select product_quantity from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?;",
                             (int(self.return_id),
                              str(self.returned_product_name),
                              int(self.returned_storeroom),
                              float(self.returned_price),
                              str(self.returned_merchant)))
            product_quantity_before = self.cur.fetchall()
            self.product_quantity_before = ([tup[0] for tup in product_quantity_before])
            self.product_quantity_before = self.product_quantity_before[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return

        self.product_quantity_after = int(abs(self.product_quantity_before - self.returned_quantity))

        self.cur.execute("update today_income set product_quantity = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.product_quantity_after),
                          int(self.return_id),
                          str(self.returned_merchant)))

        self.cur.execute("select product_total_price from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?;",
                             (int(self.return_id),
                              str(self.returned_product_name),
                              int(self.returned_storeroom),
                              float(self.returned_price),
                              str(self.returned_merchant)))


        total_quantity_price_before = self.cur.fetchall()
        self.total_quantity_price_before = ([tup[0] for tup in total_quantity_price_before])
        self.total_quantity_price_before = self.total_quantity_price_before[0]

        self.total_quantity_price_after = float(self.total_quantity_price_before - (self.returned_quantity * self.unit_price_return))

        self.cur.execute("update today_income set product_total_price = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.total_quantity_price_after),
                          int(self.return_id),
                          str(self.returned_merchant)))
        '''
        self.cur.execute("delete from today_income where recite_id = ? and product_name=? and product_Storeroom=? and "
                         "product_unit_price=? and name_of_merchant=?;",
                         (int(self.return_id),
                          str(self.returned_product_name),
                          int(self.returned_storeroom),
                          float(self.returned_price),
                          str(self.returned_merchant)))
        '''
        self.cur.execute('select debt from merchants where merchant_name=?', (self.returned_merchant,))
        debt_before = self.cur.fetchall()
        self.debt_before = ([tup[0] for tup in debt_before])
        self.debt_before = float(self.debt_before[0])
        self.debt_before = float(abs(self.old_debt - self.remaining_before))

        self.debt_after = float(self.debt_before - self.total_quantity_price_returned)
        self.cur.execute('update merchants set debt=? where merchant_name=?', (self.debt_after, self.returned_merchant,))

        self.base.commit()
        self.insert_store()
        self.get_returns()

    def get_returns(self):
        ans = ''
        self.return_table()
        self.cur.execute(
            "select return_merchant_name, return_product_name, return_storeroom, return_quantity, return_total_price from returns;")
        productlist = self.cur.fetchall()
        x = 0
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def return_recite(self):
        if messagebox.askyesno("تنبيه", "هل تريد ارجاع الأصناف التالية") == True:
            #self.cur.execute("drop table returns_history;")
            self.cur.execute("create table if not exists returns_history"
                             "(return_merchant_name varchar(30) not null,"
                             "return_date varchar(30) not null,"
                             "return_recite_id int,"
                             "return_product_name varchar(30) not null,"
                             "return_storeroom integer not null,"
                             "return_quantity int not null,"
                             "return_total_price float not null,"
                             "FOREIGN KEY (return_merchant_name) REFERENCES merchants(merchant_name));")
            self.cur.execute("INSERT INTO returns_history select * FROM returns;")
            self.cur.execute("delete from returns;")
            self.base.commit()
            self.returns()
    def table11(self):
        scrollbarx = Scrollbar(self.tableframe11, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe11, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe11,
                                 columns=(
                                 "Merchant", "Date", "Id", "Product Name", "Storeroom", "Description", "Category"),
                                 selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=80)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=80)
        self.tree.column('#5', stretch=NO, minwidth=0, width=80)
        self.tree.column('#6', stretch=NO, minwidth=0, width=80)

        self.tree.heading('Merchant', text="اسم التاجر", anchor=W)
        self.tree.heading('Date', text="تاريخ الارجاع", anchor=W)
        self.tree.heading('Id', text="رقم الفاتورة", anchor=W)
        self.tree.heading('Product Name', text="اسم الصنف", anchor=W)
        self.tree.heading('Storeroom', text="رقم المخزن", anchor=W)
        self.tree.heading('Description', text="الكمية", anchor=W)
        self.tree.heading('Category', text="سعر الكمية", anchor=W)

        self.tree.grid(row=1, column=1, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=1, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=2, sticky="ns", pady=30)

    def insertion(self):
        self.cur.execute("select * from returns_history;")
        productlist = self.cur.fetchall()
        self.table11()
        x = 0
        ans = ''
        for i in productlist:
            self.tree.insert('', 'end', values=i)
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]
        return ans

    def return_history(self):
        self.return_history_w = Tk()
        width = 800
        height = 550
        screen_width = self.return_history_w.winfo_screenwidth()
        screen_height = self.return_history_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.return_history_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.return_historyframe = Frame(self.return_history_w, width=800, height=500, bg="#FFFFFF")
        self.return_historyframe.place(x=0, y=70, anchor=NW)
        self.return_historyframeinfo = self.return_historyframe.place_info()

        self.tableframe11 = LabelFrame(self.return_history_w, width=175, height=200, bg="light gray")
        self.tableframe11.place(x=750, y=70, anchor=NE)
        self.tableframe11info = self.tableframe11.place_info()
        self.table11()
        self.insertion()
        self.search_return_history_entry = Entry(self.return_history_w, bg="light grey", font="robot 14")
        self.search_return_history_entry.place(x=500, y=20)

        self.search_return_history_date = Button(self.return_history_w, text="بحث بالتاريخ", font="robot 16 bold", fg="black",
                                             bg="#4267b2",
                                             command=self.search_date_returns)

        self.search_return_history_date.place(x=360, y=15)

        self.search_return_history_name = Button(self.return_history_w, text="بحث بالصنف", font="robot 16 bold", fg="black",
                                             bg="#4267b2",
                                             command=self.search_name_returns)

        self.search_return_history_name.place(x=215, y=15)

        self.search_return_history_merchant = Button(self.return_history_w, text="بحث بالتاجر", font="robot 16 bold", fg="black",
                                             bg="#4267b2",
                                             command=self.search_merchant_returns)

        self.search_return_history_merchant.place(x=70, y=15)

        self.return_history_w.mainloop()

    def search_date_returns(self):
        ans = ''
        try:
            self.get_search_return_history = str(self.search_return_history_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل التاريخ بشكل صحيح")
            return
        if self.get_search_return_history == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة التاريخ")
            return
        self.cur.execute(
            'select * from returns_history'
            ' where return_date=?', (self.get_search_return_history,))
        result = self.cur.fetchall()
        self.table11()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def search_name_returns(self):
        ans = ''
        try:
            self.get_search_return_history = str(self.search_return_history_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل اسم الصنف بشكل صحيح")
            return
        if self.get_search_return_history == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم الصنف")
            return
        self.cur.execute(
            'select * from returns_history'
            ' where return_product_name=?', (self.get_search_return_history,))
        result = self.cur.fetchall()
        self.table11()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def search_merchant_returns(self):
        ans = ''
        try:
            self.get_search_return_history = str(self.search_return_history_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل اسم التاجر بشكل صحيح")
            return
        if self.get_search_return_history == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم التاجر")
            return
        self.cur.execute(
            'select * from returns_history'
            ' where return_merchant_name=?', (self.get_search_return_history,))
        result = self.cur.fetchall()
        self.table11()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def delete_returned_item(self):
        self.delete_returned_item_w = Tk()
        width = 380
        height = 250
        screen_width = self.delete_returned_item_w.winfo_screenwidth()
        screen_height = self.delete_returned_item_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.delete_returned_item_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.delete_returned_entry_merchant = Entry(self.delete_returned_item_w, bg="light grey", font="robot 14")
        self.delete_returned_entry_merchant.grid(row=2, column=1)
        self.delete_returned_label_merchant = Label(self.delete_returned_item_w, text="ادخل اسم التاجر", font="roboto 14 bold",
                                           bg="#FFFFFF")
        self.delete_returned_label_merchant.grid(row=2, column=2)

        self.delete_returned_entry_product = Entry(self.delete_returned_item_w, bg="light grey", font="robot 14")
        self.delete_returned_entry_product.grid(row=3, column=1)
        self.delete_returned_label_product = Label(self.delete_returned_item_w, text="ادخل اسم الصنف", font="roboto 14 bold", bg="#FFFFFF")
        self.delete_returned_label_product.grid(row=3, column=2)

        self.delete_returned_entry_id = Entry(self.delete_returned_item_w, bg="light grey", font="robot 14")
        self.delete_returned_entry_id.grid(row=4, column=1)
        self.delete_returned_label_id = Label(self.delete_returned_item_w, text="ادخل رقم الفاتورة", font="roboto 14 bold",
                                           bg="#FFFFFF")
        self.delete_returned_label_id.grid(row=4, column=2)

        self.delete_returned_entry_storeroom = Entry(self.delete_returned_item_w, bg="light grey", font="robot 14")
        self.delete_returned_entry_storeroom.grid(row=5, column=1)
        self.delete_returned_label_storeroom = Label(self.delete_returned_item_w, text="ادخل رقم المخزن", font="roboto 14 bold", bg="#FFFFFF")
        self.delete_returned_label_storeroom.grid(row=5, column=2)

        self.delete_returned_entry_quantity = Entry(self.delete_returned_item_w, bg="light grey", font="robot 14")
        self.delete_returned_entry_quantity.grid(row=6, column=1)
        self.delete_returned_label_quantity = Label(self.delete_returned_item_w, text="ادخل الكمية", font="roboto 14 bold", bg="#FFFFFF")
        self.delete_returned_label_quantity.grid(row=6, column=2)

        self.delete_returned_entry_price = Entry(self.delete_returned_item_w, bg="light grey", font="robot 14")
        self.delete_returned_entry_price.grid(row=7, column=1)
        self.delete_returned_label_price = Label(self.delete_returned_item_w, text="ادخل سعر الوحدة", font="roboto 14 bold", bg="#FFFFFF")
        self.delete_returned_label_price.grid(row=7, column=2)

        self.delete_returned_button = Button(self.delete_returned_item_w, text="حذف", font="robot 16 bold", fg="black", bg="yellow",
                                    command=self.final_delete_returned_item)

        self.delete_returned_button.grid(row=8, column=1)
        self.delete_returned_item_w.mainloop()

    def final_delete_returned_item(self):
        self.get_delete_returned_entry_merchant = str(self.delete_returned_entry_merchant.get())
        self.get_delete_returned_entry_product = str(self.delete_returned_entry_product.get())
        self.get_delete_returned_entry_id = int(self.delete_returned_entry_id.get())
        self.get_delete_returned_entry_storeroom = int(self.delete_returned_entry_storeroom.get())
        self.get_delete_returned_entry_quantity = int(self.delete_returned_entry_quantity.get())
        self.get_delete_returned_entry_price = float(self.delete_returned_entry_price.get())

        li = [self.delete_returned_entry_storeroom, self.delete_returned_entry_product, self.delete_returned_entry_price]

        # self.cur.execute("delete from stores;")

        self.cur.execute("select return_product_name from returns;")
        ex_product = self.cur.fetchall()
        self.ex_product_delete = ([tup[0] for tup in ex_product])

        if self.get_delete_returned_entry_product not in self.ex_product_delete:
            messagebox.showerror("خطأ", "هذا الصنف غير موجود")
            return

        if self.get_delete_returned_entry_product in self.ex_product_delete:
            self.cur.execute("select product_quantity from stores where product_name = ? "
                             "and product_Storeroom=? "
                             "and product_unit_price=?", (str(self.get_delete_returned_entry_product),
                                                          int(self.get_delete_returned_entry_storeroom),
                                                          float(self.get_delete_returned_entry_price)))
            old_quantity = self.cur.fetchall()
            self.old_quantity101 = ([tup[0] for tup in old_quantity])
            self.old_quantity101 = self.old_quantity101[0]

            self.new_quantity101 = int(self.get_delete_returned_entry_quantity + self.old_quantity101)

        self.cur.execute("delete from returns where return_product_name = ?;", (self.get_delete_returned_entry_product,))

        self.cur.execute("update stores set product_quantity = ? where product_Storeroom=? and product_name=?"
                         "and product_unit_price=?",
                         (int(self.new_quantity101),
                          int(self.get_delete_returned_entry_storeroom),
                          str(self.get_delete_returned_entry_product),
                          float(self.get_delete_returned_entry_price)))

        try:
            self.cur.execute("select recite_total_price from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?",
                             (int(self.get_delete_returned_entry_id),
                              str(self.get_delete_returned_entry_product),
                              int(self.get_delete_returned_entry_storeroom),
                              float(self.get_delete_returned_entry_price),
                              str(self.get_delete_returned_entry_merchant)))
            total_recite_price_before = self.cur.fetchall()
            self.total_recite_price_before1 = ([tup[0] for tup in total_recite_price_before])
            self.total_recite_price_before1 = self.total_recite_price_before1[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return

        try:
            self.cur.execute("select product_unit_price from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=? ",
                             (int(self.get_delete_returned_entry_id),
                              str(self.get_delete_returned_entry_product),
                              int(self.get_delete_returned_entry_storeroom),
                              float(self.get_delete_returned_entry_price),
                              str(self.get_delete_returned_entry_merchant)))
            unit_price = self.cur.fetchall()
            self.unit_price_return1 = ([tup[0] for tup in unit_price])
            self.unit_price_return1 = self.unit_price_return1[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return

        try:
            self.cur.execute("select payed from today_income where recite_id = ? and name_of_merchant=?",
                             (int(self.get_delete_returned_entry_id),
                              str(self.get_delete_returned_entry_merchant)))
            payed = self.cur.fetchall()
            self.old_payed000 = ([tup[0] for tup in payed])
            self.old_payed000 = float(self.old_payed000[0])
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return

        self.cur.execute("select remaining from today_income where recite_id = ? and product_name=? "
                         "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?;",
                         (int(self.get_delete_returned_entry_id),
                          str(self.get_delete_returned_entry_product),
                          int(self.get_delete_returned_entry_storeroom),
                          float(self.get_delete_returned_entry_price),
                          str(self.get_delete_returned_entry_merchant)))
        remaining_before = self.cur.fetchall()
        self.remaining_before1 = ([tup[0] for tup in remaining_before])
        self.remaining_before1 = self.remaining_before1[0]

        self.total_quantity_price_returned1 = float((self.get_delete_returned_entry_quantity * self.unit_price_return1))
        self.total_recite_price_after1 = float(self.total_recite_price_before1 + self.total_quantity_price_returned1)
        self.remaining_after_return1 = float(self.total_recite_price_after1 - self.old_payed000)

        self.cur.execute("update today_income set recite_total_price = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.total_recite_price_after1),
                          int(self.get_delete_returned_entry_id),
                          str(self.get_delete_returned_entry_merchant)))

        self.cur.execute("update today_income set remaining = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.remaining_after_return1),
                          int(self.get_delete_returned_entry_id),
                          str(self.get_delete_returned_entry_merchant)))

        try:
            self.cur.execute("select product_quantity from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?;",
                             (int(self.get_delete_returned_entry_id),
                              str(self.get_delete_returned_entry_product),
                              int(self.get_delete_returned_entry_storeroom),
                              float(self.get_delete_returned_entry_price),
                              str(self.get_delete_returned_entry_merchant)))
            product_quantity_before = self.cur.fetchall()
            self.product_quantity_before1 = ([tup[0] for tup in product_quantity_before])
            self.product_quantity_before1 = self.product_quantity_before1[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return

        self.product_quantity_after1 = int(abs(self.product_quantity_before1 + self.get_delete_returned_entry_quantity))

        self.cur.execute("update today_income set product_quantity = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.product_quantity_after1),
                          int(self.get_delete_returned_entry_id),
                          str(self.get_delete_returned_entry_merchant)))

        self.cur.execute("select product_total_price from today_income where recite_id = ? and product_name=? "
                         "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?;",
                         (int(self.get_delete_returned_entry_id),
                          str(self.get_delete_returned_entry_product),
                          int(self.get_delete_returned_entry_storeroom),
                          float(self.get_delete_returned_entry_price),
                          str(self.get_delete_returned_entry_merchant)))

        total_quantity_price_before = self.cur.fetchall()
        self.total_quantity_price_before1 = ([tup[0] for tup in total_quantity_price_before])
        self.total_quantity_price_before1 = self.total_quantity_price_before1[0]

        self.total_quantity_price_after1 = float(
            self.total_quantity_price_before1 + (self.get_delete_returned_entry_quantity * self.unit_price_return1))

        self.cur.execute("update today_income set product_total_price = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.total_quantity_price_after1),
                          int(self.get_delete_returned_entry_id),
                          str(self.get_delete_returned_entry_merchant)))
        '''
        self.cur.execute("delete from today_income where recite_id = ? and product_name=? and product_Storeroom=? and "
                         "product_unit_price=? and name_of_merchant=?;",
                         (int(self.return_id),
                          str(self.returned_product_name),
                          int(self.returned_storeroom),
                          float(self.returned_price),
                          str(self.returned_merchant)))
        '''
        self.cur.execute('select debt from merchants where merchant_name=?', (self.get_delete_returned_entry_merchant,))
        debt_before = self.cur.fetchall()
        self.debt_before1 = ([tup[0] for tup in debt_before])
        self.debt_before1 = float(self.debt_before1[0])
        self.debt_before2 = float(abs(self.debt_before1 - self.remaining_before1))

        self.debt_after1 = float(self.debt_before1 + self.total_quantity_price_returned1)
        self.cur.execute('update merchants set debt=? where merchant_name=?',
                         (self.debt_after1, self.get_delete_returned_entry_merchant,))


        self.base.commit()
        self.delete_returned_item_w.destroy()
        self.get_returns()


    def Get(self, x=0):
        ans = ''
        self.Table()
        self.cur.execute(
            "select product_name,product_Storeroom, product_quantity, product_total_price,product_unit_price,"
            "name_of_merchant from new_income;")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def insert_into_new_income(self):
        self.cur.execute('insert into new_income values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (
            str(self.get_merchant),
            str(self.get_recite_date),
            str(self.get_entered_date),
            int(self.get_recite_id),
            str(self.get_supervisor),
            float(self.get_recite_total_price),
            float(self.get_payed),
            float(self.remaining),
            str(self.get_product_name),
            int(self.get_quantity),
            int(self.get_storeroom),
            float(self.get_piece_price),
            float(self.get_unit_price),
            float(self.get_total_price)))

    def Add_Income(self):
        self.cur.execute('CREATE TABLE if not exists merchants'
                         "(merchant_id INTEGER,"
                         "merchant_name VARCHAR(25),"
                         "debt float,"
                         "PRIMARY KEY (merchant_id, merchant_name));")
        # self.cur.execute("INSERT INTO merchants_copy select * FROM merchants;")
        # self.cur.execute("DROP TABLE new_income;")
        # self.cur.execute("ALTER TABLE merchants_copy RENAME TO merchants;")

        self.cur.execute("CREATE TABLE if not exists new_income"
                         "(name_of_merchant varchar(25) NOT NULL,"
                         "datetime_recite varchar(25) NOT NULL,"
                         "datetime_entered varchar(25) NOT NULL,"
                         "recite_id INTEGER NOT NULL,"
                         "supervisor varchar (30) NOT NULL,"
                         "recite_total_price FLOAT NOT NULL,"
                         "payed FLOAT NOT NULL,"
                         "remaining FLOAT NOT NULL,"
                         "product_name varchar (50) NOT NULL,"
                         "product_quantity INTEGER NOT NULL,"
                         "product_Storeroom INTEGER NOT NULL,"
                         "product_piece_price FLOAT NOT NULL,"
                         "product_unit_price FLOAT NOT NULL,"
                         "product_total_price FLOAT NOT NULL,"
                         "FOREIGN KEY (name_of_merchant) REFERENCES merchants(merchant_name));")

        self.cur.execute("select merchant_name from merchants;")
        names = self.cur.fetchall()
        merchant_list = names
        self.get_merchant = self.profiles.get()
        merchant_list = ([tup[0] for tup in merchant_list])
        if self.get_merchant not in merchant_list:
            messagebox.showerror("خطأ", "هذا الاسم غير موجود بقائمة التجار!")
            return

        elif self.get_merchant in merchant_list:

            try:
                self.get_recite_date = str(self.recite_date.get())
                self.get_recite_id = int(self.recite_id.get())
                self.get_supervisor = str(self.supervisor.get())
                self.get_recite_total_price = float(self.recite_total_price.get())
                self.get_payed = float(self.payed.get())
                self.get_entered_date = str(self.entered_date.get())

                self.get_product_name = str(self.product_name.get())
                self.get_quantity = int(self.quantity.get())
                self.get_storeroom = int(self.storeroom.get())
                self.get_piece_price = float(self.piece_price.get())
                self.get_unit_price = float(self.unit_price.get())
                self.get_total_price = float(self.total_price.get())
            except:
                messagebox.showerror("خطأ", "من فضلك ادخل بيانات صحيحة")
                return

            if self.get_recite_date == "" or self.get_recite_id == "" or self.get_supervisor == "":
                messagebox.showerror("خطأ", "يجب ملأ جميع البيانات")
            elif self.get_recite_total_price == "" or self.get_payed == "" or self.get_entered_date == "":
                messagebox.showerror("خطأ", "يجب ملأ جميع البيانات")
            elif self.get_product_name == "" or self.get_quantity == "":
                messagebox.showerror("خطأ", "برجاء ادخال جميع البيانات")
            elif self.get_storeroom == "" or self.get_piece_price == "" or self.get_unit_price == "":
                messagebox.showerror("خطأ", "برجاء ادخال جميع البيانات")
            elif self.get_total_price == "":
                messagebox.showerror("خطأ", "برجاء ادخال جميع البيانات")

            self.remaining = float(self.get_recite_total_price) - float(self.get_payed)

            self.cur.execute("select name_of_merchant from new_income;")
            new_income_merchant = self.cur.fetchall()
            self.new_income_merchant = ([tup[0] for tup in new_income_merchant])

            self.cur.execute("select datetime_recite from new_income;")
            new_recite_date = self.cur.fetchall()
            self.new_recite_date = ([tup[0] for tup in new_recite_date])

            self.cur.execute("select datetime_entered from new_income;")
            new_entered_date = self.cur.fetchall()
            self.new_entered_date = ([tup[0] for tup in new_entered_date])

            self.cur.execute("select recite_id from new_income;")
            new_recite_id = self.cur.fetchall()
            self.new_recite_id = ([tup[0] for tup in new_recite_id])

            self.cur.execute("select supervisor from new_income;")
            new_supervisor = self.cur.fetchall()
            self.new_supervisor = ([tup[0] for tup in new_supervisor])

            self.cur.execute("select recite_total_price from new_income;")
            new_recite_total = self.cur.fetchall()
            self.new_recite_total = ([tup[0] for tup in new_recite_total])

            self.cur.execute("select payed from new_income;")
            new_payed = self.cur.fetchall()
            self.new_payed = ([tup[0] for tup in new_payed])

            if self.new_income_merchant == []:
               self.insert_into_new_income()

            elif self.new_income_merchant != []:
                self.new_income_merchant = self.new_income_merchant[0]
                self.new_recite_date = self.new_recite_date[0]
                self.new_entered_date = self.new_entered_date[0]
                self.new_recite_id = self.new_recite_id[0]
                self.new_supervisor = self.new_supervisor[0]
                self.new_recite_total = self.new_recite_total[0]
                self.new_payed = self.new_payed[0]
                li1 = [self.new_income_merchant, self.new_recite_date, self.new_entered_date, self.new_recite_id,
                      self.new_supervisor, self.new_recite_total,  self.new_payed]
                li2 = [self.get_merchant, self.get_recite_date, self.get_entered_date, self.get_recite_id,
                       self.get_supervisor, self.get_recite_total_price, self.get_payed]
                counter = 0
                for i in li2:
                    if i not in li1:
                        messagebox.showerror("خطأ", "لا يمكنك تغيير هذه المعلومات في نفس الفاتورة")
                        return
                    elif i in li1:
                        counter = counter + 1
                        if counter == 7:
                            self.insert_into_new_income()


            li = [self.get_storeroom, self.get_product_name, self.get_unit_price]

            #self.cur.execute("delete from stores;")
            self.cur.execute("create table if not exists stores"
                             "(product_Storeroom integer not null,"
                             "product_name varchar(30) not null,"
                             "product_quantity integer not null,"
                             "product_unit_price float not null);")


            self.cur.execute("select product_name from stores;")
            ex_product = self.cur.fetchall()
            self.ex_product = ([tup[0] for tup in ex_product])

            if self.get_product_name not in self.ex_product:
                self.cur.execute("insert into stores select product_Storeroom, product_name, product_quantity,"
                                 "product_unit_price from new_income;")

            if self.get_product_name in self.ex_product:

                counter = 0
                self.cur.execute("select product_Storeroom from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_storeroom),
                                  str(self.get_product_name),
                                  float(self.get_unit_price)))
                match = self.cur.fetchall()
                self.match1 = ([tup[0] for tup in match])
                print(self.match1)
                self.match1 = self.match1[0]

                self.cur.execute("select product_name from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_storeroom),
                                  str(self.get_product_name),
                                  float(self.get_unit_price)))

                match2 = self.cur.fetchall()
                self.match2 = ([tup[0] for tup in match2])
                self.match2 = self.match2[0]

                self.cur.execute("select product_unit_price from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_storeroom),
                                  str(self.get_product_name),
                                  float(self.get_unit_price)))

                match3 = self.cur.fetchall()
                self.match3 = ([tup[0] for tup in match3])
                self.match3 = self.match3[0]
                self.match = [self.match1, self.match2, self.match3]

                if self.match != "":
                    for i in li:
                        if i in self.match:
                            counter += 1

                if counter == 3:
                    self.cur.execute("select product_quantity from stores where product_name = ? "
                                     "and product_Storeroom=? "
                                     "and product_unit_price=?", (str(self.get_product_name),
                                                                  int(self.get_storeroom),
                                                                  float(self.get_unit_price)))
                    old_quantity = self.cur.fetchall()
                    self.old_quantity = ([tup[0] for tup in old_quantity])
                    self.old_quantity = self.old_quantity[0]

                    self.new_quantity = int(self.get_quantity + self.old_quantity)

                    self.cur.execute("update stores set product_quantity=? where product_name = ? and product_Storeroom=?"
                                     "and product_unit_price=?",
                                     (self.new_quantity,
                                      str(self.get_product_name),
                                      int(self.get_storeroom),
                                      float(self.get_unit_price)))


            self.new_text = ""
            self.product_name.delete(0, END)
            self.product_name.insert(0, self.new_text)

            self.quantity.delete(0, END)
            self.quantity.insert(0, self.new_text)

            self.storeroom.delete(0, END)
            self.storeroom.insert(0, self.new_text)

            self.piece_price.delete(0, END)
            self.piece_price.insert(0, self.new_text)

            self.unit_price.delete(0, END)
            self.unit_price.insert(0, self.new_text)

            self.total_price.delete(0, END)
            self.total_price.insert(0, self.new_text)

            self.Get()

            self.base.commit()

    def Add_Recipte(self):
        if messagebox.askyesno("تنبيه", "هل تريد اضافة هذه الفاتورة") == True:
            # self.cur.execute('drop table today_income;')ظ
            self.cur.execute("CREATE TABLE if not exists today_income"
                             "(name_of_merchant varchar(25) NOT NULL,"
                             "datetime_recite varchar(25) NOT NULL,"
                             "datetime_entered varchar(25) NOT NULL,"
                             "recite_id INTEGER NOT NULL,"
                             "supervisor varchar (30) NOT NULL,"
                             "recite_total_price FLOAT NOT NULL,"
                             "payed FLOAT NOT NULL,"
                             "remaining FLOAT NOT NULL,"
                             "product_name varchar (50) NOT NULL,"
                             "product_quantity INTEGER NOT NULL,"
                             "product_Storeroom INTEGER NOT NULL,"
                             "product_piece_price FLOAT NOT NULL,"
                             "product_unit_price FLOAT NOT NULL,"
                             "product_total_price FLOAT NOT NULL,"
                             "FOREIGN KEY (name_of_merchant) REFERENCES merchants(merchant_name));")

            self.cur.execute("INSERT INTO today_income select * FROM new_income;")

            self.cur.execute('select debt from merchants where merchant_name=?', (self.get_merchant,))
            old_debt = self.cur.fetchall()
            self.old_debt = ([tup[0] for tup in old_debt])
            if self.old_debt == []:
                self.old_debt.append(0)
            self.old_debt = float(self.old_debt[0])
            self.new_debt = float(self.old_debt + self.remaining)
            self.cur.execute('update merchants set debt=? where merchant_name=?', (self.new_debt, self.get_merchant,))
            #self.cur.execute("drop table stores")
            self.cur.execute("delete from new_income;")

            self.base.commit()
            self.new_text = ""

            self.recite_id.delete(0, END)
            self.recite_id.insert(0, self.new_text)
            self.supervisor.delete(0, END)
            self.supervisor.insert(0, self.new_text)
            self.recite_total_price.delete(0, END)
            self.recite_total_price.insert(0, self.new_text)
            self.payed.delete(0, END)
            self.payed.insert(0, self.new_text)

            self.Table()

    def Get_today_income(self, x=0):
        ans = ''
        today = datetime.date(datetime.now())
        self.dt_string = str(today.strftime("%d/%m/%Y"))
        self.today_date = self.dt_string
        self.cur.execute(
            "select * from today_income where datetime_entered=?", (self.today_date,))
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def Today_Income(self):
        self.todayincomew = Tk()
        width = 1400
        height = 400
        screen_width = self.todayincomew.winfo_screenwidth()
        screen_height = self.todayincomew.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.todayincomew.geometry("%dx%d+%d+%d" % (width, height, x, y))

        scrollbarx = Scrollbar(self.todayincomew, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.todayincomew, orient=VERTICAL)
        self.tree = ttk.Treeview(self.todayincomew,
                                 columns=("merchant_name", "receipt_date", "entered_date", "receipt_id",
                                          'supervisor', 'receipt_total_price', 'payed', 'remaining',
                                          'product_name',
                                          'quantity', 'storeroom', 'piece_price', 'unit_price', 'total_price'),
                                 selectmode="browse", height=16,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=10)
        self.tree.column('#1', stretch=NO, minwidth=0, width=65)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=80)
        self.tree.column('#5', stretch=NO, minwidth=0, width=50)
        self.tree.column('#6', stretch=NO, minwidth=0, width=80)
        self.tree.column('#7', stretch=NO, minwidth=0, width=50)
        self.tree.column('#8', stretch=NO, minwidth=0, width=50)
        self.tree.column('#9', stretch=NO, minwidth=0, width=100)
        self.tree.column('#10', stretch=NO, minwidth=0, width=100)
        self.tree.column('#11', stretch=NO, minwidth=0, width=50)
        self.tree.column('#12', stretch=NO, minwidth=0, width=80)
        self.tree.column('#13', stretch=NO, minwidth=0, width=80)

        self.tree.heading("merchant_name", text="اسم التاجر", anchor=W)
        self.tree.heading("receipt_date", text="تاريخ الفاتورة", anchor=W)
        self.tree.heading('entered_date', text="تاريخ الادخال", anchor=W)
        self.tree.heading('receipt_id', text="رقم الفاتورة", anchor=W)
        self.tree.heading('supervisor', text="المستلم", anchor=W)
        self.tree.heading('receipt_total_price', text="اجمالي الفاتورة", anchor=W)
        self.tree.heading('payed', text="المدفوع", anchor=W)
        self.tree.heading('remaining', text="الباقي", anchor=W)
        self.tree.heading('product_name', text="اسم الصنف", anchor=W)
        self.tree.heading('quantity', text="الكمية", anchor=W)
        self.tree.heading('storeroom', text="رقم المخزن", anchor=W)
        self.tree.heading('piece_price', text="سعر القطعة", anchor=W)
        self.tree.heading('unit_price', text="سعر الوحدة", anchor=W)
        self.tree.heading('total_price', text="سعر الكمية", anchor=W)

        self.tree.grid(row=2, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=2, column=1, sticky="ns", pady=30)

        self.Get_today_income()

        self.todayincomew.mainloop()

    def Get_history_income(self, x=0):
        ans = ''
        self.cur.execute(
            "select * from today_income;")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def income_table(self):
        scrollbarx = Scrollbar(self.history_table_frame, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.history_table_frame, orient=VERTICAL)
        self.tree = ttk.Treeview(self.history_table_frame,
                                 columns=("merchant_name", "receipt_date", "entered_date", "receipt_id",
                                          'supervisor', 'receipt_total_price', 'payed', 'remaining',
                                          'product_name',
                                          'quantity', 'storeroom', 'piece_price', 'unit_price', 'total_price'),
                                 selectmode="browse", height=16,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=10)
        self.tree.column('#1', stretch=NO, minwidth=0, width=65)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=80)
        self.tree.column('#5', stretch=NO, minwidth=0, width=50)
        self.tree.column('#6', stretch=NO, minwidth=0, width=80)
        self.tree.column('#7', stretch=NO, minwidth=0, width=50)
        self.tree.column('#8', stretch=NO, minwidth=0, width=50)
        self.tree.column('#9', stretch=NO, minwidth=0, width=100)
        self.tree.column('#10', stretch=NO, minwidth=0, width=100)
        self.tree.column('#11', stretch=NO, minwidth=0, width=50)
        self.tree.column('#12', stretch=NO, minwidth=0, width=80)
        self.tree.column('#13', stretch=NO, minwidth=0, width=80)

        self.tree.heading("merchant_name", text="اسم التاجر", anchor=W)
        self.tree.heading("receipt_date", text="تاريخ الفاتورة", anchor=W)
        self.tree.heading('entered_date', text="تاريخ الادخال", anchor=W)
        self.tree.heading('receipt_id', text="رقم الفاتورة", anchor=W)
        self.tree.heading('supervisor', text="المستلم", anchor=W)
        self.tree.heading('receipt_total_price', text="اجمالي الفاتورة", anchor=W)
        self.tree.heading('payed', text="المدفوع", anchor=W)
        self.tree.heading('remaining', text="الباقي", anchor=W)

        self.tree.heading('product_name', text="اسم الصنف", anchor=W)
        self.tree.heading('quantity', text="الكمية", anchor=W)
        self.tree.heading('storeroom', text="رقم المخزن", anchor=W)
        self.tree.heading('piece_price', text="سعر القطعة", anchor=W)
        self.tree.heading('unit_price', text="سعر الوحدة", anchor=W)
        self.tree.heading('total_price', text="سعر الكمية", anchor=W)

        self.tree.grid(row=2, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=2, column=1, sticky="ns", pady=30)

    def income_history(self):
        self.historyincomew = Tk()
        width = 1400
        height = 600
        screen_width = self.historyincomew.winfo_screenwidth()
        screen_height = self.historyincomew.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.historyincomew.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.history_table_frame = Frame(self.historyincomew, width=1400, height=450, bg="#FFFFFF")
        self.history_table_frame.place(x=0, y=80)
        self.history_table_frame_info = self.searchframe.place_info()
        self.searchbut = Button(self.historyincomew, text="بحث بالتاريخ", font="roboto 14", bg="#FFFFFF", bd=5,
                                command=self.search_history)
        self.searchbut.place(x=400, y=10)

        self.searchbut2 = Button(self.historyincomew, text="بحث بالصنف", font="roboto 14", bg="#FFFFFF", bd=5,
                                 command=self.search_product)
        self.searchbut2.place(x=270, y=10)

        self.searchvar = StringVar()
        self.searchentry = Entry(self.historyincomew, textvariable=self.searchvar, font="roboto 14", width=25,
                                 bg="#FFFFFF")
        self.searchentry.place(x=520, y=20)

        self.delete_item = Button(self.historyincomew, text="حذف صنف من فاتورة", font="robot 16 bold", fg="black",
                                  bg="#4267b2",
                                  command=self.delete_recipt)
        self.delete_item.place(x=820, y=10)
        self.income_table()

        self.Get_history_income()

        self.historyincomew.mainloop()

    def search_history(self):
        # cur.execute("SELECT %s FROM Data where %s=?" % (column, goal), (constrain,))
        ans = ''
        try:
            self.get_date = str(self.searchentry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل التاريخ بشكل صحيح")
            return
        if self.get_date == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة التاريخ")
            return
        self.cur.execute('select * from today_income where datetime_entered=?', (self.get_date,))
        result = self.cur.fetchall()
        self.income_table()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def search_product(self):
        # cur.execute("SELECT %s FROM Data where %s=?" % (column, goal), (constrain,))
        ans = ''
        try:
            self.get_product = str(self.searchentry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل اسم الصنف بشكل صحيح")
            return
        if self.get_product == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم الصنف")
            return
        self.cur.execute('select * from today_income where product_name = ?', (self.get_product,))
        result = self.cur.fetchall()
        self.income_table()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def delete_item(self):
        self.delete_item_w = Tk()
        width = 380
        height = 250
        screen_width = self.delete_item_w.winfo_screenwidth()
        screen_height = self.delete_item_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.delete_item_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.delete_entry = Entry(self.delete_item_w, bg="light grey", font="robot 14")
        self.delete_entry.grid(row=2, column=1)
        self.delete_label = Label(self.delete_item_w, text="ادخل اسم الصنف", font="roboto 14 bold", bg="#FFFFFF")
        self.delete_label.grid(row=2, column=2)

        self.delete_entry11 = Entry(self.delete_item_w, bg="light grey", font="robot 14")
        self.delete_entry11.grid(row=3, column=1)
        self.delete_label11 = Label(self.delete_item_w, text="ادخل رقم المخزن", font="roboto 14 bold", bg="#FFFFFF")
        self.delete_label11.grid(row=3, column=2)

        self.delete_entry22 = Entry(self.delete_item_w, bg="light grey", font="robot 14")
        self.delete_entry22.grid(row=4, column=1)
        self.delete_label22 = Label(self.delete_item_w, text="ادخل الكمية", font="roboto 14 bold", bg="#FFFFFF")
        self.delete_label22.grid(row=4, column=2)

        self.delete_entry33 = Entry(self.delete_item_w, bg="light grey", font="robot 14")
        self.delete_entry33.grid(row=5, column=1)
        self.delete_label33 = Label(self.delete_item_w, text="ادخل سعر الوحدة", font="roboto 14 bold", bg="#FFFFFF")
        self.delete_label33.grid(row=5, column=2)

        self.delete_button = Button(self.delete_item_w, text="حذف", font="robot 16 bold", fg="black", bg="yellow",
                                    command=self.final_delete_item)

        self.delete_button.grid(row=6, column=1)
        self.delete_item_w.mainloop()

    def final_delete_item(self):
        self.get_delete_entry = str(self.delete_entry.get())
        self.get_delete_entry11 = int(self.delete_entry11.get())
        self.get_delete_entry22 = int(self.delete_entry22.get())
        self.get_delete_entry33 = float(self.delete_entry33.get())

        li = [self.get_delete_entry11, self.get_delete_entry, self.get_delete_entry33]

        # self.cur.execute("delete from stores;")

        self.cur.execute("select product_name from stores;")
        ex_product = self.cur.fetchall()
        self.ex_product1 = ([tup[0] for tup in ex_product])

        if self.get_delete_entry not in self.ex_product1:
            messagebox.showerror("خطأ", "هذا غير موجود")
            return

        if self.get_delete_entry in self.ex_product1:
            self.cur.execute("select product_quantity from stores where product_name = ? "
                             "and product_Storeroom=? "
                             "and product_unit_price=?", (str(self.get_delete_entry),
                                                          int(self.get_delete_entry11),
                                                          float(self.get_delete_entry33)))
            old_quantity = self.cur.fetchall()
            self.old_quantity10 = ([tup[0] for tup in old_quantity])
            self.old_quantity10 = self.old_quantity10[0]

            self.new_quantity10 = int(abs(self.get_delete_entry22 - self.old_quantity10))

        self.cur.execute("delete from new_income where product_name = ?;", (self.get_delete_entry,))

        self.cur.execute("update stores set product_quantity = ? where product_Storeroom=? and product_name=?"
                         "and product_unit_price=?",
                         (int(self.new_quantity10),
                          int(self.get_delete_entry11),
                          str(self.get_delete_entry),
                          float(self.get_delete_entry33)))
        self.base.commit()
        self.delete_item_w.destroy()
        self.Get()

    def delete_recipt(self):
        self.delete_recipt_w = Tk()
        width = 345
        height = 200
        screen_width = self.delete_recipt_w.winfo_screenwidth()
        screen_height = self.delete_recipt_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.delete_recipt_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.merchant_entry = Entry(self.delete_recipt_w, bg="light grey", font="robot 14")
        self.merchant_entry.grid(row=2, column=1)
        self.merchant_label = Label(self.delete_recipt_w, text="ادخل اسم التاجر", font="roboto 14 bold", bg="#FFFFFF")
        self.merchant_label.grid(row=2, column=2)

        self.recite_entry = Entry(self.delete_recipt_w, bg="light grey", font="robot 14")
        self.recite_entry.grid(row=3, column=1)
        self.recite_label = Label(self.delete_recipt_w, text="ادخل رقم الفاتورة", font="roboto 14 bold", bg="#FFFFFF")
        self.recite_label.grid(row=3, column=2)

        self.name_entry = Entry(self.delete_recipt_w, bg="light grey", font="robot 14")
        self.name_entry.grid(row=4, column=1)
        self.name_label = Label(self.delete_recipt_w, text="ادخل اسم الصنف", font="roboto 14 bold", bg="#FFFFFF")
        self.name_label.grid(row=4, column=2)

        self.storeroom_entry = Entry(self.delete_recipt_w, bg="light grey", font="robot 14")
        self.storeroom_entry.grid(row=5, column=1)
        self.storerroom_label = Label(self.delete_recipt_w, text="ادخل رقم المخزن", font="roboto 14 bold", bg="#FFFFFF")
        self.storerroom_label.grid(row=5, column=2)

        self.unit_entry = Entry(self.delete_recipt_w, bg="light grey", font="robot 14")
        self.unit_entry.grid(row=6, column=1)
        self.unit_label = Label(self.delete_recipt_w, text="ادخل سعر الوحدة", font="roboto 14 bold", bg="#FFFFFF")
        self.unit_label.grid(row=6, column=2)



        self.delete_button = Button(self.delete_recipt_w, text="حذف", font="robot 16 bold", fg="black", bg="yellow",
                                    command=self.final_delete_recipt)
        self.delete_button.grid(row=7, column=1)
        self.delete_recipt_w.mainloop()

    def update_debt(self):
        self.cur.execute('select debt from merchants where merchant_name=?', (self.get_merchant_entry,))
        old_debt = self.cur.fetchall()
        self.old_debt = ([tup[0] for tup in old_debt])
        self.old_debt = float(self.old_debt[0])
        self.new_debt = float(self.old_debt - self.total_quantity_price)
        self.cur.execute('update merchants set debt=? where merchant_name=?', (self.new_debt, self.get_merchant_entry,))
        self.base.commit()

    def final_delete_recipt(self):
        try:
            self.get_merchant_entry = str(self.merchant_entry.get())
            self.get_recite_entry = int(self.recite_entry.get())
            self.get_name_entry = str(self.name_entry.get())
            self.get_storeroom_entry = int(self.storeroom_entry.get())
            self.get_unit_entry = float(self.unit_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة")
            return

        if self.get_merchant_entry == "" or self.get_recite_entry == "" or self.get_name_entry == "":
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة")
        elif self.get_storeroom_entry == "" or self.get_unit_entry == "":
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة")
        try:
            self.cur.execute("select recite_total_price from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?",
                             (int(self.get_recite_entry),
                              str(self.get_name_entry),
                              int(self.get_storeroom_entry),
                              float(self.get_unit_entry),
                              str(self.get_merchant_entry)))
            total_recite_price = self.cur.fetchall()
            self.total_recite_price = ([tup[0] for tup in total_recite_price])
            self.total_recite_price = self.total_recite_price[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return



        try:
            self.cur.execute("select product_total_price from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=? ",
                             (int(self.get_recite_entry),
                              str(self.get_name_entry),
                              int(self.get_storeroom_entry),
                              float(self.get_unit_entry),
                              str(self.get_merchant_entry)))
            total_quantity_price = self.cur.fetchall()
            self.total_quantity_price = ([tup[0] for tup in total_quantity_price])
            self.total_quantity_price = self.total_quantity_price[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return




        try:
            self.cur.execute("select payed from today_income where recite_id = ? and name_of_merchant=?",
                             (self.get_recite_entry,
                              str(self.get_merchant_entry)))
            payed = self.cur.fetchall()
            self.old_payed = ([tup[0] for tup in payed])
            self.old_payed = float(self.old_payed[0])
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return




        self.new_total_recite_price = float(self.total_recite_price - self.total_quantity_price)
        self.new_remaining = float(self.new_total_recite_price - self.old_payed)

        self.cur.execute("update today_income set recite_total_price = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.new_total_recite_price),
                          int(self.get_recite_entry),
                          str(self.get_merchant_entry)))

        self.cur.execute("update today_income set remaining = ? where recite_id=? and name_of_merchant=?;",
                         (float(self.new_remaining),
                          int(self.get_recite_entry),
                          str(self.get_merchant_entry)))

        try:
            self.cur.execute("select product_quantity from stores where product_name=? "
                             "and product_Storeroom=? and product_unit_price=?;",
                             (str(self.get_name_entry),
                              int(self.get_storeroom_entry),
                              float(self.get_unit_entry)))
            product_quantity_S = self.cur.fetchall()
            self.product_quantity_S = ([tup[0] for tup in product_quantity_S])
            self.product_quantity_S = self.product_quantity_S[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return




        try:
            self.cur.execute("select product_quantity from today_income where recite_id = ? and product_name=? "
                             "and product_Storeroom=? and product_unit_price=? and name_of_merchant=?;",
                             (int(self.get_recite_entry),
                              str(self.get_name_entry),
                              int(self.get_storeroom_entry),
                              float(self.get_unit_entry),
                              str(self.get_merchant_entry)))
            product_quantity = self.cur.fetchall()
            self.product_quantity = ([tup[0] for tup in product_quantity])
            self.product_quantity = self.product_quantity[0]
        except:
            messagebox.showerror("خطأ", "من فضلك قم بإدخال المعلومات اللازمة بشكل صحيح")
            return




        self.new_product_quantity = int(abs(self.product_quantity - self.product_quantity_S))

        self.cur.execute("update stores set product_quantity = ? where product_name=? "
                         "and product_Storeroom=? and product_unit_price=?;",
                         (int(self.new_product_quantity),
                          str(self.get_name_entry),
                          int(self.get_storeroom_entry),
                          float(self.get_unit_entry)))


        self.cur.execute("delete from today_income where recite_id = ? and product_name=? and product_Storeroom=? and "
                         "product_unit_price=? and name_of_merchant=?;",
                         (int(self.get_recite_entry),
                          str(self.get_name_entry),
                          int(self.get_storeroom_entry),
                         float(self.get_unit_entry),
                          str(self.get_merchant_entry)))


        self.base.commit()
        self.delete_recipt_w.destroy()
        self.income_table()
        self.Get_history_income()
        self.update_debt()

    # PERFOMS CHECK AND ADD'S ITEMS

    # BUILD USER TABLE
    def buildusertable(self):
        self.tableframe8.place_forget()
        self.salesframe2.place_forget()
        self.returnframe.place_forget()
        self.tableframe3.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe.place_forget()
        self.itemframe.place_forget()
        self.salesframe.place_forget()
        self.marketfrme.place_forget()
        self.storesframe.place_forget()
        self.tableframe4.place_forget()
        self.tableframe5.place_forget()
        self.tableframe6.place_forget()
        self.tableframe7.place_forget()
        self.customers.place_forget()
        self.tableframe10.place_forget()

        self.formframe1.place(self.formframe1info)
        self.tableframe1.place(self.tableframe1info)
        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("اسم المستخدم", "كلمة المرور", "نوع الحساب"),
                                 selectmode="browse", height=17, yscrollcommand=scrollbary.set,
                                 xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=170)
        self.tree.column('#2', stretch=NO, minwidth=0, width=170)

        self.tree.heading('اسم المستخدم', text="اسم المستخدم", anchor=W)
        self.tree.heading('كلمة المرور', text="كلمة المرور", anchor=W)
        self.tree.heading('نوع الحساب', text="نوع الحساب", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.getusers()
        self.tree.bind("<<TreeviewSelect>>", self.clickusertable)
        self.formframe1.focus_set()
        self.usernamedit = StringVar()
        self.passwordedit = StringVar()
        self.accedit = StringVar()
        va = 110
        l1 = ['اسم المستخدم', 'كلمة المرور', 'نوع الحساب']
        for i in range(0, 3):
            Label(self.formframe1, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=va)
            va += 70
        Entry(self.formframe1, textvariable=self.usernamedit, font="roboto 14", bg="#FFFFFF", width=25,
              state='readonly').place(x=162, y=105, height=40)
        Entry(self.formframe1, textvariable=self.passwordedit, font="roboto 14", bg="#FFFFFF", width=25).place(x=162,
                                                                                                               y=175,
                                                                                                               height=40)
        profiles = mycombobox(self.formframe1, font="robot 14", width=23, textvariable=self.accedit)
        profiles.place(x=162, y=245, height=40)
        profiles.set_completion_list(['ADMIN', 'USER'])
        Button(self.formframe1, text="انشاء حساب", font="robot 12 bold", bg="#FFFFFF", bd=5, width=12, height=2,
               command=self.adduser).place(x=0, y=10)
        Button(self.formframe1, text="تعديل", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.changeusertable).place(x=145, y=381)
        Button(self.formframe1, text="ازالة", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
               command=self.deluser).place(x=345, y=381)

        self.mainsearch(0)

    # FETCH USERS FROM USERS TABLE
    def getusers(self, x=0):
        ans = ''
        self.cur.execute("select * from users")
        userslist = self.cur.fetchall()
        for i in userslist:
            self.tree.insert('', 'end', values=i)
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def changeusertable(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.usernamedit.set((self.usernamedit.get()).upper())
        self.passwordedit.set((self.passwordedit.get()).upper())
        self.accedit.set((self.accedit.get()).upper())
        if (len(li) == 3):
            if self.usernamedit.get() == '' or self.accedit.get() == '':
                messagebox.showerror("خطأ", "من فضلك ادخل المعلومات كاملة")
                return
            if (self.accedit.get() != 'ADMIN' and self.accedit.get() != 'USER'):
                messagebox.showerror("خطأ", "نوع الحساب غير موجود")
                return
            self.cur.execute(
                "update users set password = ?,account_type = ? where username = ?;", (
                    self.passwordedit.get(), self.accedit.get(), self.usernamedit.get()))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            cur = self.getusers(li[0])
            self.tree.selection_set(cur)

    def deluser(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        fa = 0
        if (self.username.get() == li[0]):
            if messagebox.askyesno("تنبيه", "هل تريد مسح هذا الحساب؟"):
                fa = 1
            else:
                return
        if messagebox.askyesno("تنبيه", "هل تريد مسح هذا الحساب؟") == True and len(li) == 3:
            self.cur.execute("delete from users where username = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getusers()
            self.usernamedit.set('')
            self.passwordedit.set('')
            self.accedit.set('')
        if (fa == 1):
            self.change_user()

    def adduser(self):
        self.reguser()
        self.loginw.state('normal')  # LOGIN WINDOW ENTERS

    def searchuser(self):
        if self.searchvar.get() == '':
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from users")
        li = self.cur.fetchall()
        for i in li:
            if (i[0] == self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def resetusertable(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getusers()

    def clickusertable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 3):
            self.usernamedit.set((li[0]))
            self.passwordedit.set((li[1]))
            self.accedit.set((li[2]))




    def table8(self):
        scrollbarx = Scrollbar(self.tableframe8, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe8, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe8,
                                 columns=("Transaction ID", "Invoice No.", "Product ID", "Description"),
                                 selectmode="browse", height=16,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=140)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)

        self.tree.heading('Transaction ID', text="تاريخ البيع", anchor=W)
        self.tree.heading('Invoice No.', text="اسم الصنف", anchor=W)
        self.tree.heading('Product ID', text="الكمية", anchor=W)
        self.tree.heading('Description', text="سعر بيع الكمية", anchor=W)

        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)

    def insert_sales_history(self):
        ans = ''
        self.cur.execute("select * from sales_history;")
        productlist = self.cur.fetchall()
        self.table8()
        x = 0
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans



    def search_sold_table1(self):
        ans = ''
        try:
            self.get_searchEntry_ = str(self.searchEntry_.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل اسم الصنف بشكل صحيح")
            return
        if self.get_searchEntry_ == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم الصنف")
            return
        self.cur.execute(
            'select * from sales_history'
            ' where product_name=?', (self.get_searchEntry_,))
        result = self.cur.fetchall()
        self.table8()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans



    def search_sold_table2(self):
        ans = ''
        try:
            self.get_searchEntry_ = str(self.searchEntry_.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل تاريخ البيع بشكل صحيح")
            return
        if self.get_searchEntry_ == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة تاريخ البيع")
            return
        self.cur.execute(
            'select * from sales_history'
            ' where sales_date=?', (self.get_searchEntry_,))
        result = self.cur.fetchall()
        self.table8()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans



    # BUILD SALES TABLE
    def buildsalestable(self):
        self.returnframe.place_forget()
        self.tableframe3.place_forget()
        self.searchframe.place_forget()
        self.formframe.place_forget()
        self.tableframe6.place_forget()
        self.tableframe7.place_forget()
        self.tableframe.place_forget()
        self.itemframe.place_forget()
        self.formframe1.place_forget()
        self.salesframe.place_forget()
        self.marketfrme.place_forget()
        self.storesframe.place_forget()
        self.tableframe4.place_forget()
        self.tableframe5.place_forget()
        self.tableframe1.place_forget()
        self.customers.place_forget()
        self.tableframe10.place_forget()
        self.tableframe8.place(self.tableframe8info)
        self.salesframe2.place(self.salesframeinfo2)
        self.insert_sales_history()
        #self.cur.execute("drop table total_income;")
        self.history_search_but = Button(self.salesframe2, text="بحث بالتاريخ", font="roboto 14", bg="#4267b2", bd=5,
                                         command=self.search_sold_table2)
        self.history_search_but.place(x=720, y=10, width=120)

        self.product_search_but = Button(self.salesframe2, text="بحث بالصنف", font="roboto 14", bg="#4267b2", bd=5,
                                    command=self.search_sold_table1)
        self.product_search_but.place(x=590, y=10, width=120)

        self.searchvar2 = StringVar()
        self.searchEntry_ = Entry(self.salesframe2, textvariable=self.searchvar2, font="roboto 14", width=25,
                                  bg="#FFFFFF")
        self.searchEntry_.place(x=860, y=20)
        self.money = Button(self.salesframe2, text="حسابات", font="roboto 14", bg="#4267b2", bd=5,
                                    command=self.calculations)
        self.money.place(x=390, y=8, width=120)

        self.money = Button(self.salesframe2, text="مرتجع للماركت", font="roboto 14", bg="#4267b2", bd=5,
                            command=self.Return_To_Market)
        self.money.place(x=260, y=8, width=120)

        self.money = Button(self.salesframe2, text="مرتجع للمخزن", font="roboto 14", bg="#4267b2", bd=5,
                            command=self.Return_To_Store)
        self.money.place(x=130, y=8, width=120)

        today = datetime.date(datetime.now())
        format_date = str(today.strftime("%d/%m/%Y"))
        salling_date = format_date

        self.cur.execute("select quantity_price from sales_history where sales_date=?", (salling_date,))
        today_total = self.cur.fetchall()
        self.today_total = ([tup[0] for tup in today_total])

        self.counter = 0
        for i in range(0, len(self.today_total)):
            num = float(self.today_total[i])
            self.counter = float(self.counter + num)


        Label(self.salesframe2, text=":اجمالي المبيعات ", font="robot 18 bold", bg="#4267b2").place(x=200, y=100)
        Label(self.salesframe2, text=self.counter, font="robot 20 bold", bg="#4267b2").place(x=210, y=140)
        Button(self.salesframe2, text="اجمالي الفلوس في الدرج", font="robot 16 bold",bg="#4267b2", command=self.confirmation).place(x=210, y=210)

    def Return_To_Market(self):
        self.return_to_market_w = Tk()
        width = 380
        height = 250
        screen_width = self.return_to_market_w.winfo_screenwidth()
        screen_height = self.return_to_market_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.return_to_market_w.geometry("%dx%d+%d+%d" % (width, height, x, y))


        self.returns_to_market_product_label = Label(self.return_to_market_w, text="اسم الصنف", font="robot 12 bold",
                                                   bg="light gray",
                                                   width=15).place(x=205, y=20)
        self.returns_to_market_product = Entry(self.return_to_market_w, bg="light gray", width=30)
        self.returns_to_market_product.place(x=5, y=20)

        self.returns_to_market_quantity_label = Label(self.return_to_market_w, text="الكمية", font="robot 12 bold",
                                                    bg="light gray", width=15).place(x=205, y=50)
        self.returns_to_market_quantity = Entry(self.return_to_market_w, bg="light gray", width=30)
        self.returns_to_market_quantity.place(x=5, y=50)

        self.returns_to_market_unitprice_label = Label(self.return_to_market_w, text="سعر الوحدة", font="robot 12 bold",
                                                     bg="light gray", width=15).place(x=205, y=80)
        self.returns_to_market_unitprice = Entry(self.return_to_market_w, bg="light gray", width=30)
        self.returns_to_market_unitprice.place(x=5, y=80)

        self.returns_to_market_date_label = Label(self.return_to_market_w, text="تاريخ البيع", font="robot 12 bold",
                                                       bg="light gray", width=15).place(x=205, y=110)
        self.returns_to_market_date = Entry(self.return_to_market_w, bg="light gray", width=30)
        self.returns_to_market_date.place(x=5, y=110)
        self.returns_to_market_button = Button(self.return_to_market_w, text="ارجاع الصنف للماركت", font="roboto 16 bold",
                                             bg="#4267b2", width=20, command=self.back_product_to_market)
        self.returns_to_market_button.place(x=13, y=140)

        self.return_to_market_w.mainloop()


    def back_product_to_market(self):
        try:
            self.get_returns_to_market_product = str(self.returns_to_market_product.get())
            self.get_returns_to_market_quantity = int(self.returns_to_market_quantity.get())
            self.get_returns_to_market_unitprice = float(self.returns_to_market_unitprice.get())
            self.get_returns_to_market_date = str(self.returns_to_market_date.get())

        except:
            messagebox.showerror("خطأ", "من فضلك ادخل معلومات صحيحة")
        try:
            self.cur.execute("select product_name from sales_history where  "
                             "product_name =? and product_quantity=? and sales_date=?;",
                             (str(self.get_returns_to_market_product),
                              int(self.get_returns_to_market_quantity),
                              str(self.get_returns_to_market_date)))
            ex_product_in_sales = self.cur.fetchall()
            self.ex_product_in_sales_to_market = ([tup[0] for tup in ex_product_in_sales])
            self.ex_product_in_sales_to_market = self.ex_product_in_sales_to_market[0]
        except:
            messagebox.showerror("خطأ", "هذا الصنف غير موجود بالمبيعات")
            return
        if self.get_returns_to_market_product not in self.ex_product_in_sales_to_market:
            messagebox.showerror("خطأ", "هذا الصنف لم يتم بيعه ")

        if self.get_returns_to_market_product in self.ex_product_in_sales_to_market:
            li = [self.get_returns_to_market_product, self.get_returns_to_market_unitprice]

            #self.cur.execute("drop table check_return_from_sales_to_market;")
            self.cur.execute("create table if not exists check_return_from_sales_to_market"     
                             "(product_name varchar(30) not null,"
                             "product_quantity integer not null,"
                             "product_unit_price float not null);")

            self.cur.execute("insert into check_return_from_sales_to_market values(?,?,?);",
                             (str(self.get_returns_to_market_product),
                              int(self.get_returns_to_market_quantity),
                              float(self.get_returns_to_market_unitprice)))

            self.cur.execute("select product_name from market_items;")
            ex_product = self.cur.fetchall()
            self.check_products_in_market = ([tup[0] for tup in ex_product])

            if self.get_returns_to_market_product not in self.check_products_in_market:
                self.cur.execute("insert into market_items select * from check_return_from_sales_to_market;")

                '''
                self.cur.execute("select product_quantity from sales_history  where  "
                                 "product_name =? and quantity_price=?;",
                                 (str(self.get_returns_to_market_product),
                                  float(self.get_returns_to_market_unitprice)))
                old_quantity = self.cur.fetchall()
                self.check_old_quantity_before_market = ([tup[0] for tup in old_quantity])
                self.check_old_quantity_before_market = self.check_old_quantity_before_market[0]
                
                self.check_new_quantity_in_market = int(abs(self.get_back_to_store_quantity - self.check_old_quantity_before))
                self.cur.execute("update market_items set product_quantity=? where  "
                                 "product_name =? and quantity_price=?;",
                                 (int(self.new_quantity_in_market),
                                  str(self.get_return_to_store_product),
                                  float(self.get_return_to_store_unitprice)))
                '''

            if self.get_returns_to_market_product in self.check_products_in_market:

                counter = 0

                self.cur.execute("select product_name from market_items where  "
                                 "product_name =? and quantity_price=?;",
                                 (str(self.get_returns_to_market_product),
                                  float(self.get_returns_to_market_unitprice)))

                match = self.cur.fetchall()
                self.check_in_market = ([tup[0] for tup in match])
                self.check_in_market = self.check_in_market[0]
                print(self.check_in_market)

                self.cur.execute("select quantity_price from market_items where  "
                                 "product_name =? and quantity_price=?;",
                                 (str(self.get_returns_to_market_product),
                                  float(self.get_returns_to_market_unitprice)))

                match2 = self.cur.fetchall()
                self.check_in_market2 = ([tup[0] for tup in match2])
                self.check_in_market2 = self.check_in_market2[0]
                self.check_if_all_in_market = [self.check_in_market, self.check_in_market2]

                if self.check_if_all_in_market != "":
                    for i in li:
                        if i in self.check_if_all_in_market:
                            counter += 1

                if counter == 2:
                    self.cur.execute("select product_quantity from market_items where  "
                                     "product_name =? and quantity_price=?;",
                                     (str(self.get_returns_to_market_product),
                                      float(self.get_returns_to_market_unitprice)))

                    old_quantity = self.cur.fetchall()
                    self.check_old_quantity_before_market1 = ([tup[0] for tup in old_quantity])
                    self.check_old_quantity_before_market1 = self.check_old_quantity_before_market1[0]

                    self.check_new_quantity_in_market = int(self.get_returns_to_market_quantity + self.check_old_quantity_before_market1)

                    self.cur.execute("update market_items set product_quantity=? where  "
                                     "product_name =? and quantity_price=?;",
                                     (int(self.check_new_quantity_in_market),
                                      str(self.get_returns_to_market_product),
                                      float(self.get_returns_to_market_unitprice)))


                    today = datetime.date(datetime.now())
                    self.format_date1 = str(today.strftime("%d/%m/%Y"))
                    self.today_date1 = self.format_date1
                    if self.get_returns_to_market_date != self.today_date1:

                        self.cur.execute("select actual_income from total_income where date=?;",
                                         (str(self.get_returns_to_market_date),))
                        old_actual_income = self.cur.fetchall()
                        self.old_actual_income1 = ([tup[0] for tup in old_actual_income])
                        self.old_actual_income1 = self.old_actual_income1[0]


                        self.cur.execute("select system_count from total_income where date=?",
                                         (str(self.get_returns_to_market_date),))
                        old_system_count = self.cur.fetchall()
                        self.old_system_count1 = ([tup[0] for tup in old_actual_income])
                        self.old_system_count1 = self.old_system_count1[0]


                        self.cur.execute("select quantity_price from sales_history where sales_date=? and product_name =? "
                                         "and product_quantity=?;",
                                         (str(self.get_returns_to_market_date),
                                         str(self.get_returns_to_market_product),
                                         int(self.get_returns_to_market_quantity),))
                        returned_quantity_price = self.cur.fetchall()
                        self.returned_quantity_price1 = ([tup[0] for tup in returned_quantity_price])
                        self.returned_quantity_price1 = self.returned_quantity_price1[0]

                        self.new_system_count1 = float(self.old_system_count1 - self.returned_quantity_price1)
                        self.new_defference1 = float(abs(self.new_system_count1 - self.old_actual_income1))

                        self.cur.execute("update total_income set system_count=? where date=?;",
                                         (float(self.new_system_count1),
                                         str(self.get_returns_to_market_date)))
                        self.cur.execute("update total_income set difference=? where date=?;",
                                         (float(self.new_defference1),
                                         str(self.get_returns_to_market_date)))
                        self.buildsalestable()

                    if self.get_returns_to_market_date == self.today_date1:
                        self.cur.execute(
                            "select quantity_price from sales_history where sales_date=? and product_name =? "
                            "and product_quantity=?;",
                            (str(self.get_returns_to_market_date),
                             str(self.get_returns_to_market_product),
                             int(self.get_returns_to_market_quantity),))
                        returned_quantity_price = self.cur.fetchall()
                        self.returned_quantity_price1 = ([tup[0] for tup in returned_quantity_price])
                        self.returned_quantity_price1 = self.returned_quantity_price1[0]

                        self.new_counter1 = float(self.counter - self.returned_quantity_price1)
                        Label(self.salesframe2, text=self.new_counter1, font="robot 20 bold", bg="#4267b2").place(x=210,
                                                                                                             y=140)
                        self.buildsalestable()



            #self.cur.execute("delete from sales_history where product_quantity = 0")
            self.cur.execute("delete from sales_history where  "
                                    "sales_date=? and product_name =? and product_quantity=?;",
                                     (str(self.get_returns_to_market_date),
                                      str(self.get_returns_to_market_product),
                                      int(self.get_returns_to_market_quantity)))
            self.cur.execute("delete from check_return_from_sales_to_market;")
            self.insert_sales_history()
            self.new_text = ""
            self.returns_to_market_product.delete(0, END)
            self.returns_to_market_product.insert(0, self.new_text)

            self.returns_to_market_quantity.delete(0, END)
            self.returns_to_market_quantity.insert(0, self.new_text)

            self.returns_to_market_unitprice.delete(0, END)
            self.returns_to_market_unitprice.insert(0, self.new_text)

            self.returns_to_market_date.delete(0, END)
            self.returns_to_market_date.insert(0, self.new_text)


            self.base.commit()

    def Return_To_Store(self):
        self.return_to_stores_w = Tk()
        width = 380
        height = 250
        screen_width = self.return_to_stores_w.winfo_screenwidth()
        screen_height = self.return_to_stores_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.return_to_stores_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.back_storeroom_num_label = Label(self.return_to_stores_w, text="رقم المخزن", font="robot 12 bold",
                                                bg="light gray",
                                                width=15).place(x=205, y=20)
        self.back_storeroom_num = Entry(self.return_to_stores_w, bg="light gray", width=30)
        self.back_storeroom_num.place(x=5, y=20)

        self.back_to_store_product_label = Label(self.return_to_stores_w, text="اسم الصنف", font="robot 12 bold",
                                                   bg="light gray",
                                                   width=15).place(x=205, y=50)
        self.back_to_store_product = Entry(self.return_to_stores_w, bg="light gray", width=30)
        self.back_to_store_product.place(x=5, y=50)

        self.back_to_store_quantity_label = Label(self.return_to_stores_w, text="الكمية", font="robot 12 bold",
                                                    bg="light gray", width=15).place(x=205, y=80)
        self.back_to_store_quantity = Entry(self.return_to_stores_w, bg="light gray", width=30)
        self.back_to_store_quantity.place(x=5, y=80)

        self.back_to_store_unitprice_label = Label(self.return_to_stores_w, text="سعر الوحدة", font="robot 12 bold",
                                                     bg="light gray", width=15).place(x=205, y=110)
        self.back_to_store_unitprice = Entry(self.return_to_stores_w, bg="light gray", width=30)
        self.back_to_store_unitprice.place(x=5, y=110)

        self.back_sell_date_label = Label(self.return_to_stores_w, text="تاريخ البيع", font="robot 12 bold",
                                              bg="light gray",
                                              width=15).place(x=205, y=140)
        self.back_sell_date = Entry(self.return_to_stores_w, bg="light gray", width=30)
        self.back_sell_date.place(x=5, y=140)
        self.back_to_store_button = Button(self.return_to_stores_w, text="ارجاع الصنف للمخزن", font="roboto 16 bold",
                                             bg="#4267b2", width=20, command=self.back_product_to_store)
        self.back_to_store_button.place(x=13, y=180)


        self.return_to_stores_w.mainloop()


    def back_product_to_store(self):
        try:
            self.get_back_storeroom_num = int(self.back_storeroom_num.get())
            self.get_back_to_store_product = str(self.back_to_store_product.get())
            self.get_back_to_store_quantity = int(self.back_to_store_quantity.get())
            self.get_back_to_store_unitprice = float(self.back_to_store_unitprice.get())
            self.get_back_sell_date = str(self.back_sell_date.get())
        except:
            messagebox.showerror("خطأ", "من فضلك ادخل معلومات صحيحة")
        try:
            self.cur.execute("select product_name from sales_history where  "
                             "product_name =? and product_quantity=? and sales_date=?;",
                             (str(self.get_back_to_store_product),
                              int(self.get_back_to_store_quantity),
                              str(self.get_back_sell_date)))
            ex_product_in_sales = self.cur.fetchall()
            self.ex_product_in_sales = ([tup[0] for tup in ex_product_in_sales])
            self.ex_product_in_sales = self.ex_product_in_sales[0]
        except:
            messagebox.showerror("خطأ", "هذا الصنف غير موجود بالمبيعات")
            return
        if self.get_back_to_store_product not in self.ex_product_in_sales:
            messagebox.showerror("خطأ", "هذا الصنف لم يتم بيعه ")

        if self.get_back_to_store_product in self.ex_product_in_sales:
            li = [self.get_back_storeroom_num, self.get_back_to_store_product, self.get_back_to_store_unitprice]

            # self.cur.execute("delete from stores;")
            self.cur.execute("create table if not exists check_return_from_sales"
                             "(product_Storeroom integer not null,"
                             "product_name varchar(30) not null,"
                             "product_quantity integer not null,"
                             "product_unit_price float not null);")

            self.cur.execute("insert into check_return_from_sales values(?,?,?,?);",
                             (int(self.get_back_storeroom_num),
                              str(self.get_back_to_store_product),
                              int(self.get_back_to_store_quantity),
                              float(self.get_back_to_store_unitprice)))

            self.cur.execute("select product_name from stores;")
            ex_product = self.cur.fetchall()
            self.check_products_in_stores = ([tup[0] for tup in ex_product])

            if self.get_back_to_store_product not in self.check_products_in_stores:
                self.cur.execute("insert into stores select * from check_return_from_sales;")
                self.cur.execute("select product_quantity from sales_history  where  "
                                 "product_name =? and quantity_price=?;",
                                 (str(self.get_back_to_store_product),
                                  float(self.get_back_to_store_unitprice)))
                old_quantity = self.cur.fetchall()
                self.check_old_quantity_before = ([tup[0] for tup in old_quantity])
                self.check_old_quantity_before = self.check_old_quantity_before[0]
                '''
                self.check_new_quantity_in_market = int(abs(self.get_back_to_store_quantity - self.check_old_quantity_before))
                self.cur.execute("update market_items set product_quantity=? where  "
                                 "product_name =? and quantity_price=?;",
                                 (int(self.new_quantity_in_market),
                                  str(self.get_return_to_store_product),
                                  float(self.get_return_to_store_unitprice)))
                '''

            if self.get_back_to_store_product in self.check_products_in_stores:

                counter = 0
                self.cur.execute("select product_Storeroom from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_back_storeroom_num),
                                  str(self.get_back_to_store_product),
                                  float(self.get_back_to_store_unitprice)))
                match = self.cur.fetchall()
                self.check_in_store1 = ([tup[0] for tup in match])
                self.check_in_store1 = self.check_in_store1[0]

                self.cur.execute("select product_name from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_back_storeroom_num),
                                  str(self.get_back_to_store_product),
                                  float(self.get_back_to_store_unitprice)))

                match2 = self.cur.fetchall()
                self.check_in_store2 = ([tup[0] for tup in match2])
                self.check_in_store2 = self.check_in_store2[0]

                self.cur.execute("select product_unit_price from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_back_storeroom_num),
                                  str(self.get_back_to_store_product),
                                  float(self.get_back_to_store_unitprice)))

                match3 = self.cur.fetchall()
                self.check_in_store3 = ([tup[0] for tup in match3])
                self.check_in_store3 = self.check_in_store3[0]
                self.check_if_all_in_store = [self.check_in_store1, self.check_in_store2, self.check_in_store3]

                if self.check_if_all_in_store != "":
                    for i in li:
                        if i in self.check_if_all_in_store:
                            counter += 1

                if counter == 3:
                    self.cur.execute("select product_quantity from stores  where  "
                                    "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                     (int(self.get_back_storeroom_num),
                                      str(self.get_back_to_store_product),
                                      float(self.get_back_to_store_unitprice)))
                    old_quantity = self.cur.fetchall()
                    self.check_old_quantity_before1 = ([tup[0] for tup in old_quantity])
                    self.check_old_quantity_before1 = self.check_old_quantity_before1[0]

                    self.check_new_quantity_in_store1 = int(self.get_back_to_store_quantity + self.check_old_quantity_before1)


                    self.cur.execute("update stores set product_quantity=? where  "
                                    "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                     (int(self.check_new_quantity_in_store1),
                                      int(self.get_back_storeroom_num),
                                      str(self.get_back_to_store_product),
                                      float(self.get_back_to_store_unitprice)))

                    today = datetime.date(datetime.now())
                    self.format_date = str(today.strftime("%d/%m/%Y"))
                    self.today_date = self.format_date
                    if self.get_back_sell_date != self.today_date:

                        self.cur.execute("select actual_income from total_income where date=?;",
                                         (str(self.get_back_sell_date),))
                        old_actual_income = self.cur.fetchall()
                        self.old_actual_income = ([tup[0] for tup in old_actual_income])
                        self.old_actual_income = self.old_actual_income[0]


                        self.cur.execute("select system_count from total_income where date=?",
                                         (str(self.get_back_sell_date),))
                        old_system_count = self.cur.fetchall()
                        self.old_system_count = ([tup[0] for tup in old_actual_income])
                        self.old_system_count = self.old_system_count[0]


                        self.cur.execute("select quantity_price from sales_history where sales_date=? and product_name =? "
                                         "and product_quantity=?;",
                                         (str(self.get_back_sell_date),
                                         str(self.get_back_to_store_product),
                                         int(self.get_back_to_store_quantity),))
                        returned_quantity_price = self.cur.fetchall()
                        self.returned_quantity_price = ([tup[0] for tup in returned_quantity_price])
                        self.returned_quantity_price = self.returned_quantity_price[0]

                        self.new_system_count = float(self.old_system_count - self.returned_quantity_price)
                        self.new_defference = float(abs(self.new_system_count - self.old_actual_income))

                        self.cur.execute("update total_income set system_count=? where date=?;",
                                         (float(self.new_system_count),
                                         str(self.get_back_sell_date)))
                        self.cur.execute("update total_income set difference=? where date=?;",
                                         (float(self.new_defference),
                                         str(self.get_back_sell_date)))
                        self.buildsalestable()

                    if self.get_back_sell_date == self.today_date:
                        self.cur.execute(
                            "select quantity_price from sales_history where sales_date=? and product_name =? "
                            "and product_quantity=?;",
                            (str(self.get_back_sell_date),
                             str(self.get_back_to_store_product),
                             int(self.get_back_to_store_quantity),))
                        returned_quantity_price = self.cur.fetchall()
                        self.returned_quantity_price = ([tup[0] for tup in returned_quantity_price])
                        self.returned_quantity_price = self.returned_quantity_price[0]

                        self.new_counter = float(self.counter - self.returned_quantity_price)
                        print(self.new_counter)
                        Label(self.salesframe2, text=self.new_counter, font="robot 20 bold", bg="#4267b2").place(x=210,
                                                                                                             y=140)
                        self.buildsalestable()



            #self.cur.execute("delete from sales_history where product_quantity = 0")
            self.cur.execute("delete from sales_history where  "
                                    "sales_date=? and product_name =? and product_quantity=?;",
                                     (str(self.get_back_sell_date),
                                      str(self.get_back_to_store_product),
                                      int(self.get_back_to_store_quantity)))
            self.cur.execute("delete from check_return_from_sales;")
            self.insert_sales_history()
            self.new_text = ""
            self.back_storeroom_num.delete(0, END)
            self.back_storeroom_num.insert(0, self.new_text)

            self.back_to_store_product.delete(0, END)
            self.back_to_store_product.insert(0, self.new_text)

            self.back_to_store_quantity.delete(0, END)
            self.back_to_store_quantity.insert(0, self.new_text)

            self.back_to_store_unitprice.delete(0, END)
            self.back_to_store_unitprice.insert(0, self.new_text)

            self.back_sell_date.delete(0, END)
            self.back_sell_date.insert(0, self.new_text)

            self.base.commit()




    def confirmation(self):
        self.total_day_income = Entry(self.salesframe2, font="roboto 14", width=11,
                                  bg="#FFFFFF")
        self.total_day_income.place(x=210, y=265)
        self.confirm =  Button(self.salesframe2, text="تأكيد",bg="#4267b2",font="roboto 14", command=self.total_income)
        self.confirm.place(x=350, y=260)
    def total_income(self):
        if messagebox.askyesno("تنبيه",
                               "هل انت متأكد من ان هذا هو اجمالي اليوم. لن تتمكن من تعديل قيمة المبلغ في حالة التأكيد"):
            today = datetime.date(datetime.now())
            format_date = str(today.strftime("%d/%m/%Y"))
            income_date = format_date
            system_count = self.counter
            try:
                self.get_total_day_income = float(self.total_day_income.get())
            except:
                messagebox.showerror("خطأ", "من فضلك أدخل المعلومات بشكل صحيح")
                return
            difference = float(self.get_total_day_income - system_count)

            self.cur.execute("create table if not exists total_income"
                             "(num INTEGER PRIMARY KEY not null,"
                             "date varchar(15) not null,"
                             "system_count float not null,"
                             "actual_income float not null,"
                             "difference float not null);")

            self.cur.execute("select date from total_income;")
            ex_history = self.cur.fetchall()
            self.ex_history = ([tup[0] for tup in ex_history])
            if income_date in self.ex_history:
                messagebox.showerror("خطأ", "لقد قمت بالفعل بادخال الاجمالي لهذا اليوم")
                self.confirm.destroy()
                self.total_day_income.destroy()
                return

            self.cur.execute("select num from total_income;")
            ex_num = self.cur.fetchall()
            self.ex_num = ([tup[0] for tup in ex_num])

            if self.ex_num == []:
                self.ex_num = 0
                new_num = 0

            else:
                self.ex_num = int(self.ex_num[-1])
                new_num = self.ex_num + 1
            self.cur.execute("insert into total_income values(?,?,?,?,?)",
                             (int(new_num),
                              str(income_date),
                              float(system_count),
                              float(self.get_total_day_income),
                              float(difference)))
            self.base.commit()
            self.confirm.destroy()
            self.total_day_income.destroy()
    def table9(self):

        scrollbarx = Scrollbar(self.tableframe9, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe9, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe9,
                                 columns=("Merchant", "Date", "Id", "Product Name"),
                                 selectmode="extended", height=20,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=100)

        self.tree.heading('Merchant', text="التاريخ", anchor=W)
        self.tree.heading('Date', text="اجمالي المبيعات", anchor=W)
        self.tree.heading('Id', text="اجمالي الدرج", anchor=W)
        self.tree.heading('Product Name', text="الفرق", anchor=W)

        Label(self.tableframe4, ).grid(row=1, column=4)
        Label(self.tableframe4, ).grid(row=2, column=4)
        Label(self.tableframe4, ).grid(row=3, column=4)

        self.tree.grid(row=2, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=3, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=2, column=1, sticky="ns", pady=30)


    def insert_calc(self):
        ans = ''

        self.cur.execute(
            'select date, system_count, actual_income, difference from total_income;')
        result = self.cur.fetchall()
        self.table9()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans


    def search_calc2(self):
        ans = ''
        try:
            self.get_search_calc = str(self.search_calc_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل التاريخ بشكل صحيح")
            return
        if self.get_search_calc == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة التاريخ")
            return
        self.cur.execute(
            'select date, system_count, actual_income, difference from total_income'
            ' where date=?', (self.get_search_calc,))
        result = self.cur.fetchall()
        self.table9()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def explore_but(self):
        try:
            self.get_search_from_entry = str(self.search_from_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل تاريخ بداية الاستعلام بشكل صحيح")
            return
        if self.get_search_from_entry == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة تاريخ بداية الاستعلام")
            return

        try:
            self.get_search_to_entry = str(self.search_to_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل تاريخ نهاية الاستعلام بشكل صحيح")
            return
        if self.get_search_to_entry == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة تاريخ نهاية الاستعلام")
            return


        try:
            self.cur.execute("select num from total_income where date=?",
                             (str(self.get_search_from_entry),))
            from_date = self.cur.fetchall()
            self.from_date = ([tup[0] for tup in from_date])
            self.from_date = self.from_date[0]


            self.cur.execute("select num from total_income where date=?",
                             (str(self.get_search_to_entry),))
            to_date = self.cur.fetchall()
            self.to_date = ([tup[0] for tup in to_date])
            self.to_date = self.to_date[0]
        except:
            messagebox.showerror("خطأ", "من فضلك حدد المدة الزمنية بشكل صحيح")

        self.lim = int(self.to_date - self.from_date) + 1


        self.cur.execute("select system_count from total_income limit ? offset ?",
                         (self.lim,
                          self.from_date,))
        total_system_count = self.cur.fetchall()
        self.total_system_count = ([tup[0] for tup in total_system_count])
        self.system_counter = 0
        for i in range (0, len(self.total_system_count)):
            num = float(self.total_system_count[i])
            self.system_counter = float(self.system_counter + num)

        self.cur.execute("select actual_income from total_income limit ? offset ?",
                         (self.lim,
                          self.from_date,))
        total_actual_count = self.cur.fetchall()
        self.total_actual_count = ([tup[0] for tup in total_actual_count])
        self.actual_counter = 0
        for i in range(0, len(self.total_actual_count)):
            num = float(self.total_actual_count[i])
            self.actual_counter = float(self.actual_counter + num)

        self.deff = float(self.actual_counter - self.system_counter)


        if self.from_date >= self.to_date:
            messagebox.showerror("خطأ", "من فضلك ادخل التاريخ بشكل صحيح")
            return





        Label(self.calcframe, text=":اجمالي المبيعات", font="robot 18 bold", bg="black", fg="white").place(x=115,
                                                                                                           y=275)
        Label(self.calcframe, text=self.system_counter, font="robot 18 bold", bg="black", fg="white").place(x=35,
                                                                                               y=275)
        Label(self.calcframe, text=":اجمالي الدرج", font="robot 18 bold", bg="black", fg="white").place(x=133,
                                                                                                        y=350)
        Label(self.calcframe, text=self.actual_counter, font="robot 18 bold", bg="black", fg="white").place(x=35,
                                                                                               y=350)
        Label(self.calcframe, text=":الفرق", font="robot 18 bold", bg="black", fg="white").place(x=150,
                                                                                                 y=425)
        Label(self.calcframe, text=self.deff, font="robot 18 bold", bg="black", fg="white").place(x=35,
                                                                                               y=425)



    def calculations(self):
        self.calculation_w = Tk()
        width = 800
        height = 600
        screen_width = self.calculation_w.winfo_screenwidth()
        screen_height = self.calculation_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.calculation_w.geometry("%dx%d+%d+%d" % (width, height, x, y))


        self.calcframe = Frame(self.calculation_w, width=800, height=600, bg="#FFFFFF")
        self.calcframe.place(x=0, y=0, anchor=NW)
        self.calcframeinfo = self.calcframe.place_info()

        self.tableframe9 = LabelFrame(self.calculation_w, width=175, height=200)
        self.tableframe9.place(x=800, y=85, anchor=NE)
        self.tableframe9info = self.tableframe9.place_info()

        self.insert_calc()

        self.search_calc = Button(self.calcframe, text="بحث بالتاريخ", font="roboto 14", bg="#4267b2", bd=5,
                                         command=self.search_calc2)
        self.search_calc.place(x=350, y=20)

        self.searchvar3 = StringVar()
        self.search_calc_entry = Entry(self.calcframe, textvariable=self.searchvar3, font="roboto 14", width=20,
                                  bg="#FFFFFF")
        self.search_calc_entry.place(x=475, y=24)

        Label(self.calcframe, text=":الإستعلام عن فترة محددة", font="robot 18 bold", bg="black", fg="white").place(x=40, y=100)
        Label(self.calcframe, text=":من يوم", font="robot 12 bold", bg="black", fg="white").place(
            x=200, y=150)
        self.search_from_entry = Entry(self.calcframe, font="roboto 14", width=17,
                                       bg="#FFFFFF")
        self.search_from_entry.place(x=5, y=150)

        Label(self.calcframe, text=":الي يوم", font="robot 12 bold", bg="black", fg="white").place(
            x=200, y=200)
        self.search_to_entry = Entry(self.calcframe, font="roboto 14", width=17,
                                       bg="#FFFFFF")
        self.search_to_entry.place(x=5, y=200)

        self.explore = Button(self.calcframe, text="استعلام",font="robot 14 bold", bg="yellow", fg="black", command=self.explore_but).place(x=100, y=230)





        self.calculation_w.mainloop()


    def sales(self):
        self.tableframe.place_forget()
        self.itemframe.place_forget()
        self.formframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe1.place_forget()
        self.tableframe8.place_forget()
        self.returnframe.place_forget()
        self.salesframe2.place_forget()
        self.tableframe6.place_forget()
        self.tableframe7.place_forget()
        self.searchframe.place_forget()
        self.tableframe2.place_forget()
        self.tableframe3.place_forget()
        self.marketfrme.place_forget()
        self.storesframe.place_forget()
        #self.tableframe.place_forget()
        self.tableframe4.place_forget()
        self.tableframe5.place_forget()
        self.customers.place_forget()
        self.tableframe10.place_forget()
        self.salesframe.place(self.salesframeinfo)
        self.marketFun()

        self.stores_button = Button(self.salesframe, text="مخازن", width=18, font="robot 15 bold", bg="Purple", bd=5,
                                    command=self.storesFun)
        self.stores_button.place(x=430, y=10)
        #Label(self.salesframe, text="  ", bg="white").grid(row=0, column=4)
        self.market_button = Button(self.salesframe, text="ماركت", width=18, font="robot 15 bold", bg="Purple", bd=5,
                                    command=self.marketFun)
        self.market_button.place(x=670, y=10)

    def table4(self):
        scrollbarx = Scrollbar(self.tableframe4, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe4, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe4,
                                 columns=("Merchant", "Date", "Id", "Product Name"),
                                 selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=80)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)

        self.tree.heading('Merchant', text="رقم المخزن", anchor=W)
        self.tree.heading('Date', text="اسم الصنف", anchor=W)
        self.tree.heading('Id', text="الكمية", anchor=W)
        self.tree.heading('Product Name', text="سعر الوحدة", anchor=W)

        Label(self.tableframe4, ).grid(row=1, column=4)
        Label(self.tableframe4, ).grid(row=2, column=4)
        Label(self.tableframe4, ).grid(row=3, column=4)

        self.tree.grid(row=4, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=5, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=4, column=1, sticky="ns", pady=30)

    def table5(self):
        scrollbarx = Scrollbar(self.tableframe5, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe5, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe5,
                                 columns=("Merchant", "Date", "Id", "Product Name"),
                                 selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=80)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)

        self.tree.heading('Merchant', text="رقم المخزن", anchor=W)
        self.tree.heading('Date', text="اسم الصنف", anchor=W)
        self.tree.heading('Id', text="الكمية", anchor=W)
        self.tree.heading('Product Name', text="سعر الكمية بيع", anchor=W)

        self.tree.grid(row=0, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=1, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=0, column=1, sticky="ns", pady=30)

    def table6(self):
        scrollbarx = Scrollbar(self.tableframe6, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe6, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe6,
                                 columns=("Date", "Id", "Product Name"),
                                 selectmode="extended", height=17,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=80)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)

        self.tree.heading('Date', text="اسم الصنف", anchor=W)
        self.tree.heading('Id', text="الكمية", anchor=W)
        self.tree.heading('Product Name', text="سعر الوحدة", anchor=W)

        Label(self.tableframe6, text="   ").grid(row=1, column=0)
        Label(self.tableframe6, text="   ").grid(row=2, column=0)
        Label(self.tableframe6, text="   ").grid(row=3, column=0)

        self.tree.grid(row=4, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=5, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=4, column=1, sticky="ns", pady=30)

    def table7(self):
        scrollbarx = Scrollbar(self.tableframe7, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe7, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe7,
                                 columns=("Merchant", "Date", "Id", "Product Name"),
                                 selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=80)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)

        self.tree.heading('Merchant', text="تاريخ البيع", anchor=W)
        self.tree.heading('Date', text="اسم الصنف", anchor=W)
        self.tree.heading('Id', text="الكمية", anchor=W)
        self.tree.heading('Product Name', text="سعر الكمية", anchor=W)

        self.tree.grid(row=0, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=1, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=0, column=1, sticky="ns", pady=30)

    def storesFun(self):
        self.tableframe6.place_forget()
        self.tableframe8.place_forget()
        self.salesframe2.place_forget()
        self.tableframe7.place_forget()
        self.returnframe.place_forget()
        self.searchframe.place_forget()
        self.tableframe2.place_forget()
        self.tableframe3.place_forget()
        self.marketfrme.place_forget()
        self.tableframe.place_forget()
        self.formframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe1.place_forget()
        self.itemframe.place_forget()
        self.customers.place_forget()
        self.tableframe10.place_forget()
        self.tableframe4.place(self.tableframe4info)
        self.tableframe5.place(self.tableframe5info)
        self.salesframe.place(self.salesframeinfo)
        self.storesframe.place(self.storesframeinfo)
        self.cur.execute("delete from stores where product_quantity = 0")

        self.table4()

        self.store_entry = Entry(self.tableframe4, width=20, bg="light gray")

        self.store_entry.place(x=320, y=10, height=40)
        self.search_name = Button(self.tableframe4, text='بحث بالصنف', width=12, font="robot 12 bold", bg="#4267b2",
                                  bd=5, command=self.search_store_table1)
        self.search_name.place(x=20, y=10)
        self.search_storeroom = Button(self.tableframe4, text='بحث برقم المخزن', width=12, font="robot 12 bold",
                                       bg="#4267b2",
                                       bd=5, command=self.search_store_table2)
        self.search_storeroom.place(x=160, y=10)

        self.storeroom_num_label = Label(self.storesframe, text="رقم المخزن", font="robot 12 bold", bg="light gray",
                                         width=15).place(x=205, y=20)
        self.storeroom_num = Entry(self.storesframe, bg="light gray", width=30)
        self.storeroom_num.place(x=0, y=20)

        self.product_pull_label = Label(self.storesframe, text="اسم الصنف", font="robot 12 bold",
                                        bg="light gray", width=15).place(x=205, y=50)
        self.product_pull = Entry(self.storesframe, bg="light gray", width=30)
        self.product_pull.place(x=0, y=50)

        self.quantity_pull_label = Label(self.storesframe, text="الكمية", font="robot 12 bold",
                                         bg="light gray", width=15).place(x=205, y=80)
        self.quantity_pull = Entry(self.storesframe, bg="light gray", width=30)
        self.quantity_pull.place(x=0, y=80)
        self.pull = Button(self.storesframe, text="سحب", width=14, font="robot 12 bold", bg="#4267b2",
                           command=self.pull_button)
        self.pull.place(x=205, y=200)

        self.add = Button(self.storesframe, text="اضافة", width=16, font="robot 12 bold", bg="#4267b2",
                          command=self.add_to_market)
        self.add.place(x=100, y=110)


        self.sell = Button(self.storesframe, text="بيع", width=17, font="robot 12 bold", bg="#4267b2", command=self.sell_button_store)
        self.sell.place(x=0, y=200)

        self.delete = Button(self.storesframe, text="حذف", width=17, font="robot 12 bold", bg="yellow",
                             command=self.delete_pulled_item)
        self.delete.place(x=0, y=240)



        self.store_history = Button(self.storesframe, text="سجل السحب", width=17, font="robot 14 bold", bg="#4267b2", command=self.pull_history)
        self.store_history.place(x=100, y=290)

        self.insert_store()

        scrollbarx = Scrollbar(self.tableframe5, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe5, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe5,
                                 columns=("Merchant", "Date", "Id", "Product Name"),
                                 selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=80)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)

        self.tree.heading('Merchant', text="رقم المخزن", anchor=W)
        self.tree.heading('Date', text="اسم الصنف", anchor=W)
        self.tree.heading('Id', text="الكمية", anchor=W)
        self.tree.heading('Product Name', text="سعر الكمية بيع", anchor=W)

        self.tree.grid(row=0, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=1, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=0, column=1, sticky="ns", pady=30)

    def Return_To_Stores(self):
        self.return_to_store_w = Tk()
        width = 380
        height = 250
        screen_width = self.return_to_store_w.winfo_screenwidth()
        screen_height = self.return_to_store_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.return_to_store_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.return_storeroom_num_label = Label(self.return_to_store_w, text="رقم المخزن", font="robot 12 bold", bg="light gray",
                                               width=15).place(x=205, y=20)
        self.return_storeroom_num = Entry(self.return_to_store_w, bg="light gray", width=30)
        self.return_storeroom_num.place(x=5, y=20)

        self.return_to_store_product_label = Label(self.return_to_store_w, text="اسم الصنف", font="robot 12 bold", bg="light gray",
                                               width=15).place(x=205, y=50)
        self.return_to_store_product = Entry(self.return_to_store_w, bg="light gray", width=30)
        self.return_to_store_product.place(x=5, y=50)

        self.return_to_store_quantity_label = Label(self.return_to_store_w, text="الكمية", font="robot 12 bold",
                                           bg="light gray", width=15).place(x=205, y=80)
        self.return_to_store_quantity = Entry(self.return_to_store_w, bg="light gray", width=30)
        self.return_to_store_quantity.place(x=5, y=80)

        self.return_to_store_unitprice_label = Label(self.return_to_store_w, text="سعر الوحدة", font="robot 12 bold",
                                        bg="light gray", width=15).place(x=205, y=110)
        self.return_to_store_unitprice = Entry(self.return_to_store_w, bg="light gray", width=30)
        self.return_to_store_unitprice.place(x=5, y=110)
        self.return_to_store_button = Button(self.return_to_store_w, text="ارجاع الصنف للمخزن",font="roboto 16 bold",
                                             bg="#4267b2", width=20, command=self.return_product_to_store)
        self.return_to_store_button.place(x=13, y=140)

        self.return_to_store_w.mainloop()

    def return_product_to_store(self):
        try:
            self.get_return_storeroom_num = int(self.return_storeroom_num.get())
            self.get_return_to_store_product = str(self.return_to_store_product.get())
            self.get_return_to_store_quantity = int(self.return_to_store_quantity.get())
            self.get_return_to_store_unitprice = float(self.return_to_store_unitprice.get())
        except:
            messagebox.showerror("خطأ", "من فضلك ادخل معلومات صحيحة")
        try:
            self.cur.execute("select product_name from market_items where  "
                             "product_name =? and quantity_price=?;",
                             (str(self.get_return_to_store_product),
                              float(self.get_return_to_store_unitprice)))
            ex_product_in_market = self.cur.fetchall()
            self.ex_product_in_market = ([tup[0] for tup in ex_product_in_market])
            self.ex_product_in_market = self.ex_product_in_market[0]
        except:
            messagebox.showerror("خطأ", "هذا الصنف غير موجود بالماركت")
            return

        if self.get_return_to_store_product in self.ex_product_in_market:
            li = [self.get_return_storeroom_num, self.get_return_to_store_product, self.get_return_to_store_unitprice]

            # self.cur.execute("delete from stores;")
            self.cur.execute("create table if not exists check_return_to_store"
                             "(product_Storeroom integer not null,"
                             "product_name varchar(30) not null,"
                             "product_quantity integer not null,"
                             "product_unit_price float not null);")

            self.cur.execute("insert into check_return_to_store values(?,?,?,?);",
                             (int(self.get_return_storeroom_num),
                              str(self.get_return_to_store_product),
                              int(self.get_return_to_store_quantity),
                              float(self.get_return_to_store_unitprice)))

            self.cur.execute("select product_name from stores;")
            ex_product = self.cur.fetchall()
            self.products_in_stores = ([tup[0] for tup in ex_product])

            if self.get_return_to_store_product not in self.products_in_stores:
                self.cur.execute("insert into stores select * from check_return_to_store;")
                self.cur.execute("select product_quantity from market_items  where  "
                                 "product_name =? and quantity_price=?;",
                                 (str(self.get_return_to_store_product),
                                  float(self.get_return_to_store_unitprice)))
                old_quantity = self.cur.fetchall()
                self.old_quantity_before = ([tup[0] for tup in old_quantity])
                self.old_quantity_before = self.old_quantity_before[0]
                self.new_quantity_in_market = int(abs(self.get_return_to_store_quantity - self.old_quantity_before))
                self.cur.execute("update market_items set product_quantity=? where  "
                                 "product_name =? and quantity_price=?;",
                                 (int(self.new_quantity_in_market),
                                  str(self.get_return_to_store_product),
                                  float(self.get_return_to_store_unitprice)))

            if self.get_return_to_store_product in self.products_in_stores:

                counter = 0
                self.cur.execute("select product_Storeroom from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_return_storeroom_num),
                                  str(self.get_return_to_store_product),
                                  float(self.get_return_to_store_unitprice)))
                match = self.cur.fetchall()
                self.match_in_store1 = ([tup[0] for tup in match])
                self.match_in_store1 = self.match_in_store1[0]

                self.cur.execute("select product_name from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_return_storeroom_num),
                                  str(self.get_return_to_store_product),
                                  float(self.get_return_to_store_unitprice)))

                match2 = self.cur.fetchall()
                self.match_in_store2 = ([tup[0] for tup in match2])
                self.match_in_store2 = self.match_in_store2[0]

                self.cur.execute("select product_unit_price from stores where  "
                                 "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                 (int(self.get_return_storeroom_num),
                                  str(self.get_return_to_store_product),
                                  float(self.get_return_to_store_unitprice)))

                match3 = self.cur.fetchall()
                self.match_in_store3 = ([tup[0] for tup in match3])
                self.match_in_store3 = self.match_in_store3[0]
                self.match_all_in_store = [self.match_in_store1, self.match_in_store2, self.match_in_store3]

                if self.match_all_in_store != "":
                    for i in li:
                        if i in self.match_all_in_store:
                            counter += 1

                if counter == 3:
                    self.cur.execute("select product_quantity from stores  where  "
                                    "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                     (int(self.get_return_storeroom_num),
                                      str(self.get_return_to_store_product),
                                      float(self.get_return_to_store_unitprice)))
                    old_quantity = self.cur.fetchall()
                    self.old_quantity_before = ([tup[0] for tup in old_quantity])
                    self.old_quantity_before = self.old_quantity_before[0]

                    self.new_quantity_in_store = int(self.get_return_to_store_quantity + self.old_quantity_before)
                    self.new_quantity_in_market = int(abs(self.get_return_to_store_quantity - self.old_quantity_before))

                    self.cur.execute("update stores set product_quantity=? where  "
                                    "product_Storeroom=? and product_name =? and product_unit_price=?;",
                                     (int(self.new_quantity_in_store),
                                      int(self.get_return_storeroom_num),
                                      str(self.get_return_to_store_product),
                                      float(self.get_return_to_store_unitprice)))
                    self.cur.execute("update market_items set product_quantity=? where  "
                                     "product_name =? and quantity_price=?;",
                                     (int(self.new_quantity_in_market),
                                      str(self.get_return_to_store_product),
                                      float(self.get_return_to_store_unitprice)))
            self.cur.execute("delete from market_items where product_quantity = 0")
            self.cur.execute("delete from check_return_to_store;")
            self.insert_market_items()
            self.new_text = ""
            self.return_storeroom_num.delete(0, END)
            self.return_storeroom_num.insert(0, self.new_text)

            self.return_to_store_product.delete(0, END)
            self.return_to_store_product.insert(0, self.new_text)

            self.return_to_store_quantity.delete(0, END)
            self.return_to_store_quantity.insert(0, self.new_text)

            self.return_to_store_unitprice.delete(0, END)
            self.return_to_store_unitprice.insert(0, self.new_text)
            self.base.commit()

    def search_store_table1(self):
        ans = ''
        try:
            self.get_store_entry = str(self.store_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل اسم الصنف بشكل صحيح")
            return
        if self.get_store_entry == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم الصنف")
            return
        self.cur.execute(
            'select product_storeroom, product_name, product_quantity, product_unit_price from stores'
            ' where product_name=?', (self.get_store_entry,))
        result = self.cur.fetchall()
        self.table4()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def search_store_table2(self):
        ans = ''
        try:
            self.get_store_entry = int(self.store_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل رقم المخزن بشكل صحيح")
            return
        if self.get_store_entry == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة رقم المخزن")
            return
        self.cur.execute(
            'select product_storeroom, product_name, product_quantity, product_unit_price from stores'
            ' where product_storeroom=?', (self.get_store_entry,))
        result = self.cur.fetchall()
        self.table4()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def insert_store(self):

        self.cur.execute("select * from stores;")
        self.store_info = self.cur.fetchall()
        self.table4()
        self.base.commit()

        x = 0
        ans = ''
        for i in self.store_info:
            self.tree.insert('', 'end', values=i)
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]
        return ans

    def marketFun(self):
        self.salesframe2.place_forget()
        self.returnframe.place_forget()
        self.searchframe.place_forget()
        self.tableframe2.place_forget()
        self.tableframe3.place_forget()
        self.tableframe.place_forget()
        self.formframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe1.place_forget()
        self.itemframe.place_forget()
        self.tableframe8.place_forget()
        self.customers.place_forget()
        self.tableframe10.place_forget()
        self.salesframe.place(self.salesframeinfo)
        self.storesframe.place_forget()
        self.marketfrme.place(self.marketfrmeinfo)
        self.tableframe4.place_forget()
        self.tableframe5.place_forget()
        self.tableframe6.place(self.tableframe6info)
        self.tableframe7.place(self.tableframe7info)
        self.cur.execute("delete from market_items where product_quantity = 0")
        self.table6()
        self.insert_market_items()
        self.market_entry = Entry(self.tableframe6, width=20, bg="light gray")

        self.market_entry.place(x=200, y=10, height=40)
        self.search_name_m = Button(self.tableframe6, text='بحث بالصنف', width=12, font="robot 12 bold", bg="#4267b2",
                                    bd=5, command=self.search_market_table)
        self.search_name_m.place(x=38, y=10)

        self.product_name_market_label = Label(self.marketfrme, text="اسم الصنف", font="robot 12 bold", bg="light gray",
                                               width=15).place(x=205, y=20)
        self.product_name_market = Entry(self.marketfrme, bg="light gray", width=30)
        self.product_name_market.place(x=0, y=20)

        self.quantity_market_label = Label(self.marketfrme, text="الكمية", font="robot 12 bold",
                                           bg="light gray", width=15).place(x=205, y=50)
        self.quantity_market = Entry(self.marketfrme, bg="light gray", width=30)
        self.quantity_market.place(x=0, y=50)

        self.price_market_label = Label(self.marketfrme, text="سعر الكمية", font="robot 12 bold",
                                        bg="light gray", width=15).place(x=205, y=80)
        self.price_market = Entry(self.marketfrme, bg="light gray", width=30)
        self.price_market.place(x=0, y=80)

        self.sell_market = Button(self.marketfrme, text="بيع", width=14, font="robot 12 bold", bg="#4267b2", command=self.sell_button)
        self.sell_market.place(x=205, y=130)

        self.add_market = Button(self.marketfrme, text="اضافة", width=16, font="robot 12 bold", bg="#4267b2",
                                 command=self.add_to_sales)
        self.add_market.place(x=0, y=130)

        self.delete_market = Button(self.marketfrme, text="حذف", width=16, font="robot 12 bold", bg="yellow",
                                    command=self.delete_sold_item)
        self.delete_market.place(x=0, y=180)



        self.table7()


    def Get_to_market(self, x=0):
        ans = ''
        self.table5()
        self.cur.execute(
            "select * from market_table;")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def add_to_market(self):
        #self.cur.execute("drop table market_table")
        self.cur.execute("create table if not exists market_table"
                         "(storeroom_num INTEGER not null,"
                         "product_name varchar(30) not null,"
                         "quantity INTEGER not null,"
                         "quantity_price float not null);")
        try:
            self.get_storeroom_num = int(self.storeroom_num.get())
            self.get_product_pull = str(self.product_pull.get())
            self.get_quantity_pull = int(self.quantity_pull.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل بيانات صحيحة")

        if self.get_storeroom_num == "" or self.get_product_pull == "" or self.get_quantity_pull=="":
            messagebox.showerror("خطأ", "من فضلك ادخل جميع البيانات")

        if self.get_quantity_pull <= 0:
            messagebox.showerror("خطأ", "من فضلك أدخل الكمية مرة أخرى")
            return


        li = [self.get_storeroom_num, self.get_product_pull]
        self.cur.execute("select product_name from stores;")
        ex_product = self.cur.fetchall()
        self.ex_product = ([tup[0] for tup in ex_product])

        if self.get_product_pull not in self.ex_product:
            messagebox.showerror("خطأ", "هذا الصنف غير موجود بالمخزن")
            return

        if self.get_product_pull in self.ex_product:
            counter = 0
            try:
                self.cur.execute("select product_Storeroom from stores where  "
                                 "product_Storeroom=? and product_name =?;",
                                 (int(self.get_storeroom_num),
                                  str(self.get_product_pull)))
                match11 = self.cur.fetchall()
                self.match11 = ([tup[0] for tup in match11])
                self.match11 = self.match11[0]
            except:
                messagebox.showerror("خطأ", "البيانات المدخلة غير صحيحة")

            self.cur.execute("select product_name from stores where  "
                             "product_Storeroom=? and product_name =?;",
                             (int(self.get_storeroom_num),
                              str(self.get_product_pull)))

            match22 = self.cur.fetchall()
            self.match22 = ([tup[0] for tup in match22])
            self.match22 = self.match22[0]

            self.matchB = [self.match11, self.match22]

            if self.matchB != "":
                for i in li:
                    if i in self.matchB:
                        counter += 1

            if counter == 2:
                self.cur.execute("select product_quantity from stores where product_name = ? "
                                 "and product_Storeroom=? ", (str(self.get_product_pull),
                                                              int(self.get_storeroom_num)))
                old_quantity = self.cur.fetchall()
                self.old_quantity1 = ([tup[0] for tup in old_quantity])
                self.old_quantity1 = self.old_quantity1[0]

                self.new_quantity1 = int(self.old_quantity1 - self.get_quantity_pull)

                if self.new_quantity1 < 0:
                    messagebox.showerror("خطأ", "الكمية المطلوبة غير متوفرة بالمخزن")
                    return

                if self.new_quantity1 == 0:
                    messagebox.showerror("تنبيه", "الكمية المتبقية من هذا الصنف في المخزن 0 برجاء استيراد كمية جديدة ")

                self.cur.execute("update stores set product_quantity=? where product_name = ? and product_Storeroom=?",
                                 (self.new_quantity1,
                                  str(self.get_product_pull),
                                  int(self.get_storeroom_num)))


        self.cur.execute("select product_unit_price from today_income where product_name=? and product_storeroom=?",
                         (str(self.get_product_pull),
                         int(self.get_storeroom_num)))
        unit_price3 = self.cur.fetchall()
        self.the_unit_price2 = ([tup[0] for tup in unit_price3])
        self.the_unit_price2 = self.the_unit_price2[0]


        self.cur.execute('insert into market_table values(?,?,?,?)', (
            int(self.get_storeroom_num),
            str(self.get_product_pull),
            int(self.get_quantity_pull),
            float(self.the_unit_price2)))

        self.cur.execute("create table if not exists market_items"
                         "(product_name varchar(30) not null,"
                         "product_quantity integer not null,"
                         "quantity_price float not null);")

        self.cur.execute("select product_name from market_items;")
        ex_market_product = self.cur.fetchall()
        self.ex_market_product = ([tup[0] for tup in ex_market_product])

        if self.get_product_pull not in self.ex_market_product:
            self.cur.execute("insert into market_items select product_name, quantity, quantity_price"
                             " from market_table;")
            self.cur.execute("select product_unit_price from stores where product_name=? and product_Storeroom=?",
                             (self.get_product_pull, self.get_storeroom_num))
            unit_price = self.cur.fetchall()
            self.the_unit_price = ([tup[0] for tup in unit_price])
            self.the_unit_price = self.the_unit_price[0]
            self.cur.execute("update market_items set quantity_price = ? where product_name = ?",
                             (self.the_unit_price, self.get_product_pull))

        if self.get_product_pull in self.ex_market_product:
            self.cur.execute("select product_quantity from market_items where product_name = ? ",
                             (str(self.get_product_pull),))
            old_quantity11 = self.cur.fetchall()
            self.old_quantity2 = ([tup[0] for tup in old_quantity11])
            self.old_quantity2 = self.old_quantity2[0]

            self.new_quantity2 = int(self.get_quantity_pull + self.old_quantity2)

            self.cur.execute("update market_items set product_quantity=? where product_name = ?",
                             (self.new_quantity2,
                              str(self.get_product_pull)))



        self.Get_to_market()
        self.table4()
        self.insert_store()
        self.base.commit()
        self.new_text2 = ""
        self.storeroom_num.delete(0, END)
        self.storeroom_num.insert(0, self.new_text2)

        self.product_pull.delete(0, END)
        self.product_pull.insert(0, self.new_text2)

        self.quantity_pull.delete(0, END)
        self.quantity_pull.insert(0, self.new_text2)

    def insert_market_items(self):
        ans = ''

        self.cur.execute("select * from market_items;")
        productlist = self.cur.fetchall()
        self.table6()
        x = 0
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def delete_pulled_item(self):
        self.delete_pulled_item_w = Tk()
        width = 300
        height = 100
        screen_width = self.delete_pulled_item_w.winfo_screenwidth()
        screen_height = self.delete_pulled_item_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.delete_pulled_item_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.delete_pulled_item_entry = Entry(self.delete_pulled_item_w, bg="light grey", font="robot 14")
        self.delete_pulled_item_entry.grid(row=2, column=1)
        self.delete_pulled_item_label = Label(self.delete_pulled_item_w, text="ادخل اسم الصنف", font="roboto 14 bold",
                                              bg="#FFFFFF")
        self.delete_pulled_item_label.grid(row=2, column=2)

        self.delete_pulled_item_entry2 = Entry(self.delete_pulled_item_w, bg="light grey", font="robot 14")
        self.delete_pulled_item_entry2.grid(row=3, column=1)
        self.delete_pulled_item_label2 = Label(self.delete_pulled_item_w, text="ادخل رقم المخزن", font="roboto 14 bold",
                                              bg="#FFFFFF")
        self.delete_pulled_item_label2.grid(row=3, column=2)

        self.delete_pulled_item_button = Button(self.delete_pulled_item_w, text="حذف", font="robot 16 bold", fg="black",
                                                bg="yellow",
                                                command=self.final_delete_pulled_item)
        self.delete_pulled_item_button.grid(row=4, column=1)
        self.delete_pulled_item_w.mainloop()

    def final_delete_pulled_item(self):
        self.get_delete_pulled_item_entry = str(self.delete_pulled_item_entry.get())
        self.get_delete_pulled_item_entry2 = int(self.delete_pulled_item_entry2.get())

        self.cur.execute("select quantity from market_table where product_name = ? ",
                         (str(self.get_delete_pulled_item_entry),))
        old_quantity = self.cur.fetchall()
        self.old_quantity3 = ([tup[0] for tup in old_quantity])
        self.old_quantity3 = self.old_quantity3[0]

        self.cur.execute("select product_quantity from market_items where product_name = ? ",
                         (str(self.get_delete_pulled_item_entry),))
        old_quantity2 = self.cur.fetchall()
        self.old_quantity4 = ([tup[0] for tup in old_quantity2])
        self.old_quantity4 = self.old_quantity4[0]
        self.new_quantity5 = int(abs(self.old_quantity4 - self.old_quantity3))
        self.cur.execute("update market_items set product_quantity=? where product_name = ?",
                         (self.new_quantity5,
                          str(self.get_delete_pulled_item_entry)))


        self.cur.execute("select product_quantity from stores where product_name = ? and product_Storeroom = ? ",
                         (str(self.get_delete_pulled_item_entry),
                          int(self.get_delete_pulled_item_entry2)))
        old_quantity0 = self.cur.fetchall()
        self.old_quantity6 = ([tup[0] for tup in old_quantity0])
        self.old_quantity6 = self.old_quantity6[0]

        self.new_quantity6 = int(abs(self.old_quantity6 + self.old_quantity3))

        self.cur.execute("update stores set product_quantity=? where product_name = ? and product_Storeroom = ?",
                         (self.new_quantity6,
                          str(self.get_delete_pulled_item_entry),
                          int(self.get_delete_pulled_item_entry2)))

        self.cur.execute("delete from market_table where product_name = ?;", (self.get_delete_pulled_item_entry,))
        self.base.commit()
        self.delete_pulled_item_w.destroy()
        self.Get_to_market()
        self.insert_store()

    def sell_button_store(self):
        self.add2 = Button(self.storesframe, text="اضافة", width=16, font="robot 12 bold", bg="#4267b2", command=self.sold_items_fromstore)
        self.add2.place(x=100, y=110)

        self.sell2 = Button(self.storesframe, text="بيع", width=17, font="robot 12 bold", bg="#4267b2", command=self.sell_but)
        self.sell2.place(x=0, y=200)

        self.price_label = Label(self.storesframe, text="سعر البيع", font="robot 12 bold", bg="light gray",
                                         width=15).place(x=205, y=150)
        self.price_entry = Entry(self.storesframe, bg="light gray", width=30)
        self.price_entry.place(x=0, y=152)

        self.delete1 = Button(self.storesframe, text="حذف", width=17, font="robot 12 bold", bg="yellow",
                             command=self.delete_sold_item_fromstore)
        self.delete1.place(x=0, y=240)



    def sold_items_fromstore(self):
        try:
            self.get_storeroom_num = int(self.storeroom_num.get())
            self.get_product_pull = str(self.product_pull.get())
            self.get_quantity_pull = int(self.quantity_pull.get())
            self.get_price = float(self.price_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل بيانات صحيحة")

        if self.get_storeroom_num == "" or self.get_product_pull == "" or self.get_quantity_pull=="":
            messagebox.showerror("خطأ", "من فضلك ادخل جميع البيانات")
        elif self.get_price == "":
            messagebox.showerror("خطأ", "من فضلك ادخل جميع البيانات")

        if self.get_quantity_pull <= 0:
            messagebox.showerror("خطأ", "من فضلك أدخل الكمية مرة أخرى")
            return


        li = [self.get_storeroom_num, self.get_product_pull]
        self.cur.execute("select product_name from stores;")
        ex_product2 = self.cur.fetchall()
        self.ex_product_2 = ([tup[0] for tup in ex_product2])

        if self.get_product_pull not in self.ex_product_2:
            messagebox.showerror("خطأ", "هذا الصنف غير موجود بالمخزن")
            return

        if self.get_product_pull in self.ex_product_2:
            counter = 0
            try:
                self.cur.execute("select product_Storeroom from stores where  "
                                 "product_Storeroom=? and product_name =?;",
                                 (int(self.get_storeroom_num),
                                  str(self.get_product_pull)))
                match111 = self.cur.fetchall()
                self.match111 = ([tup[0] for tup in match111])
                self.match111 = self.match111[0]
            except:
                messagebox.showerror("خطأ", "البيانات المدخلة غير صحيحة")




            self.cur.execute("select product_name from stores where  "
                             "product_Storeroom=? and product_name =?;",
                             (int(self.get_storeroom_num),
                              str(self.get_product_pull)))

            match222 = self.cur.fetchall()
            self.match222 = ([tup[0] for tup in match222])
            self.match222 = self.match222[0]

            self.matchBB = [self.match111, self.match222]



            if self.matchBB != "":
                for i in li:
                    if i in self.matchBB:
                        counter += 1

            if counter == 2:
                self.cur.execute("select product_quantity from stores where product_name = ? "
                                 "and product_Storeroom=? ", (str(self.get_product_pull),
                                                              int(self.get_storeroom_num)))
                old_quantity = self.cur.fetchall()
                self.old_quantity11 = ([tup[0] for tup in old_quantity])
                self.old_quantity11 = self.old_quantity11[0]

                self.new_quantity11 = int(self.old_quantity11 - self.get_quantity_pull)

                if self.new_quantity11 < 0:
                    messagebox.showerror("خطأ", "الكمية المطلوبة غير متوفرة بالمخزن")
                    return

                if self.new_quantity11 == 0:
                    messagebox.showerror("تنبيه", "الكمية المتبقية من هذا الصنف في المخزن 0 برجاء استيراد كمية جديدة ")

                self.cur.execute("update stores set product_quantity=? where product_name = ? and product_Storeroom=?",
                                 (self.new_quantity11,
                                  str(self.get_product_pull),
                                  int(self.get_storeroom_num)))



        today = datetime.date(datetime.now())
        self.format_date2 = str(today.strftime("%d/%m/%Y"))
        self.salling_date_store = self.format_date2

        self.cur.execute("INSERT INTO sales_history values(?,?,?,?)", (
            str(self.salling_date_store),
            str(self.get_product_pull),
            int(self.get_quantity_pull),
            float(self.get_price)))




        self.Get_to_market()
        self.table4()
        self.insert_store()
        self.base.commit()

        self.new_text2 = ""
        self.storeroom_num.delete(0, END)
        self.storeroom_num.insert(0, self.new_text2)

        self.product_pull.delete(0, END)
        self.product_pull.insert(0, self.new_text2)

        self.quantity_pull.delete(0, END)
        self.quantity_pull.insert(0, self.new_text2)

        self.price_entry.delete(0, END)
        self.price_entry.insert(0, self.new_text2)




    def sell_but(self):
        if messagebox.askyesno("تنبيه", "هل تريد بيع هذه الاصناف") == True:
            #self.cur.execute('drop table to_market_table_new;')

            self.cur.execute("delete from market_table;")
            self.base.commit()
            self.table5()
            self.add2.destroy()
            self.sell2.destroy()
            self.price_entry.destroy()
            self.price_label = Label(self.storesframe, text="", font="robot 12 bold", bg="#FFFFFF",
                                     width=15).place(x=205, y=150)
            self.delete1.destroy()


    def delete_sold_item_fromstore(self):
        self.delete_sold_item_fromstore_w = Tk()
        width = 300
        height = 100
        screen_width = self.delete_sold_item_fromstore_w.winfo_screenwidth()
        screen_height = self.delete_sold_item_fromstore_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.delete_sold_item_fromstore_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.delete_sold_item__ftomstore_entry = Entry(self.delete_sold_item_fromstore_w, bg="light grey", font="robot 14")
        self.delete_sold_item__ftomstore_entry.grid(row=2, column=1)

        self.delete_sold_item_fromstore_label = Label(self.delete_sold_item_fromstore_w, text="ادخل اسم الصنف", font="roboto 14 bold",
                                              bg="#FFFFFF")
        self.delete_sold_item_fromstore_label.grid(row=2, column=2)

        self.delete_sold_item__ftomstore_entry2 = Entry(self.delete_sold_item_fromstore_w, bg="light grey", font="robot 14")
        self.delete_sold_item__ftomstore_entry2.grid(row=3, column=1)

        self.delete_sold_item_fromstore_label2 = Label(self.delete_sold_item_fromstore_w, text="ادخل رقم المخزن", font="roboto 14 bold",
                                              bg="#FFFFFF")
        self.delete_sold_item_fromstore_label2.grid(row=3, column=2)

        self.delete_sold_item_fromstore_button = Button(self.delete_sold_item_fromstore_w, text="حذف", font="robot 16 bold", fg="black",
                                                bg="yellow",
                                                command=self.final_delete_sold_item_fromstore)
        self.delete_sold_item_fromstore_button.grid(row=4, column=1)
        self.delete_sold_item_fromstore_w.mainloop()

    def final_delete_sold_item_fromstore(self):
        self.get_delete_sold_item__ftomstore_entry = str(self.delete_sold_item__ftomstore_entry.get())
        self.get_delete_sold_item__ftomstore_entry2 = int(self.delete_sold_item__ftomstore_entry2.get())

        self.cur.execute("select quantity from market_table where product_name = ? ",
                         (str(self.get_delete_sold_item__ftomstore_entry),))
        old_quantity = self.cur.fetchall()
        self.old_quantity33 = ([tup[0] for tup in old_quantity])
        self.old_quantity33 = self.old_quantity33[0]

        self.cur.execute("select product_quantity from sales_history where product_name = ? ",
                         (str(self.get_delete_sold_item__ftomstore_entry),))
        old_quantity2 = self.cur.fetchall()
        self.old_quantity44 = ([tup[0] for tup in old_quantity2])
        self.old_quantity44 = self.old_quantity44[0]
        self.new_quantity55 = int(abs(self.old_quantity44 - self.old_quantity33))

        self.cur.execute("delete from sales_history where product_name = ? and product_quantity=? and sales_date=?",
                         (str(self.get_delete_sold_item__ftomstore_entry),
                          int(self.get_quantity_pull),
                          str(self.salling_date_store)))


        self.cur.execute("select product_quantity from stores where product_name = ? and product_Storeroom = ? ",
                         (str(self.get_delete_sold_item__ftomstore_entry),
                          int(self.get_delete_sold_item__ftomstore_entry2)))
        old_quantity0 = self.cur.fetchall()
        self.old_quantity66 = ([tup[0] for tup in old_quantity0])
        self.old_quantity66 = self.old_quantity66[0]

        self.new_quantity66 = int(abs(self.old_quantity66 + self.old_quantity33))

        self.cur.execute("update stores set product_quantity=? where product_name = ? and product_Storeroom = ?",
                         (self.new_quantity66,
                          str(self.get_delete_sold_item__ftomstore_entry),
                          int(self.get_delete_sold_item__ftomstore_entry2)))

        self.cur.execute("delete from market_table where product_name = ?;", (self.get_delete_sold_item__ftomstore_entry,))
        self.base.commit()
        self.delete_sold_item_fromstore_w.destroy()
        self.Get_to_market()
        self.insert_store()






    def pull_button(self):
        if messagebox.askyesno("تنبيه", "هل تريد سحب هذه الاصناف") == True:
            #self.cur.execute('drop table to_market_table_new;')
            self.cur.execute("create table if not exists to_market_table_new"
                             "(storeroom_num INTEGER not null,"
                             "product_name varchar(30) not null,"
                             "quantity INTEGER not null,"
                             "price float not null);")

            self.cur.execute("INSERT INTO to_market_table_new select * FROM market_table;")
            self.cur.execute("delete from market_table;")
            self.base.commit()
            self.table5()

    def pull_history_table(self):
        scrollbarx = Scrollbar(self.pullhistory_table_frame, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.pullhistory_table_frame, orient=VERTICAL)
        self.tree = ttk.Treeview(self.pullhistory_table_frame,
                                 columns=("Merchant", "Date", "Id", "Product Name", "Quantity"),
                                 selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=80)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=80)

        self.tree.heading('Merchant', text="رقم المخزن", anchor=W)
        self.tree.heading('Date', text="اسم الصنف", anchor=W)
        self.tree.heading('Id', text="الكمية", anchor=W)
        self.tree.heading('Product Name', text="سعر الكمية بيع", anchor=W)
        self.tree.heading('Quantity', text="تاريخ السحب", anchor=W)

        self.tree.grid(row=0, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=1, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=0, column=1, sticky="ns", pady=30)


    def Get_pullhistory(self, x=0):
        ans = ''
        x = 0
        self.cur.execute(
            "select * from to_market_table_new;")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans


    def pull_history(self):
        self.pullhistoryw = Tk()
        width = 700
        height = 500
        screen_width = self.pullhistoryw.winfo_screenwidth()
        screen_height = self.pullhistoryw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.pullhistoryw.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.pullhistory_table_frame = Frame(self.pullhistoryw, width=1400, height=450, bg="#FFFFFF")
        self.pullhistory_table_frame.place(x=120, y=80)
        self.pullhistory_table_frame_info = self.searchframe.place_info()

        self.searchbutton = Button(self.pullhistoryw, text="بحث بالتاريخ", font="roboto 14", bg="#FFFFFF", bd=5)
        self.searchbutton.place(x=240, y=10)

        self.searchbutton2 = Button(self.pullhistoryw, text="بحث بالصنف", font="roboto 14", bg="#FFFFFF", bd=5, command=self.search_pullhistory_table1)
        self.searchbutton2.place(x=130, y=10)

        self.searchvar1 = StringVar()
        self.searchentry1 = Entry(self.pullhistoryw, textvariable=self.searchvar1, font="roboto 14", width=25,
                                 bg="#FFFFFF")
        self.searchentry1.place(x=360, y=20)

        self.pull_history_table()

        self.Get_pullhistory()

        self.pullhistoryw.mainloop()


    def search_pullhistory_table1(self):
        ans = ''
        try:
            self.get_searchentry1 = str(self.searchentry1.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل اسم الصنف بشكل صحيح")
            return
        if self.get_searchentry1 == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم الصنف")
            return
        self.cur.execute(
            'select * from market_items'
            ' where product_name=?', (self.get_searchentry1,))
        result = self.cur.fetchall()
        self.pull_history_table()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans




    def search_market_table(self):
        ans = ''
        try:
            self.get_market_entry = str(self.market_entry.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل اسم الصنف بشكل صحيح")
            return
        if self.get_market_entry == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم الصنف")
            return
        self.cur.execute(
            'select product_name, product_quantity, quantity_price from market_items'
            ' where product_name=?', (self.get_market_entry,))
        result = self.cur.fetchall()
        self.table6()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans


    def Get_to_sales(self, x=0):
        ans = ''
        self.table7()
        self.cur.execute(
            "select * from sales_table;")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def add_to_sales(self):
        #self.cur.execute("drop table market_table")
        self.cur.execute("create table if not exists sales_table"
                         "(sales_date varchar(15) not null,"
                         "product_name varchar(30) not null,"
                         "quantity INTEGER not null,"
                         "quantity_price float not null);")
        try:
            self.get_sold_product = str(self.product_name_market.get())
            self.get_sold_quantity = int(self.quantity_market.get())
            self.get_sold_quantity_price = float(self.price_market.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل بيانات صحيحة")

        if self.get_sold_product == "" or self.get_sold_quantity == "" or self.get_sold_quantity_price=="":
            messagebox.showerror("خطأ", "من فضلك ادخل جميع البيانات")

        if self.get_sold_quantity <= 0:
            messagebox.showerror("خطأ", "من فضلك أدخل الكمية مرة أخرى")
            return

        if self.get_sold_quantity_price <= 0:
            messagebox.showerror("خطأ", "من فضلك أدخل سعر الكمية مرة أخرى")
            return

        self.cur.execute("select product_name from market_items;")
        ex_product = self.cur.fetchall()
        self.ex_product1 = ([tup[0] for tup in ex_product])

        if self.get_sold_product not in self.ex_product1:
            messagebox.showerror("خطأ", "هذا الصنف غير موجود بالماركت")
            return

        if self.get_sold_product in self.ex_product1:

            self.cur.execute("select product_quantity from market_items where  "
                             "product_name=?;",
                             (str(self.get_sold_product),))
            ex_quantity = self.cur.fetchall()
            self.ex_quantity = ([tup[0] for tup in ex_quantity])
            self.ex_quantity = self.ex_quantity[0]





            self.remained_quantity = int(self.ex_quantity - self.get_sold_quantity)

            if self.remained_quantity < 0:
                messagebox.showerror("خطأ", "الكمية المطلوبة غير متوفرة بالماركت")
                return

            if self.remained_quantity == 0:
                messagebox.showerror("تنبيه", "الكمية المتبقية من هذا الصنف في الماركت 0 لا تنسى سحب كمية جديدة ")
            self.cur.execute("update market_items set product_quantity=? where product_name = ?",
                             (self.remained_quantity,
                              str(self.get_sold_product)))

        today = datetime.date(datetime.now())
        self.format_date = str(today.strftime("%d/%m/%Y"))
        self.salling_date = self.format_date
        self.cur.execute('insert into sales_table values(?,?,?,?)', (
            str(self.salling_date),
            str(self.get_sold_product),
            int(self.get_sold_quantity),
            float(self.get_sold_quantity_price)))



        self.Get_to_sales()

        self.insert_market_items()

        self.base.commit()

        self.new_text = ""
        self.product_name_market.delete(0, END)
        self.product_name_market.insert(0, self.new_text)

        self.quantity_market.delete(0, END)
        self.quantity_market.insert(0, self.new_text)

        self.price_market.delete(0, END)
        self.price_market.insert(0, self.new_text)

    def delete_sold_item(self):
        self.delete_sold_item_w = Tk()
        width = 300
        height = 100
        screen_width = self.delete_sold_item_w.winfo_screenwidth()
        screen_height = self.delete_sold_item_w.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.delete_sold_item_w.geometry("%dx%d+%d+%d" % (width, height, x, y))

        self.delete_sold_item_entry = Entry(self.delete_sold_item_w, bg="light grey", font="robot 14")
        self.delete_sold_item_entry.grid(row=2, column=1)
        self.delete_sold_item_label = Label(self.delete_sold_item_w, text="ادخل اسم الصنف", font="roboto 14 bold",
                                              bg="#FFFFFF")
        self.delete_sold_item_label.grid(row=2, column=2)

        self.delete_sold_item_button = Button(self.delete_sold_item_w, text="حذف", font="robot 16 bold", fg="black",
                                                bg="#4267b2",
                                                command=self.final_delete_sold_item)
        self.delete_sold_item_button.grid(row=4, column=1)
        self.delete_sold_item_w.mainloop()

    def final_delete_sold_item(self):
        self.get_delete_sold_item_entry = str(self.delete_sold_item_entry.get())
        self.cur.execute("select quantity from sales_table where product_name = ? ",
                         (str(self.get_delete_sold_item_entry),))
        sold_quantity = self.cur.fetchall()
        self.sold_quantity = ([tup[0] for tup in sold_quantity])
        self.sold_quantity = self.sold_quantity[0]

        self.cur.execute("select product_quantity from market_items where product_name = ? ",
                         (str(self.get_delete_sold_item_entry),))
        old_quantity_store = self.cur.fetchall()
        self.old_quantity_store = ([tup[0] for tup in old_quantity_store])
        self.old_quantity_store = self.old_quantity_store[0]
        self.new_quantity_store = int(abs(self.old_quantity_store + self.sold_quantity))
        self.cur.execute("update market_items set product_quantity=? where product_name = ?",
                         (self.new_quantity_store,
                          str(self.get_delete_sold_item_entry)))


        self.cur.execute("delete from sales_table where product_name = ?;", (self.get_delete_sold_item_entry,))
        self.base.commit()
        self.delete_sold_item_w.destroy()
        self.Get_to_sales()
        self.insert_market_items()


    def sell_button(self):
        if messagebox.askyesno("تنبيه", "هل تريد بيع هذه الاصناف") == True:
            #self.cur.execute('drop table sales_history;')
            self.cur.execute("create table if not exists sales_history"
                             "(sales_date varchar(15) not null,"
                             "product_name varchar(30) not null,"
                             "product_quantity integer not null,"
                             "quantity_price float not null);")

            self.cur.execute("insert into sales_history select * from sales_table;")

            self.cur.execute("delete from sales_table;")
            self.cur.execute("delete from market_items where product_quantity = 0;")
            self.base.commit()
            self.table7()


    def customers_table(self):
        scrollbarx = Scrollbar(self.tableframe10, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe10, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe10, columns=("Date", "Customer", "Debt"),
                                 selectmode="browse", height=17, yscrollcommand=scrollbary.set,
                                 xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=170)
        self.tree.column('#2', stretch=NO, minwidth=0, width=170)

        self.tree.heading('Date', text="التاريخ", anchor=W)
        self.tree.heading('Customer', text="اسم العميل", anchor=W)
        self.tree.heading('Debt', text="المديونية", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)




    def build_customers_table(self):
        self.salesframe2.place_forget()
        self.tableframe4.place_forget()
        self.tableframe5.place_forget()
        self.tableframe6.place_forget()
        self.tableframe7.place_forget()
        self.returnframe.place_forget()
        self.searchframe.place_forget()
        self.tableframe2.place_forget()
        self.tableframe3.place_forget()
        self.salesframe.place_forget()
        self.marketfrme.place_forget()
        self.storesframe.place_forget()
        self.tableframe.place_forget()
        self.formframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe1.place_forget()
        self.itemframe.place_forget()
        self.tableframe8.place_forget()
        self.customers.place(self.customersinfo)
        self.tableframe10.place(self.tableframe10info)

        self.cur.execute("create table if not exists customers"
                         "(date varchar (15),"
                         "name varchar (30),"
                         "debt float);")

        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()

        self.customers_table()
        self.getcustomers()

        self.tree.bind("<<TreeviewSelect>>", self.clickcustomertable)
        self.customers.focus_set()

        self.customer_name = StringVar()
        self.customer_debt = StringVar()
        self.search_entry_customer = StringVar()
        va = 110
        l1 = [':اسم العميل', ':المديونية']
        for i in range(0, 2):
            Label(self.customers, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(x=430, y=va)
            va += 70
        Entry(self.customers, textvariable=self.customer_name, font="roboto 14", bg="#FFFFFF", width=25).place(x=120, y=105, height=40)
        Entry(self.customers, textvariable=self.customer_debt, font="roboto 14", bg="#FFFFFF", width=25).place(
            x=120,
            y=175,
            height=40)

        Button(self.customers, text="اضافة عميل", font="robot 12 bold", bg="light blue", bd=5, width=12, height=2,
               command=self.addcustomer).place(x=85, y=330)
        Button(self.customers, text="تعديل", font="robot 12 bold", bg="light blue", bd=5, width=10, height=2,
               command=self.changecustomer).place(x=240, y=330)
        Button(self.customers, text="ازالة", font="robot 12 bold", bg="light blue", bd=5, width=10, height=2,
               command=self.delcustomer).place(x=385, y=330)
        Entry(self.customers,textvariable=self.search_entry_customer, font="roboto 14", bg="#FFFFFF", width=20).place(x=965, y=30)
        self.date_but = Button(self.customers, text="بحث بالتاريخ", font="robot 14 bold", bg="light blue", bd=5,
                               width=13, command=self.search_customer2).place(x=785, y=20)
        self.name_but = Button(self.customers, text="بحث بالاسم", font="robot 14 bold", bg="light blue", bd=5,
                               width=13, command=self.search_customer1).place(x=600, y=20)



    # FETCH USERS FROM USERS TABLE
    def getcustomers(self, x=0):
        ans = ''
        self.customers_table()
        self.cur.execute("select * from customers")
        userslist = self.cur.fetchall()
        for i in userslist:
            self.tree.insert('', 'end', values=i)
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans

    def changecustomer(self):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']

        self.customer_name.set((self.customer_name.get()))
        self.customer_debt.set((self.customer_debt.get()))


        if self.customer_name.get() == '' or self.customer_debt.get() == '':
            messagebox.showerror("خطأ", "من فضلك ادخل المعلومات كاملة")
            return

        today = datetime.date(datetime.now())
        self.format_date_customer = str(today.strftime("%d/%m/%Y"))
        self.date_customer = self.format_date_customer

        self.cur.execute(
            "update customers set date = ?,debt = ? where name = ?;", (
                self.date_customer, self.customer_debt.get(), self.customer_name.get()))
        self.base.commit()
        self.tree.delete(*self.tree.get_children())
        cur = self.getcustomers(li[1])
        self.customer_name.set("")
        self.customer_debt.set("")
        self.tree.selection_set(cur)

    def delcustomer(self):
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if self.customer_name.get() == '' or self.customer_debt.get() == '':
            messagebox.showerror("خطأ", "من فضلك ادخل المعلومات كاملة")
            return

        if messagebox.askyesno("تنبيه", "هل تريد مسح هذا العميل؟") == True:
            self.cur.execute("delete from customers where name = ?;", (li[1],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getcustomers()
            self.customer_name.set('')
            self.customer_debt.set('')



    def addcustomer(self):
        try:
            self.customer_name.set(str(self.customer_name.get()))
            self.customer_debt.set(float(self.customer_debt.get()))

        except:
            messagebox.showerror("خطأ", "من فضلك ادخل بيانات صحيحة")
            return

        if self.customer_name.get() == '' or self.customer_debt.get() == '':
            messagebox.showerror("خطأ", "من فضلك ادخل جميع البيانات")
            return

        else:
            l = [self.customer_name.get(), self.customer_debt.get()]
            for i in range(0, len(l)):
                if l[i].isdigit():
                    if i == 1:
                        messagebox.showerror("خطأ", "يجب ان تكون المديونية ارقام")
                    return
        self.cur.execute('select * from customers where name = ?', (str(self.customer_name.get()),))
        l = self.cur.fetchall()

        today = datetime.date(datetime.now())
        self.format_date_customer = str(today.strftime("%d/%m/%Y"))
        self.date_customer = self.format_date_customer

        x = str(self.customer_name.get())
        y = float(self.customer_debt.get())
        z = self.date_customer

        self.cur.execute("insert into customers values(?,?,?)", (z, x, y))
        self.customer_name.set('')
        self.customer_debt.set('')

        messagebox.showinfo('تأكيد', 'تم اضافة العميل بنجاح')
        self.getcustomers()
        self.build_customers_table()
        self.base.commit()



    def clickcustomertable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 3):
            self.customer_name.set((li[1]))
            self.customer_debt.set((li[2]))



    def search_customer1(self):
        ans = ''

        try:
            self.get_entry_customer = str(self.search_entry_customer.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل التاريخ بشكل صحيح")
            return

        if self.get_entry_customer == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة اسم العميل")
            return
        self.cur.execute(
            'select * from customers'
            ' where name=?', (self.get_entry_customer,))
        result = self.cur.fetchall()
        self.customers_table()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans


    def search_customer2(self):
        ans = ''
        try:
            self.get_entry_date = str(self.search_entry_customer.get())
        except:
            messagebox.showerror("خطأ", "من فضلك أدخل التاريخ بشكل صحيح")
            return
        if self.get_entry_date == "":
            messagebox.showerror("خطأ", "من فضلك قم بكتابة التاريخ")
            return
        self.cur.execute(
            'select * from customers'
            ' where date=?', (self.get_entry_date,))
        result = self.cur.fetchall()
        self.customers_table()
        x = 0
        for i in result:
            self.tree.insert('', 'end', values=(i))
            if str(x) == i[0]:
                a = self.tree.get_children()
                ans = a[len(a) - 1]

        return ans