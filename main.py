from player import Player
from adventure import go_adventuring
from shop import shop
from save_load import save_game, load_game
from utils import show_player_status

def main():
    print("🗡️ Welcome to the Command Line RPG 🗡️")
    name = input("Enter your hero's name: ")
    player = Player(name)

    while True:
        show_player_status(player)
        print("Main Menu")
        print("1. Go Adventuring")
        print("2. Shop")
        print("3. Rest")
        print("4. Save Game")
        print("5. Load Game")
        print("6. Quit")

        choice = input("> ")

        if choice == "1":
            go_adventuring(player)

        elif choice == "2":
            shop(player)

        elif choice == "3":
            player.hp = player.max_hp
            print("😴 You rest and recover all HP.")

        elif choice == "4":
            save_game(player)

        elif choice == "5":
            loaded_player = load_game()
            if loaded_player:
                player = loaded_player

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()