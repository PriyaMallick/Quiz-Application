import tkinter
from tkinter import *

def startQuiz():
    labeltext.destroy()
    labelimage.destroy()
    linstruction.destroy()
    lrules.destroy()
    btnstart.destroy()

root = tkinter.Tk()
root.title("Quizzie")
root.geometry("600x500")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="quiz.png")
labelimage = Label(root, image=img1, background="#ffffff")
labelimage.pack(side=TOP)

labeltext = Label(root, text="Quizzie", font=("Comis sans MS", 24, "bold"), background="#ffffff")
labeltext.pack()

btnstart = Button(root, text="Start!", font=("verdana", 18), relief='ridge',command=startQuiz)
btnstart.pack()

linstruction = Label(root, text="Read The Instructions And\nClick Start Once You Are Ready", background="#ffffff",
                     font=("Consolas", 14), justify="center")
linstruction.pack(pady=(20, 40))

lrules = Label(root,
               text="1. Quiz contains 10 questions.\n2. You will get 20 seconds to answer each questions\n3. Once you select an option, that will be the final answer.\n Note: Hence think before you select.",
               width=100, font=("Times", 14), background="yellow", foreground="black")
lrules.pack()

root.mainloop()
