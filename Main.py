from tkinter import Tk, Frame, Label, Button
from rmxvi import wishme , cycle
from tkinter.ttk import *
from tkinter import * 
from PIL import ImageTk, Image


class Main(Tk):

    def __init__(self, screenName=None, baseName=None, useTk=1, sync=0, use=None):

        super().__init__(screenName=screenName, baseName=baseName, useTk=useTk, sync=sync, use=use)

        self.title("RMX")
        self.geometry("400x680")

        C = Frame(self)
        self.img01 = Image.open("static\\bg01.png").resize((400, 680))
        self.img02 = Image.open("static\\speakerimg.png").resize((50, 50))
        self.img04 = Image.open("static\\microphone.png").resize((50, 50))
        self.img07 = Image.open("static\\logo.png").resize((350, 100))
        
        self.img03 = ImageTk.PhotoImage(self.img02)
        self.img05 = ImageTk.PhotoImage(self.img04)
        self.img08 = ImageTk.PhotoImage(self.img07)


        p1 = PhotoImage(file = 'static\\button1.png')
        self.iconphoto(False, p1)

        self.leaf = ImageTk.PhotoImage(self.img01)
        background_label = Label(self, image=self.leaf)
        background_label.place(x=0,y=0)
        C.pack()

        self.f2 = Frame(master=self)
        self.Labellogo=Label(self.f2,image=self.img08,bg='black')
        self.Labellogo.pack()
        self.f2.pack(pady=(0,450))


        self.f1 = Frame(master=self,bg='black')
        
        self.txt1 = Button(master=self.f1, command=wishme,image=self.img03,compound="right",bg='black')
        self.txt1.pack(side = LEFT)



        photo = PhotoImage(file = r"static\\microphone.png")

        self.txt2 = Button(master=self.f1, image=self.img05, command=cycle,bg='black')
        self.txt2.pack()
        self.f1.pack()


if __name__ == "__main__":
    app = Main()
    app.mainloop()