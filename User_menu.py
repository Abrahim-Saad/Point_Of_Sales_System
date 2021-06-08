"""
    INVENTORY MANAGEMENT SYSTEM
    Developed By->PJ28105
    Started On ->08/11/18
"""

import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Addtional_features import mycombobox, myentry
from Admin_menu import Admin
import datetime
import os

# USER MENU

class User:
    def __init__(self, mainw):
         self.mainw=mainw

    def user_mainmenu(self, a, b):
        self.mainframe = LabelFrame(self.mainw, width=800, height=140, bg="#f7f7f7")
        self.mainframe.place(x=330, y=120)
        mi = PhotoImage(file="images/items.png")
        mi = mi.subsample(a, b)
        self.aitems = Button(self.mainframe, text="وارد", bd=5, font="roboto 11 bold",bg="cyan", image=mi, compound=TOP,
                             command=self.builditemtable)
        self.aitems.image = mi
        self.aitems.place(x=260, y=17)
        mi = PhotoImage(file="images/invoice2.png")
        mi = mi.subsample(a,b)
        self.aitems = Button(self.mainframe, text="بيع", bd=5,bg="cyan",font="roboto 11 bold", image=mi, compound=TOP,command=self.make_invoice)
        self.aitems.image = mi
        self.aitems.place(x=62, y=17)
        mi = PhotoImage(file="images/change1.png")
        mi = mi.subsample(a, b)
        self.changeuser = Button(self.mainframe, text="تبديل الحساب",bd=5,bg="cyan",font="roboto 11 bold", image=mi, compound=TOP)
        self.changeuser.image = mi
        self.changeuser.place(x=460, y=17)
        mi = PhotoImage(file="images/Door_Out-512.png")
        mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="خروج",bd=5,bg="cyan",font="roboto 11 bold", image=mi, compound=TOP)
        self.logout.image = mi
        self.logout.place(x=670, y=17)
        self.itemframe = Frame(self.mainw, bg="#FFFFFF", width=1000, height=400)
        self.itemframe.place(x=340, y=340, anchor=NW)
        self.itemframeinfo = self.itemframe.place_info()
        self.tableframe1 =Frame(self.mainw, width=150, height=400,bg="#FFFFFF")
        self.tableframe1.place(x=1230, y=270, anchor=NE)
        self.tableframe1info=self.tableframe1.place_info()
        self.tableframe =Frame(self.mainw, width=350, height=700,bg="#FFFFFF")
        self.tableframe.place(x=1110, y=300, anchor=NE)
        self.tableframeinfo = self.tableframe.place_info()
        self.entryframe = Frame(self.mainw, width=800, height=350, bg="#FFFFFF")
        self.entryframe.place(x=810, y=460+20)
        self.entryframeinfo = self.entryframe.place_info()
        self.entryframe1 = Frame(self.mainw, width=500, height=350, bg="#FFFFFF")
        self.entryframe1.place(x=230, y=470+20)
        self.entryframe1info=self.entryframe1.place_info()


    def builditemtable(self):
        self.merchant = StringVar()
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.itemframe.place(self.itemframeinfo)
        self.cur.execute("select merchant_name from merchants")
        names = self.cur.fetchall()
        merchant_list = [names]
        self.itemframe.place(self.itemframeinfo)
        Label(self.itemframe, text="اختر اسم التاجر", font="robot 20 bold", fg="#4267b2", bg="white").grid(row=0,
                                                                                                           column=3)
        profiles = mycombobox(self.itemframe, font="robot 14", textvariable=self.merchant)
        profiles.grid(row=1, column=3)
        for name in merchant_list:
            profiles.set_completion_list(name)

        # enteries
        self.recite_date = Entry(self.itemframe, bg="light gray")
        self.recite_date.grid(row=2, column=4)
        self.recite_id = Entry(self.itemframe, bg="light gray")
        self.recite_id.grid(row=3, column=4)
        self.supervisor = Entry(self.itemframe, bg="light gray")
        self.supervisor.grid(row=4, column=4)
        self.product_name = Entry(self.itemframe, bg="light gray")
        self.product_name.grid(row=5, column=4)
        self.product_id = Entry(self.itemframe, bg="light gray")
        self.product_id.grid(row=6, column=4)
        self.quantity = Entry(self.itemframe, bg="light gray")
        self.quantity.grid(row=7, column=4)
        self.storeroom = Entry(self.itemframe, bg="light gray")
        self.storeroom.grid(row=8, column=4)
        self.piece_price = Entry(self.itemframe, bg="light gray")
        self.piece_price.grid(row=9, column=4)
        self.unit_price = Entry(self.itemframe, bg="light gray")
        self.unit_price.grid(row=2, column=1)
        self.total_price = Entry(self.itemframe, bg="light gray")
        self.total_price.grid(row=3, column=1)
        self.discount = Entry(self.itemframe, bg="light gray")
        self.discount.grid(row=4, column=1)
        self.bonus = Entry(self.itemframe, bg="light gray")
        self.bonus.grid(row=5, column=1)
        self.unit_sale_price = Entry(self.itemframe, bg="light gray")
        self.unit_sale_price.grid(row=6, column=1)
        self.sector_sale_price = Entry(self.itemframe, bg="light gray")
        self.sector_sale_price.grid(row=7, column=1)
        self.recite_total_price = Entry(self.itemframe, bg="light gray")
        self.recite_total_price.grid(row=8, column=1)
        self.payed = Entry(self.itemframe, bg="light gray")
        self.payed.grid(row=9, column=1)
        self.entered_date = Entry(self.itemframe, bg="light gray")
        self.entered_date.grid(row=10, column=1)

        self.recite_date_label = Label(self.itemframe, text=":تاريخ الفاتورة   ", font="roboto 14 bold", bg="#FFFFFF")
        self.recite_date_label.grid(row=2, column=5)
        self.recite_id_label = Label(self.itemframe, text=":رقم الفاتورة     ", font="roboto 14 bold", bg="#FFFFFF")
        self.recite_id_label.grid(row=3, column=5)
        self.supervisor_label = Label(self.itemframe, text=":اسم المستلم     ", font="roboto 14 bold", bg="#FFFFFF")
        self.supervisor_label.grid(row=4, column=5)
        self.product_name_label = Label(self.itemframe, text=":اسم الصنف     ", font="roboto 14 bold", bg="#FFFFFF")
        self.product_name_label.grid(row=5, column=5)
        self.product_id_label = Label(self.itemframe, text=":رقم الصنف     ", font="roboto 14 bold", bg="#FFFFFF")
        self.product_id_label.grid(row=6, column=5)
        self.quantity_label = Label(self.itemframe, text=":الكمية           ", font="roboto 14 bold", bg="#FFFFFF")
        self.quantity_label.grid(row=7, column=5)
        self.storeroom_label = Label(self.itemframe, text=":رقم المخزن    ", font="roboto 14 bold", bg="#FFFFFF")
        self.storeroom_label.grid(row=8, column=5)
        self.piece_price_label = Label(self.itemframe, text=":سعر القطعة    ", font="roboto 14 bold", bg="#FFFFFF")
        self.piece_price_label.grid(row=9, column=5)
        self.unit_price_label = Label(self.itemframe, text=":سعر الوحدة           ", font="roboto 14 bold",
                                      bg="#FFFFFF")
        self.unit_price_label.grid(row=2, column=2)
        self.total_price_label = Label(self.itemframe, text=":سعر الكمية           ", font="roboto 14 bold",
                                       bg="#FFFFFF")
        self.total_price_label.grid(row=3, column=2)
        self.discount_label = Label(self.itemframe, text=":الخصم                 ", font="roboto 14 bold", bg="#FFFFFF")
        self.discount_label.grid(row=4, column=2)
        self.bonus_label = Label(self.itemframe, text=":بونص                 ", font="roboto 14 bold", bg="#FFFFFF")
        self.bonus_label.grid(row=5, column=2)
        self.unit_sale_price_label = Label(self.itemframe, text=":سعر الوحدة جملة    ", font="roboto 14 bold",
                                           bg="#FFFFFF")
        self.unit_sale_price_label.grid(row=6, column=2)
        self.sector_sale_price_label = Label(self.itemframe, text=":سعر الوحدة قطاعي  ", font="roboto 14 bold",
                                             bg="#FFFFFF")
        self.sector_sale_price_label.grid(row=7, column=2)
        self.recite_total_price_label = Label(self.itemframe, text=":اجمالي الفاتورة      ", font="roboto 14 bold",
                                              bg="#FFFFFF")
        self.recite_total_price_label.grid(row=8, column=2)
        self.payed_label = Label(self.itemframe, text=":مدفوع                  ", font="roboto 14 bold", bg="#FFFFFF")
        self.payed_label.grid(row=9, column=2)
        self.entered_date_label = Label(self.itemframe, text=":تاريخ ادخال الفاتورة", font="roboto 14 bold",
                                        bg="#FFFFFF")
        self.entered_date_label.grid(row=10, column=2)

    def getproducts(self):
         self.cur.execute("select * from products")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
    def make_invoice(self):
        self.tableframe.place_forget()
        self.entryframe.place(self.entryframeinfo)
        self.entryframe1.place(self.entryframe1info)
        self.tableframe1.place(self.tableframe1info)
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Transaction ID", "Product ID", "Product Name",
        'Quantity', 'Price','Date','Time'), selectmode="browse", height=6,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=170)
        self.tree.column('#4', stretch=NO, minwidth=0, width=130)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        self.tree.heading('Transaction ID', text="Transaction ID", anchor=W)
        self.tree.heading('Product ID', text="Product ID", anchor=W)
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Price', text="Price", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.tree.bind("<<TreeviewSelect>>", self.clicktranstable)
        self.user_input()

    def user_input(self):
       self.cur.execute('select max(trans_id) from sales')
       li = self.cur.fetchall()
       if(li[0][0]!=None):
        self.transid = li[0][0] + 1
       else:
           self.transid = 100
       self.qty = StringVar(value=1)
       self.additem=StringVar()
       self.total=IntVar(value=0)
       Button(self.entryframe,text="Proceed",command=self.transtableadd,bd=10,width=8,height=7,bg="#FFFFFF",font="roboto 10").place(x=0,y=30)
       Button(self.entryframe, text="Add to cart", command=self.addtotrans, bd=10, width=10, height=3,bg="#FFFFFF",font="roboto 10").place(x=100,y=80)
       Button(self.entryframe, text="Remove", command=self.removecart, bd=10, width=10, height=3, bg="#FFFFFF",font="roboto 10").place(x=210, y=80)
       entercart=mycombobox(self.entryframe,width=20,textvariable=self.additem,font="roboto 12")
       entercart.place(x=100,y=30,height=30)
       cartqty = Entry(self.entryframe,textvariable=self.qty,width=9,bg="#ffffff",font="roboto 12")
       cartqty.place(x=320,y=30,height=30)
       carttotal = Entry(self.entryframe, textvariable=self.total, width=20, state='readonly', bg="#ffffff", font="roboto 12")
       carttotal.place(x=130, y=185, height=60)
       Label(self.entryframe, text="Quantity", font="roboto 12 bold", bg="#ffffff").place(x=318,y=0)
       Label(self.entryframe, text="Search", font="roboto 12 bold", bg="#ffffff").place(x=100, y=0)
       Label(self.entryframe, text="Amount Due", font="roboto 14 bold", bg="#ffffff").place(x=0, y=205)
       self.cur.execute("select max(invoice) from sales")
       self.invoice = self.cur.fetchall()
       self.invoice = self.invoice[0][0] + 1
       Label(self.tableframe1, text="Invoice No. "+str(self.invoice), font="roboto 14 bold", bg="#ffffff").grid(row=0, column=0)
       self.cur.execute("select product_desc,product_price from products")
       li=self.cur.fetchall()
       self.inventory = []
       self.desc_price=dict()
       for i in range(0, len(li)):
           if (self.inventory.count(li[i][0]) == 0):
               self.inventory.append(li[i][0])
           self.desc_price[li[i][0]]=li[i][1]
       entercart.set_completion_list(self.inventory)
       li=['Product Id','Product Name','Price','Left Stock']
       va=0
       for i in range(0,4):
           Label(self.entryframe1, text=li[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=va)
           va += 65
       self.cartitemid = StringVar()
       self.cartitem = StringVar()
       self.cartitemprice = StringVar()
       self.cartitemstock = StringVar()
       Entry(self.entryframe1, textvariable=self.cartitemid, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=0,height = 40)
       Entry(self.entryframe1, textvariable=self.cartitem, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=65,height=40)
       Entry(self.entryframe1, textvariable=self.cartitemprice, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*2,height=40)
       Entry(self.entryframe1, textvariable=self.cartitemstock, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*3,height=40)
       self.id_qty=dict()
       self.cur.execute("select product_id from products")
       l=self.cur.fetchall()
       for i in range(0,len(l)):
           self.id_qty[l[i][0]]=0

    def addtotrans(self):
        if(len(self.additem.get()) == 0 or self.inventory.count(self.additem.get())==0):
            messagebox.showerror("Error", "Product Not Found!")
            return
        else:
            if(not self.qty.get().isdigit()):
                messagebox.showerror('Error','Invalid quantity!')
                return
            if(int(self.qty.get()) <= 0):
                messagebox.showerror('Error', 'Invalid quantity!')
                return
            self.cur.execute("select product_id,product_desc from products where product_desc = ? ",(self.additem.get(),))
            row = self.cur.fetchall()
            row = [list(row[0])]
            row[0].insert(0,self.transid)
            self.transid+=1
            row[0].append(int(self.qty.get()))
            row[0].append((int(self.qty.get())*self.desc_price[self.additem.get()]))
            x=str(datetime.datetime.now().strftime("%d-%m-%y"))
            row[0].append(x)
            x=datetime.datetime.now()
            x=str(x.hour)+' : '+str(x.minute)+' : '+str(x.second)
            row[0].append(x)
            row = [tuple(row[0])]
            self.cartitemid.set(row[0][1])
            self.cartitemprice.set(self.desc_price[self.additem.get()])
            self.cartitem.set(row[0][2])
            self.cur.execute("select stocks from products where product_id=?", (row[0][1],))
            li = self.cur.fetchall()
            if((li[0][0]-self.id_qty[row[0][1]])-int(self.qty.get())<0):
                if(li[0][0]!=0):
                    messagebox.showerror('Error','Product with this quantity not available!')
                else:
                    messagebox.showerror('Error', 'Product out of stock!')
                return
            self.id_qty[row[0][1]] += int(self.qty.get())
            self.cartitemstock.set(li[0][0]-self.id_qty[row[0][1]])
            for data in row:
                self.tree.insert('', 'end', values=(data))
            self.total.set(self.total.get() + (int(self.qty.get()) * self.desc_price[self.additem.get()]))
            self.qty.set('1')
            self.additem.set('')

    def transtableadd(self):
        x=self.tree.get_children()
        if(len(x) == 0):
            messagebox.showerror('Error','Empty cart!')
            return
        if (messagebox.askyesno('Alert!','Do you want to proceed?') == False):
            return
        a=[]
        self.cur.execute("select max(invoice) from sales")
        self.invoice=self.cur.fetchall()
        self.invoice=self.invoice[0][0]+1
        for i in x:
            l=self.tree.item(i)
            a.append(l['values'])
        for i in a:
            s = (str(i[5])).split('-')
            i[5] = s[2] + "-" + s[1] + "-" + s[0]
            self.cur.execute("insert into sales values (?,?,?,?,?,?)",(int(i[0]),int(self.invoice),int(i[1]),int(i[3]),i[5],i[6]))
            self.cur.execute("select stocks from products where product_id=?",(int(i[1]),))
            l=self.cur.fetchall()
            self.cur.execute("update products set stocks=? where product_id=?",(l[0][0]-self.id_qty[str(i[1])],int(i[1])))
            self.base.commit()
        messagebox.showinfo('Success','Transaction Successful!')
        self.makeprint()
        self.tree.delete(*self.tree.get_children())
        self.cartitemstock.set('')
        self.cartitem.set('')
        self.cartitemid.set('')
        self.cartitemprice.set('')
        self.total.set(0)
        self.additem.set('')
        self.qty.set('1')
        self.cur.execute("select product_id from products")
        l = self.cur.fetchall()
        for i in range(0, len(l)):
            self.id_qty[l[i][0]] = 0
        self.make_invoice()

    def removecart(self):
        re = self.tree.selection()
        if(len(re)==0):
            messagebox.showerror('Error','No cart selected')
            return
        if (messagebox.askyesno('Alert!','Remove cart?') == True):
            x = self.tree.get_children()
            re=re[0]
            l=[]
            fi=[]
            for i in x:
                if(i!=re):
                    l.append(tuple((self.tree.item(i))['values']))
                else:
                    fi=((self.tree.item(i))['values'])
            self.tree.delete(*self.tree.get_children())
            for i in l:
                self.tree.insert('', 'end', values=(i))
            self.cartitemstock.set('')
            self.cartitem.set('')
            self.cartitemid.set('')
            self.cartitemprice.set('')
            self.additem.set('')
            self.qty.set('1')
            self.id_qty[str(fi[1])]-=fi[3]
            self.total.set(self.total.get()-fi[4])
            return

    def makeprint(self):
       if messagebox.askyesno("Alert!","Print this transaction?")== True:
          pass
       ''''
           x = datetime.datetime.now()
           x = str(x.hour) + ' - ' + str(x.minute) + ' - ' + str(x.second)
           dir="E:\GUI\docs\ "
           if not os.path.exists(dir):
               os.makedirs(dir)
           shop="\t\t\t\t\t  The Bake Shop\n"
           address="\t\t\t\t Dwarka Sec-12, New Delhi\n"
           phone="\t\t\t\t     Phone-:1122334455\n"
           sample="\t\t\t\t\t   Invoice No.-:"+str(self.invoice)+"\n"
           dt="\t\t\t\t      "+x
           head="\n\n\t\t------------------------------------------------------\n"
           row="\t     Sno.\t\tProduct Name\t\tQuantity\tTotal\n"
           final=shop+address+phone+sample+dt+head+row
           file_name=str(dir)+str(x)+".rtf"
           f=open(file_name,"x")
           f.write(final)
           x=self.tree.get_children()
           for i in range(0,len(x)):
               f.write("\t     "+str(i+1)+"\t\t")
               for j in range(2,len(self.tree.item(x[i])['values'])-2):
                   f.write(str(self.tree.item(x[i])['values'][j])+"\t\t")
               f.write("\n")
           f.close()
       '''
    def clicktranstable(self,event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 7):
            self.cartitemid.set((li[1]))
            self.cartitem.set((li[2]))
            self.cur.execute("select product_price,stocks from products where product_id=?",(li[1],))
            li = self.cur.fetchall()
            self.cartitemprice.set(li[0][0])
            self.cartitemstock.set(li[0][1]-self.id_qty[self.cartitemid.get()])
