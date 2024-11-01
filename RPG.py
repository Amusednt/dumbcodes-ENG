import random

# Class to represent a character (player)
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def attack_enemy(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.attack} damage!")
        enemy.take_damage(self.attack)

# Class to represent an item
class Item:
    def __init__(self, name, healing_amount):
        self.name = name
        self.healing_amount = healing_amount

    def use(self, character):
        character.health += self.healing_amount
        print(f"{character.name} uses {self.name} and heals {self.healing_amount} health! Health is now {character.health}.")

# Class to represent an enemy
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")

    def attack_character(self, character):
        print(f"{self.name} attacks {character.name} for {self.attack} damage!")
        character.take_damage(self.attack)

# Function to represent a game phase
def game_phase():
    # Create a player character
    player = Character(name="Hero", health=100, attack=20)

    # Create a healing item
    healing_potion = Item(name="Healing Potion", healing_amount=30)

    # Create enemies
    goblin = Enemy(name="Goblin", health=30, attack=10)
    boss = Enemy(name="Dragon", health=100, attack=15)

    # Start the phase with the goblin
    print("A wild Goblin appears!")
    while goblin.is_alive() and player.is_alive():
        player.attack_enemy(goblin)
        if goblin.is_alive():
            goblin.attack_character(player)
        print()  # New line for better readability

    if player.is_alive():
        print("Goblin defeated! You found a Healing Potion.")
        healing_potion.use(player)

        # Now face the final boss
        print("A fierce Dragon appears!")
        while boss.is_alive() and player.is_alive():
            player.attack_enemy(boss)
            if boss.is_alive():
                boss.attack_character(player)
            print()  # New line for better readability

        if player.is_alive():
            print("Congratulations! You have defeated the Dragon and completed the phase.")
        else:
            print("You have been defeated by the Dragon. Game Over!")
    else:
        print("You have been defeated by the Goblin. Game Over!")

# Run the game phase
if __name__ == "__main__":
    game_phase()