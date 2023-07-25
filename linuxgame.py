import random

class Game:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "What command lists the contents of a directory?",
                "answer": "ls"
            },
            {
                "question": "What command changes the current directory?",
                "answer": "cd"
            },
            {
                "question": "What command shows the current working directory?",
                "answer": "pwd"
            },
            {
                "question": "What command creates a new directory?",
                "answer": "mkdir"
            },
            {
                "question": "What command removes a file?",
                "answer": "rm"
            }
        ]

    def ask_question(self):
        question = random.choice(self.questions)
        print(question["question"])
        answer = input("> ")
        if answer == question["answer"]:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")

    def play(self):
        print("Welcome to the Linux Administration Game!")
        while True:
            self.ask_question()
            print(f"Your current score is: {self.score}")
            play_again = input("Do you want to play again? (yes/no) ")
            if play_again.lower() != "yes":
                break

if __name__ == "__main__":
    game = Game()
    game.play()
