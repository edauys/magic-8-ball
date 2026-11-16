"""Interactive command-line Magic 8-Ball, adapted from a Codecademy exercise."""

import random

ANSWERS = (
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
)


def get_answer():
    """Return one randomly selected fortune."""
    return random.choice(ANSWERS)


def main():
    print("Welcome to the Magic 8-Ball!")
    name = input("Your name (optional): ").strip()

    while True:
        question = input("Ask a yes-or-no question (or type 'quit'): ").strip()
        if question.lower() == "quit":
            print("Thanks for playing!")
            break
        if not question:
            print("Please enter a question before asking the Magic 8-Ball.\n")
            continue
        print(f"{name} asks: {question}" if name else f"Question: {question}")
        print(f"Magic 8-Ball's answer: {get_answer()}\n")


if __name__ == "__main__":
    main()
