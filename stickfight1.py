import random

# Fighter klass
class Fighter:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, opponent):
        hit_chance = random.random()  # Slumpa om attacken träffar
        if hit_chance < 0.7:  # 70% chans att träffa
            damage = random.randint(5, 15)
            opponent.hp -= damage
            print(f"{self.name} träffade {opponent.name} för {damage} skada!")
        else:
            print(f"{self.name} missade!")

# Huvudfunktion
def fight_simulator():
    player_money = 1000  # Startpengar
    while player_money > 0:
        player_name = input("Skriv ditt namn: ")
        fighter_a = Fighter(player_name, 100)
        fighter_b = Fighter(random.choice(["Gladiator", "Samurai", "Ninja"]), 100)

        print(f"\n{fighter_a.name} vs {fighter_b.name}!")

        # Satsa pengar
        while True:
            try:
                bet = int(input(f"Du har {player_money} kr. Hur mycket vill du satsa? "))
                if 0 < bet <= player_money:
                    break
            except ValueError:
                pass
        bet_type = input("Satsa på att du vinner (v) eller förlorar (f): ").lower()

        # Strid
        while fighter_a.hp > 0 and fighter_b.hp > 0:
            fighter_a.attack(fighter_b)
            if fighter_b.hp <= 0:
                break
            fighter_b.attack(fighter_a)

        # Avgör resultat och uppdatera pengar
        if fighter_a.hp > 0:
            print(f"{fighter_a.name} vann!")
            if bet_type == 'v':
                player_money += bet
            else:
                player_money -= bet
        else:
            print(f"{fighter_b.name} vann!")
            if bet_type == 'f':
                player_money += bet
            else:
                player_money -= bet
        print(f"Du har nu {player_money} kr kvar.")

        # Fråga om spelaren vill spela igen
        if input("Vill du spela igen? (ja/nej): ").lower() != "ja":
            break

    print("Spelet är slut.")

# Starta spelet
fight_simulator()
