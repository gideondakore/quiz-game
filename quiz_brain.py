class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number <= len(self.question_list) - 1

    def next_question(self):
        q_num = self.question_number
        q_text = self.question_list[q_num].text
        current_question = self.question_list[q_num]
        self.question_number += 1
        user_answer = input(f"Q.{q_num+1}: {q_text}. (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")