import json
from player import Player

SAVE_FILE = "save.json"

def save_game(player):
    data = {
        "name": player.name,
        "level": player.level,
        "exp": player.exp,
        "exp_to_level": player.exp_to_level,
        "max_hp": player.max_hp,
        "hp": player.hp,
        "attack": player.attack,
        "gold": player.gold,
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

    print("💾 Game saved successfully.")

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

        player = Player(data["name"])
        player.level = data["level"]
        player.exp = data["exp"]
        player.exp_to_level = data["exp_to_level"]
        player.max_hp = data["max_hp"]
        player.hp = data["hp"]
        player.attack = data["attack"]
        player.gold = data["gold"]

        print("📂 Game loaded successfully.")
        return player

    except FileNotFoundError:
        print("No save file found.")
        return None