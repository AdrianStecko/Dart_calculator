

game_type = None

while game_type != "301" and game_type != "501":
    game_type = input("Choose type of the game: ")
    if game_type != "301" and game_type != "501":
        print("Choose correct type of the game!!!")

print("Good choice", game_type, "is your type of game")

player_1 = input("What is first player name? ")
player_2 = input("What is second player name? ")

print("So lets begin the", game_type)