import random

choices = ['rock', 'paper', 'scissors']

# Number of rounds to play
rounds = 3

# Start the game for a fixed number of rounds
for _ in range(rounds):
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    # Check if the user's choice is valid using if-else-elif
    if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
        # Computer randomly picks a choice
        computer_choice = random.choice(choices)

        # Show what both the user and the computer chose
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner using if-else-elif
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print("Rock smashes scissors! You win!")
        elif user_choice == 'paper' and computer_choice == 'rock':
            print("Paper covers rock! You win!")
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print("Scissors cut paper! You win!")
        else:
            print("You lose.")
    else:
        print("Please choose rock, paper, or scissors.")

print("Game over! Thanks for playing!")
