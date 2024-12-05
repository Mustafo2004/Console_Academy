# create a list of famous brend (4-brend) with input
brend_1 = input("Game 1: ")
brend_2 = input("Game 2: ")
brend_3 = input("Game 3: ")
brend_4 = input("Game 4: ")

games = []
games.append(brend_1)
games.append(brend_2)
games.append(brend_3)
games.append(brend_4)

print(games)

# Delete the brends from user input 
brends = ["Nike", "Addidas" , "NorthFace","Gucci"]
print(games)
answer = input("Which brend do you want to delete? ")

if answer in brends:
    brends.remove(answer)
    print("Successfully deleted:", answer)
    print(games)
else:
    print("There is not a game called:", answer)
    print(games)