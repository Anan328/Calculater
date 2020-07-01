from tkinter import *
from math import *
try:
    win = Tk()
    win.title("Calci-Created BY ANAN")
    win.configure(background="cyan")
    win.geometry(("300x240"))
    exp = ""
    update = StringVar()
    def press(n):
        global exp
        exp += str(n)
        update.set(exp)
    def clear():
        global exp
        exp = ""
        update.set(exp)
    def equal():
        try:
            global exp
            r=str(eval(exp))
            update.set(r)
            exp = ""
        except Exception:
            update.set("ERROR ")
    def percent():
        try:
            global exp
            y=factorial(int(exp))
            update.set(y)
            exp = ""
        except Exception:
            update.set("ERROR ")
    def root():
        try:
            global exp
            y=sqrt(float(exp))
            update.set(y)
            exp = ""
        except Exception:
            update.set("ERROR ")
    entry = Entry(win,textvariable=update,width=45)
    entry.grid(row=0,column=0,columnspan=5,ipadx=5,ipady=15)
    button7 = Button(win,text="7",height=1,width=7,command=lambda :press(7),)
    button7.grid(row=2,column=0,ipadx=5,pady=5)
    button8 = Button(win,text="8",height=1,width=7,command=lambda :press(8))
    button8.grid(row=2,column=1,ipadx=5)
    button9 = Button(win,text="9",height=1,width=7,command=lambda :press(9))
    button9.grid(row=2,column=2,ipadx=5)
    button4 = Button(win,text="4",height=1,width=7,command=lambda :press(4))
    button4.grid(row=3,column=0,ipadx=5,pady=5)
    button5 = Button(win,text="5",height=1,width=7,command=lambda :press(5))
    button5.grid(row=3,column=1,ipadx=5)
    button6 = Button(win,text="6",height=1,width=7,command=lambda :press(6))
    button6.grid(row=3,column=2,ipadx=5)
    button1 = Button(win,text="1",height=1,width=7,command=lambda :press(1))
    button1.grid(row=4,column=0,ipadx=5,pady=5)
    button2 = Button(win,text="2",height=1,width=7,command=lambda :press(2))
    button2.grid(row=4,column=1,ipadx=5)
    button3 = Button(win,text="3",height=1,width=7,command=lambda :press(3))
    button3.grid(row=4,column=2,ipadx=5)
    button0 = Button(win,text="0",height=1,width=7,command=lambda :press(0))
    button0.grid(row=5,column=0,ipadx=5)
    buttonc=Button(win,text="C",height=1,width=7,command=clear)
    buttonc.grid(row=1,column=0,ipadx=5)
    buttonp=Button(win,text="+",height=1,width=7,command=lambda:press("+"))
    buttonp.grid(row=4,column=3,ipadx=5)
    buttons=Button(win,text="-",height=1,width=7,command=lambda:press("-"))
    buttons.grid(row=3,column=3,ipadx=5)
    buttonm=Button(win,text="*",height=1,width=7,command=lambda:press("*"))
    buttonm.grid(row=2,column=3,ipadx=5)
    buttond=Button(win,text=".",height=1,width=7,command=lambda:press("."))
    buttond.grid(row=5,column=1,ipadx=5)
    buttonequal=Button(win,text="=",height=1,width=7,command=equal)
    buttonequal.grid(row=5,column=2,ipadx=40,columnspan=2)
    buttondiv=Button(win,text="/",height=1,width=7,command=lambda:press("/"))
    buttondiv.grid(row=1,column=3,ipadx=5)
    buttonf=Button(win,text="!",height=1,width=7,command=lambda:percent())
    buttonf.grid(row=1, column=2, ipadx=5,pady=5)
    buttonr = Button(win, text="√", height=1, width=7, command=lambda:root())
    buttonr.grid(row=1, column=1, ipadx=5)
    win.mainloop()
except Exception:
    update.set("something went wrong")
