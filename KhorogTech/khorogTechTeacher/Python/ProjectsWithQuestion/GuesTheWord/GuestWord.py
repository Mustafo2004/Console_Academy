import random

def get_word():
    # List of words with their corresponding question and hints
    words = [
        {
            "question": "Which programming language is called JS?",
            "answer": "javascript",
            "hintFirst": "The file extension is .js",
            "hintSecond": "It was invented in 1995"
        },
        {
            "question": "Which programming language is known for its snake logo?",
            "answer": "python",
            "hintFirst": "It's named after a British comedy group.",
            "hintSecond": "It's widely used in data science."
        },
        {
            "question": "What is the classic word-guessing game often played on paper?",
            "answer": "hangman",
            "hintFirst": "It's associated with drawing parts of a stick figure.",
            "hintSecond": "The word you guess is often related to a theme."
        }
    ]
    return random.choice(words)

def guess_the_word():
    word_data = get_word()
    answer = word_data["answer"].lower()
    attempts = 3  # Number of attempts to guess the word
    hint_index = 0  # Index to track which hint to give

    print("Welcome to 'Guess the Word'!")
    print(word_data["question"])

    while attempts > 0:
        guess = input("Guess the word: ").lower()

        if guess == answer:
            print(f"Congratulations! You've guessed the word: {answer.capitalize()}")
            break
        else:
            print("Incorrect guess.")
            attempts -= 1

            if attempts > 0:
                if hint_index == 0:
                    print(f"Hint 1: {word_data['hintFirst']}")
                    hint_index += 1
                elif hint_index == 1:
                    print(f"Hint 2: {word_data['hintSecond']}")

    else:
        print(f"Sorry, you're out of attempts. The word was: {answer.capitalize()}")

# Start the game
guess_the_word()
