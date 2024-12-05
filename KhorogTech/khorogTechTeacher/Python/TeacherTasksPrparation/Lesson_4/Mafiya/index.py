players = [
    {"name": "Player 1", "role": "mafiya", "status": "alive"},
    {"name": "Player 2", "role": "sheriff", "status": "alive"},
    {"name": "Player 3", "role": "civilian", "status": "alive"},
    {"name": "Player 4", "role": "civilian", "status": "alive"}
]
def print_players(players):
    for player in players:
        print(f"{player['name']} - {player['role']} - {player['status']}")

print_players(players)
def mafiya_turn(players):
    for player in players:
        if player["role"] == "mafiya" and player["status"] == "alive":
            while True:
                target = input("Mafiya, choose a player to eliminate: ")
                for p in players:
                    if p["name"] == target and p["status"] == "alive":
                        p["status"] = "eliminated"
                        print(f"{p['name']} has been eliminated.")
                        return
                print("Invalid choice, try again.")

mafiya_turn(players)
print_players(players)
def sheriff_turn(players):
    for player in players:
        if player["role"] == "sheriff" and player["status"] == "alive":
            while True:
                target = input("Sheriff, choose a player to investigate: ")
                for p in players:
                    if p["name"] == target and p["status"] == "alive":
                        print(f"{p['name']} is a {p['role']}.")
                        return
                print("Invalid choice, try again.")

sheriff_turn(players)
def civilians_turn(players):
    while True:
        vote = input("Civilians, choose a player to eliminate: ")
        for p in players:
            if p["name"] == vote and p["status"] == "alive":
                p["status"] = "eliminated"
                print(f"{p['name']} has been eliminated by the civilians.")
                return
        print("Invalid choice, try again.")

civilians_turn(players)
print_players(players)
def check_game_over(players):
    mafiya_alive = False
    civilians_alive = False
    for player in players:
        if player["role"] == "mafiya" and player["status"] == "alive":
            mafiya_alive = True
        elif player["role"] != "mafiya" and player["status"] == "alive":
            civilians_alive = True
    if not mafiya_alive:
        print("Civilians win!")
        return True
    if not civilians_alive:
        print("Mafiya wins!")
        return True
    return False

def game_loop(players):
    while True:
        mafiya_turn(players)
        if check_game_over(players):
            break
        sheriff_turn(players)
        if check_game_over(players):
            break
        civilians_turn(players)
        if check_game_over(players):
            break

game_loop(players)
