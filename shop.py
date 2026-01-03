def shop(player):
    while True:
        print("\n🏪 Welcome to the Shop")
        print(f"Gold: {player.gold}")
        print("1. Health Potion (+30 HP) - 20 gold")
        print("2. Sword Upgrade (+5 Attack) - 50 gold")
        print("3. Leave Shop")

        choice = input("> ")

        if choice == "1":
            if player.gold >= 20:
                player.gold -= 20
                player.potions += 1
                print("You bought a health potion.")
            else:
                print("Not enough gold.")

        elif choice == "2":
            if player.gold >= 50:
                player.gold -= 50
                player.attack += 5
                print("Your attack increased!")
            else:
                print("Not enough gold.")

        elif choice == "3":
            break
