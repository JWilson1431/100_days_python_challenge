class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0

    #Method to show and process the next question
    def next_question(self):
        print(f"Q.{self.question_number + 1} {self.questions_list[self.question_number].text} (True/False):")
        self.question_number += 1
        user_answer = input("What is your answer?")
        self.check_answer(user_answer, self.questions_list[self.question_number].answer)

    #Method to check if there are still new questions in the loop
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    #Method to check if the user's answer if correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, your answer was not correct.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
