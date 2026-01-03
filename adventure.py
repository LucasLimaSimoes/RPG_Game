import random

def go_adventuring(player):
    print("\n🌲 You venture into the wilderness...\n")

    enemy_hp = random.randint(40, 80)
    enemy_attack = random.randint(6, 14)
    reward_gold = random.randint(15, 35)
    reward_exp = random.randint(25, 60)

    defending = False

    while enemy_hp > 0 and player.is_alive():
        print("\n------------------")
        print(f"Enemy HP: {enemy_hp}")
        print(f"Your HP: {player.hp}")
        print(f"Potions: {player.potions}")
        print("------------------")

        print("1. Attack")
        print("2. Defend")
        print("3. Use Potion")
        print("4. Run")

        choice = input("> ")

        # PLAYER TURN
        if choice == "1":
            damage = player.attack
            enemy_hp -= damage
            print(f"You attack and deal {damage} damage!")
            defending = False

        elif choice == "2":
            defending = True
            print("You brace yourself. Incoming damage will be reduced.")

        elif choice == "3":
            if player.potions > 0:
                player.potions -= 1
                heal = 30
                player.hp = min(player.max_hp, player.hp + heal)
                print(f"You use a potion and recover {heal} HP.")
            else:
                print("You have no potions!")
                continue  # enemy does NOT attack if invalid action

        elif choice == "4":
            if random.random() < 0.5:
                print("🏃 You successfully escaped!")
                return
            else:
                print("You failed to escape!")

        else:
            print("Invalid choice.")
            continue

        # ENEMY TURN
        if enemy_hp > 0:
            damage = enemy_attack
            if defending:
                damage //= 2
                print("Your defense reduces the damage!")

            player.hp -= damage
            print(f"The enemy attacks for {damage} damage!")

    # END OF BATTLE
    if player.is_alive():
        print("\n✅ You defeated the enemy!")
        print(f"You gain {reward_gold} gold.")
        player.gold += reward_gold
        player.gain_exp(reward_exp)
    else:
        print("\n💀 You were defeated...")
        print("You wake up in town with half HP.")
        player.hp = player.max_hp // 2
