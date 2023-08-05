THEME_COLOR = "#375362"
from tkinter import *
from  quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.score=0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_lable = Label(text="score:0")
        self.score_lable.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question = self.canvas.create_text(150,125,width=280,text="your question is :",font=("Arail",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2)
        self.trueimg = PhotoImage(file="./images/true.png")
        self.falseimg = PhotoImage(file="./images/false.png")

        self.true = Button(image=self.trueimg ,command=self.true_button_check)
        self.true.grid(column=0,row=2)

        self.false = Button(image=self.falseimg,command=self.false_button_check)
        self.false.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():

            self.canvas.config(bg="white")

            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=question)
        else:
            self.canvas.itemconfig(self.question,text="you've reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")



    def true_button_check(self):
        score = self.quiz.check_answer("true")
        self.feedback(score)
        # if score:
        #      self.score += 1
        #
             # self.score_lable.config(text=f"score:{self.score}")
        #
        # self.get_next_question()
    def false_button_check(self):
        score = self.quiz.check_answer("false")
        self.feedback(score)
        # if score:
        #     self.score+=1
        #
        #     self.score_lable.config(text=f"score:{self.score}")
        # self.get_next_question()
    def feedback(self,is_right):

        if is_right:
            self.canvas.config(bg="green")
            self.score += 1

            self.score_lable.config(text=f"score:{self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question())










