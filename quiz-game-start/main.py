from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
for data in question_data:
    question = Question(data["text"], data["answer"])
    questions.append(question)

quiz = QuizBrain(questions)

quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("Your completed the quiz")
print(f"Your totatl score was {quiz.score}/{quiz.question_number}")