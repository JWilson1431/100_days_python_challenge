from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#Create a list of question objects using the question data
question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

#Create quizbrain object called quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score was : {quiz.score}/{len(quiz.questions_list)}")