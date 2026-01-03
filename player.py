class Player:
    def __init__(self, name="Hero"):
        self.name = name
        self.level = 1
        self.exp = 0
        self.exp_to_level = 100
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack = 10
        self.gold = 50
        self.potions = 2  # NEW

    def gain_exp(self, amount):
        self.exp += amount
        print(f"You gained {amount} EXP.")

        while self.exp >= self.exp_to_level:
            self.exp -= self.exp_to_level
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp_to_level = int(self.exp_to_level * 1.5)
        self.max_hp += 20
        self.attack += 5
        self.hp = self.max_hp
        print(f"\n🎉 You leveled up to level {self.level}!")
        print(f"Max HP: {self.max_hp}, Attack: {self.attack}\n")

    def is_alive(self):
        return self.hp > 0
