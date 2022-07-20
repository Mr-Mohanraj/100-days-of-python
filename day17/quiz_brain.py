class QuizBrain:

    def __init__(self, q_list): # for init value to the variables
        self.question_number = 0
        self.score = 0
        self.question_list = q_list # get from the main.py 

    def still_has_questions(self): # return true or false, base on the condition from the main file
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]# for get value in the list based on the question number
        print("current Question", current_question.answer)
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
