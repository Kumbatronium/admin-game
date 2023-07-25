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
            },
            {
                "question": "What command displays a list of running processes?",
                "answer": "ps"
            },
            {
                "question": "What command displays the memory usage of a process?",
                "answer": "top"
            },
            {
                "question": "What command displays the disk usage of a directory?",
                "answer": "du"
            },
            {
                "question": "What command displays the network usage of a process?",
                "answer": "netstat"
            },
            {
                "question": "What command creates a symbolic link?",
                "answer": "ln"
            },
            {
                "question": "What command displays the contents of a file?",
                "answer": "cat"
            },
            {
               "question": "What command copies a file?",
               "answer": "cp"
            },
            {
               "question": "What command moves a file?",
               "answer": "mv"
            },
            {
               "question": "What command removes a directory?",
               "answer": "rmdir"
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
            play_again = input("Do you want to play again? (y/n) ")
            if play_again.lower() != "y":
                break

if __name__ == "__main__":
    game = Game()
    game.play()
