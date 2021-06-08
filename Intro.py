"""
    INVENTORY MANAGEMENT SYSTEM
    Developed By-> Ibrahim Saad / Ahmed Samir / Yossef Ibrahim
    Started On ->
"""
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


class splash:
    def __init__(self):
        self.splashminw = Tk()
        self.splashminw.title("أبو حمزة ماركت")
        width = 1000
        height = 700
        self.splashminw.config(bg="#4267b2")
        screen_width = self.splashminw.winfo_screenwidth()
        screen_height = self.splashminw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.splashminw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.splashminw.resizable(0, 0)
        path = "images/items.png"
        img = ImageTk.PhotoImage(Image.open(path))
        main = LabelFrame(self.splashminw, width=890, height=560, bg="gray", relief="sunken")
        main.place(x=55, y=70)
        photoframe = LabelFrame(main, width=480, height=444, bg="snow", relief="raised")
        pic = Label(photoframe, image=img)
        pic.place(x=5, y=5)
        photoframe.place(x=8, y=100)
        Label(main, text="أبو حمزة هايبر ماركت", font="roboto 32 bold underline", bg="#4267b2", anchor="center").place(
            x=250, y=10)
        Label(main, text="System Created By:", font="roboto 25 bold underline", bg="gray", fg="#4267b2").place(x=500, y=160)
        Label(main, text="Eng. Ibrahim Saad /  01276256028", font="roboto 16 bold", bg="gray", fg="#4267b2").place(x=500, y=240)
        Label(main, text="abrahimsaad271@gmail.com", font="roboto 16 bold", bg="gray", fg="#4267b2").place(x=500, y=290)
        Label(main, text="Eng. Ahmed Samir /  01140427159", font="roboto 16 bold", bg="gray", fg="#4267b2").place(x=500, y=340)
        Label(main, text="ahmedsamir18824@gmail.com", font="roboto 16 bold", bg="gray", fg="#4267b2").place(x=500, y=390)

        pic.bind('<Motion>', lambda event: self.splashminw.destroy())
        # self.splashminw.after(10000,lambda :self.splashminw.destroy())
        self.splashminw.mainloop()
