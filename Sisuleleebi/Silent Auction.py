
players = {}

def add_player(player_name, player_bid):
    players[player_name] = int(player_bid)

new_players = True
while new_players == True:
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    add_player(name, bid)
    nomore = input("Are there any other players?: Y/N ").lower()
    if nomore == "n":
        new_players = False
    else:
        clear()

highest = 0
highest_name = ""

for value in players:

    if players[value] > highest:
        highest = players[value]
        highest_name = str(value)


print("winner is " + highest_name + " " + highest)


