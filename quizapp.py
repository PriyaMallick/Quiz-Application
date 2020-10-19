import tkinter
from tkinter import *
import random

questions = ["Who was the first Indian woman in Space?",
             "Who was the first Indian in space?",
             "Who was the first Man to Climb Mount Everest Without Oxygen?",
             "Who built the Jama Masjid?",
             "Who wrote the Indian National Anthem?",
             "Who was the first Indian Scientist to win a Nobel Prize?",
             "Who is the first Indian to win a Nobel Prize?",
             "Who was the first Indian woman to win the Miss World Title?",
             "Who was the first President of India?",
             "Who was the first Indian to win the Booker Prize?"
             ]

answerChoice = [
    ["Kalpana Chawla", "Sunita Williams", "Koneru Humpy", "None of the above"],
    ["Vikram Ambalal", "Ravish", "Rakesh Sharma", "Nagapathi Bhat"],
    ["Junko Tabei", "Reinhold Messner", "Peter Habeler", "Phu Dorji"],
    ["Jahangir", "Akbar", "Imam Bukhari", "Shah Jahan"],
    ["Bakim Chandra Chatterji", "Rabindranath Tagore", "Swami Vivekanand", "None of the above"],
    ["CV Raman", "Amartya Sen", "Hargobind Khorana", "Subramanian Chrandrashekar"],
    ["Rabindranath Tagore", "CV Raman", "Mother Theresa", "Hargobind Khorana"],
    ["Aishwarya Rai", "Sushmita Sen", "Reita Faria", "Diya Mirza"],
    ["Abdul Kalam", "Lal Bahadur Shastri", "Dr. Rajendra Prasad", "Zakir Hussain"],
    ["Dhan Gopal Mukerji", "Nirad C. Chaudhuri", "Arundhati Roy", "Aravind Adiga"],
]

answers = [0, 2, 3, 3, 1, 0, 0, 2, 2, 2]
user_answer=[]

indexes = []


def generatequestion():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    limage=Label(root,background="#ffffff",border=0)
    limage.pack()
    limageresulttext=Label(root,font=("Consolas",20))
    limageresulttext.pack(pady=(50,30))
    if score>=20:
        img=PhotoImage(file="excellent.png")
        limage.config(image=img)
        limage.image=img
        limageresulttext.config(text="Superb!!!",background="#ffffff")
    elif(score>=10 and score<20):
        img = PhotoImage(file="okay.png")
        limage.config(image=img)
        limage.image = img
        limageresulttext.config(text="Good Job!!!", background="#ffffff")
    else:
        img = PhotoImage(file="thumbsdown.png")
        limage.config(image=img)
        limage.image = img
        limageresulttext.config(text="Better luck next time!!!", background="#ffffff")

def calc():
    global indexes, user_answer, answerChoice
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer
    global lquestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lquestion.config(text=questions[indexes[ques]])
        r1['text'] = answerChoice[indexes[ques]][0]
        r2['text'] = answerChoice[indexes[ques]][1]
        r3['text'] = answerChoice[indexes[ques]][2]
        r4['text'] = answerChoice[indexes[ques]][3]
        ques += 1
    else:
        calc()


def quiz():
    global lquestion, r1, r2, r3, r4
    lquestion = Label(root, text=questions[indexes[0]], font=("Consolas", 16), width=500, justify="center",
                      wraplength=400, background="#ffffff")
    lquestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root, text=answerChoice[indexes[0]][0], font=("Times", 12), value=0, variable=radiovar,
                     command=selected, background="#ffffff")
    r1.pack(pady=5)
    r2 = Radiobutton(root, text=answerChoice[indexes[0]][1], font=("Times", 12), value=1, variable=radiovar,
                     command=selected, background="#ffffff")
    r2.pack(pady=5)
    r3 = Radiobutton(root, text=answerChoice[indexes[0]][2], font=("Times", 12), value=2, variable=radiovar,
                     command=selected, background="#ffffff")
    r3.pack(pady=5)
    r4 = Radiobutton(root, text=answerChoice[indexes[0]][3], font=("Times", 12), value=3, variable=radiovar,
                     command=selected, background="#ffffff")
    r4.pack(pady=5)


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
linstruction.pack(pady=(20, 25))

lrules = Label(root,
               text="1. Quiz contains 5 questions.\n2. Once you select an option, that will be the final answer.\n3. There are 4 options for each question.\n4. There is only 1 correct option.\n Note: Hence think before you select.",
               width=100, font=("Times", 14), background="yellow", foreground="black")
lrules.pack()

root.mainloop()
