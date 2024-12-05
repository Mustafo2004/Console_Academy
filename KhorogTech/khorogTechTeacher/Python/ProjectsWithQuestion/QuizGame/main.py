
# ! QuizGame
# Function to add players
def add_players():
    count_player = int(input("How many players are playing? "))
    players = []
    for i in range(count_player):
        name = input("Enter your name: ")
        players.append(name)
    return players

# List of quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    }
]

# Function to play the quiz
def play_quiz(players):
    scores = {}
    for player in players:
        scores[player] = 0

    for question in quiz_questions:
        print(question["question"])
        for option in question["options"]:
            print(option)

        for player in players:
            answer = input(f"{player}, choose your answer (A, B, C, D): ").upper()
            if answer == question["answer"]:
                scores[player] += 1
            else:
                print(f"Oops! The correct answer was {question['answer']}.")

    return scores

# Function to find and announce the winner
def find_winner(scores):
    highest_score = max(scores.values())
    winners = []
    for player, score in scores.items():
        if score == highest_score:
            winners.append(player)

    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")

    if len(winners) > 1:
        print("\nIt's a tie! The winners are:")
        for winner in winners:
            print(winner)
    else:
        print(f"\nThe winner is {winners[0]} with {highest_score} points!")

# Main part of the program
players = add_players()
scores = play_quiz(players)
find_winner(scores)
