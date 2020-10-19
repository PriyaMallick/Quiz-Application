import tkinter
from tkinter import *
import random

questions = ["Question 1?", "Question 2?", "Question 3", "Question 4?", "Question 5?", "Question 6?", "Question 7?",
             "Question 8?", "Question 9?", "Question 10?"]

answerChoice = [
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
]

indexes=[]
def generatequestion():
    global indexes
    while(len(indexes)<5):
        x= random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append()

def quiz():
    lquestion = Label(root, text=questions[indexes[0]], font=("Consolas", 16), width=500, justify="center", wraplength=400)
    lquestion.pack()

    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root, text=answerChoice[indexes[0]][0], font=("Times", 12), value=0, variable=radiovar)
    r1.pack()
    r2 = Radiobutton(root, text=answerChoice[indexes[0]][1], font=("Times", 12), value=1, variable=radiovar)
    r2.pack()
    r3 = Radiobutton(root, text=answerChoice[indexes[0]][2], font=("Times", 12), value=2, variable=radiovar)
    r3.pack()
    r4 = Radiobutton(root, text=answerChoice[indexes[0]][3], font=("Times", 12), value=3, variable=radiovar)
    r4.pack()


def startQuiz():
    labeltext.destroy()
    labelimage.destroy()
    linstruction.destroy()
    lrules.destroy()
    btnstart.destroy()
    generatequestion()
    quiz()


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

btnstart = Button(root, text="Start!", font=("verdana", 18), relief='ridge', command=startQuiz)
btnstart.pack()

linstruction = Label(root, text="Read The Instructions And\nClick Start Once You Are Ready", background="#ffffff",
                     font=("Consolas", 14), justify="center")
linstruction.pack(pady=(20, 40))

lrules = Label(root,
               text="1. Quiz contains 10 questions.\n2. You will get 20 seconds to answer each questions\n3. Once you select an option, that will be the final answer.\n Note: Hence think before you select.",
               width=100, font=("Times", 14), background="yellow", foreground="black")
lrules.pack()

root.mainloop()
