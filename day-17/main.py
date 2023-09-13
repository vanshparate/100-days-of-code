# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Vansh")
# user_2 = User("002", "Ayush")
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_que = Question(question_text, question_ans)
    question_bank.append(new_que)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")