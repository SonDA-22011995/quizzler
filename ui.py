from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, window, quiz: QuizBrain):
        self.window = window
        self.quiz = quiz
        self.window.title("Quizzler")

        self.style = ttk.Style()
        self.style.configure("My.TFrame", background=THEME_COLOR)

        self.mainframe = ttk.Frame(
            self.window,
            padding=(20, 20, 20, 20),
            style="My.TFrame",
            width=340
        )

        self.style.configure(
            "My.TLabel",
            background=THEME_COLOR,
            font=("Arial", 10, "bold"),
            foreground="white",
            padding=(0,0,50,50)
        )
        self.score = StringVar()
        self.score.set("Score:0")

        self.score_label = ttk.Label(
            self.mainframe,
            textvariable=self.score,
            style="My.TLabel"
        )

        self.canvas = Canvas(
            self.mainframe,
            height=250,
            width=300,
        )
        self.canvas_text = self.canvas.create_text(
            10, 10,
            text='A wonderful story',
            anchor='nw',
            font=("Arial", 20, "italic"),
            fill='black',
            width=290,
        )

        self.true_image = PhotoImage(file='./images/true.png')
        self.true_btn = Button(
            self.mainframe,
            background=THEME_COLOR,
            highlightthickness=0,
            image=self.true_image,
            command= lambda : self.next_question(answer="true")
        )

        self.false_image = PhotoImage(file='./images/false.png')
        self.false_btn = Button(
            self.mainframe,
            background=THEME_COLOR,
            highlightthickness=0,
            image=self.false_image,
            command=lambda: self.next_question(answer="false")
        )

        # gird design
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.score_label.grid(column=1, row=0, sticky=(E))
        self.canvas.grid(column=0, row=1,columnspan=2, sticky=(N, W, E, S))
        self.true_btn.grid(column=0, row=2, sticky=(N, W, E, S), pady=(50,0))
        self.false_btn.grid(column=1, row=2, sticky=(N, W, E, S), pady=(50,0))

        #
        self.update_canvas_text(self.quiz.next_question())


    def update_canvas_text(self, question):
        self.canvas.itemconfig(
            self.canvas_text,
            text = question
        )

    def update_score(self, score: int):
        self.score.set(f"Score: {score}")

    def next_question(self, answer: str):
        if self.quiz.still_has_questions():
            self.quiz.check_answer(answer)
            self.update_canvas_text(self.quiz.next_question())
            self.update_score(getattr(self.quiz, "score"))
        else:
            self.update_canvas_text(self.quiz.result())
