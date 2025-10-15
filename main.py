from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface
from tkinter import *

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

window = Tk()
quizz_interface = QuizzInterface(window, quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
#     quizz_interface.update_canvas_text(getattr(quiz,"current_question"))
#     quizz_interface.update_score(getattr(quiz, "score"))
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")


window.mainloop()