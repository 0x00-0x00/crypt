from __future__ import unicode_literals
from tkinter import filedialog
from tkinter import *
from functools import*
import tkinter.scrolledtext as sct
#from PIL import Image, ImageTk



#global entrada
#entrada=0

def callback():
    name= filedialog.askdirectory()

def callback2():
    entrada= filedialog.askopenfilename()

def callback3():
    entrada2= filedialog.askdirectory()

def bt_onclick2(entrada):
    entradadados = entrada

def bt_onclick(entrada):
    entradadados=entrada

def options():
    janela2=Tk()
    janela2.title("options")
    janela2.geometry("400x200+600+200")
    lb2=Label(janela2,text="Put text here")
    lb2.place(x=25, y=50)
    btn2=Button(janela2, width=7, text="Close", command=janela2.destroy)
    btn2.place(x=150,y=150)

def help():
    janela2=Tk()
    janela2.title("Help")
    janela2.geometry("400x300+600+200")
    lb2=Label(janela2,text="Put text here")
    lb2.place(x=10, y=30)
    btn2=Button(janela2, width=7, text="Close", command=janela2.destroy)
    btn2.place(x=150,y=250)

def about():
    janela2=Tk()
    janela2.title("About")
    janela2.geometry("400x200+600+200")
    lb2=Label(janela2,text="Put text here")
    lb2.place(x=15, y=50)
    btn2=Button(janela2, width=7, text="Close", command=janela2.destroy)
    btn2.place(x=150,y=150)

janela = Tk()
janela.title ("Cript")

principal=Menu(janela)
arquivo=Menu(principal)
principal.add_command(label="Options", command=options)
principal.add_command(label="Help", command=help)
principal.add_command(label="About", command=about)

janela.configure(menu=principal)

lb = Label (janela, text="Chose the destination:")
lb.place(x=20, y =180)

lb2 = Label (janela, text="Write bellow:")
lb2.place(x=20, y =230)

lb3 = Label (janela, text="Put the text to encryp bellow:")
lb3.place(x=20, y =280)

#Deixei essa label para caso vc queira usar para testes
lbdown = Label (janela, text="Ready to work")
lbdown.place(x=200, y =470)

entrada=Entry(janela, width=50, font="Arial", border=2)
entrada.place(x=20, y=200)

entrada2=Entry(janela, width=62, font="Arial", border=2)
entrada2.place(x=20, y=250)

entrada3=sct.Text(janela, width=90, height=10, border=2)
entrada3.place(x=20, y=300)

bt = Button(janela, width = 20, text="Open folder")
bt["command"]=callback
bt.place(x=510, y =199)

bt2 = Button(janela, width=20, text="Open file")
bt2["command"]=callback2
bt2.place(x=700, y=199)

bt3 = Button (janela, width = 20, text="Open folder")
bt3["command"]=callback3
bt3.place(x=650, y =249)

bt4 = Button (janela, width = 20, height=4, text="Encrypt")
bt4["command"]=partial(bt_onclick,entrada3)
bt4.place(x=670, y =299)

bt5 = Button (janela, width = 20, height=4, text="Decrypt")
bt5["command"]=partial(bt_onclick2,entrada3)
bt5.place(x=670, y =379)



#Tire o comentario da proximas linhas para colocar a foto
#load = Image.open("image.png")
#render = ImageTk.PhotoImage(load)
#img = Label(image=render)
#img.image = render
#img.place(x=70, y=0)

janela.geometry ("920x500+200+200")
janela.mainloop()