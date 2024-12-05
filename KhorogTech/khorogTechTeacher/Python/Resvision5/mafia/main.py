players = [
    {
        "name": "Masrur",
        "role": "citizen",
    },
    {
        "name": "Hisom",
        "role": "citizen",
    },
    {
        "name": "Jahongir",
        "role": "citizen",
    },
    {
        "name": "Murtuzo",
        "role": "citizen",
    },
    {
        "name": "Dilafruz",
        "role": "citizen",
    },
]

def start_game(): 
    print("")
    print("The city will go to sleep!")
    print("The host will choose mafia")
    choose_mafia()

def choose_mafia():
    print("")
    print(players)
    mafia = input("Who do you want to be a mafia... ")
    
    found = True
    
    for player in players:
        if player["name"] == mafia:
            player["role"] = "mafia"
            found = True
            # print(player)
            break
        else:
            found = False
    
    
    if found == False:
        print("")
        print("There is not player with this name. Try again")
        choose_mafia()
    else:
        mafia_start_to_kill()
        

def mafia_start_to_kill():
    print("")
    print("Everyone is sleeping!")
    print("Mafia wake up!")
    
    print(players)
    victim = input("You are mafia. Choose the victim... ")

    for player in players:
        if player["name"] == victim:
            players.remove(player)
            found = True
            break
        else:
            found = False
    
    if found == False:
        print("")
        print("There is not player with this name. Try again")
        mafia_start_to_kill()
    
    print(players)
    find_mafia(victim)

def find_mafia(dead):
    print("")
    print("Everyone, Wake up!")
    print("Mafia killed one person tonight")
    print("And it is...")
    print(dead)
    print("")
    print("Now citizen should find the mafia")
    
    # print(players)
    suspectced = input("Who do you think mafia is... ")

    for player in players:
        if player["name"] == suspected and player["role"] == "mafia":
            players.remove(player)
            print("")
            print("Congratulation! You have found the mafia")
            stop_game()
            break
        elif player["name"] == suspected and player["role"] == "citizen":
            players.remove(player)
            print("")
            print("Nope! You voted off the citizen!")
            print(players)
            mafia_start_to_kill() 
            break

def stop_game():
    return       

start_game()