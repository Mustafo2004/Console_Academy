# 1. Create a list of mobile games (at list 4 games) with input function
game_1 = input("Game 1: ")
game_2 = input("Game 2: ")
game_3 = input("Game 3: ")
game_4 = input("Game 4: ")

games = []
games.append(game_1)
games.append(game_2)
games.append(game_3)
games.append(game_4)

print(games)

# 2. Delete the game from user input
games = ["GTA", "Counter Strike", "Pubg", "Dota", "Fifa"]

print(games)
answer = input("Which game do you want to delete? ")

if answer in games:
    games.remove(answer)
    print("Successfully deleted:", answer)
    print(games)
else:
    print("There is not a game called:", answer)
    print(games)