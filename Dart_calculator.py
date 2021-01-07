

game_type = None

while game_type != "301" and game_type != "501":
    game_type = input("Wybierz typ gry 301 lub 501: ")
    if game_type != "301" and game_type != "501":
        print("Wybierz poprawny typ gry!!!!!!!!!!")

print("Good answer", game_type, "to Twój wybór")
