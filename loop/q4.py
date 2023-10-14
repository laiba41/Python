
banned_users_new_name = ['eve', 'fred', 'gary', 'helen']
prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "
players_new_name = []

while True:
    player = input(prompt)

    if player.lower() == 'quit':
        break
    elif player in banned_users_new_name:
        print(f"{player} is banned!")
    elif player in players_new_name:
        print(f"{player} is already on your team!")
    else:
        players_new_name.append(player)
        print(f"{player} has been added to your team.")

print("\nYour team (original names):")
for player in players_new_name:
    print(player)

# Now, if you want to change names for the players on your team:
change_names = input("Do you want to change the names of players on your team? (yes/no): ")

if change_names.lower() == "yes":
    for i, player in enumerate(players_new_name):
        new_name = input(f"Enter a new name for {player}: ")
        players_new_name[i] = new_name

print("\nYour team (updated names):")
for player in players_new_name:
    print(player)
