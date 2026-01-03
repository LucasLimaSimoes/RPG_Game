def show_player_status(player):
    print("\n====================")
    print(f"Name: {player.name}")
    print(f"Level: {player.level}")
    print(f"EXP: {player.exp}/{player.exp_to_level}")
    print(f"HP: {player.hp}/{player.max_hp}")
    print(f"Attack: {player.attack}")
    print(f"Gold: {player.gold}")
    print("====================\n")