import random

# ASCII art för slagskämpar
fighter_a_art = r"""
 O
/|\
/ \
"""
fighter_b_art = r"""
 @
/|\
/ \
"""

# Skapa klassen för slagskämparna
class Fighter:
    def __init__(self, name, hp, strength, accuracy):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.accuracy = accuracy

    # Metod för att attackera med två valmöjligheter
    def attack(self, opponent):
        print(f"\n{self.name}'s tur att attackera!")
        print("1. Stark attack (50% chans att träffa, hög skada)")
        print("2. Svag attack (80% chans att träffa, låg skada)")
        choice = input("Välj en attack (1 eller 2): ")

        if choice == "1":
            hit_chance = 0.5
            damage_range = (10, 20)
        else:
            hit_chance = 0.8
            damage_range = (5, 10)

        if random.random() < hit_chance:
            damage = random.randint(*damage_range)
            opponent.hp -= damage
            print(f"{self.name} träffade {opponent.name} för {damage} skada!")
        else:
            print(f"{self.name} missade!")

# Funktion för att validera spelarens namn
def get_valid_name():
    while True:
        name = input("Skriv in namn på din slagskämpe (3-10 tecken): ")
        if 3 <= len(name) <= 10:
            return name
        else:
            print("Namnet måste vara mellan 3 och 10 tecken långt.")

# Funktion för att hantera spelarens satsning
def place_bet(money):
    while True:
        try:
            bet = int(input(f"Hur mycket pengar vill du satsa? Du har {money} kr: "))
            if 0 < bet <= money:
                return bet
            else:
                print("Du måste satsa ett belopp mellan 1 och dina tillgängliga pengar.")
        except ValueError:
            print("Ange ett giltigt nummer.")

# Funktion för att välja satsning på att vinna eller förlora
def choose_bet_type():
    while True:
        bet_type = input("Vill du satsa på att du vinner eller förlorar? (v/f): ").lower()
        if bet_type in ["v", "f"]:
            return bet_type
        else:
            print("Ange 'v' för att vinna eller 'f' för att förlora.")

# Huvudprogrammet
def fight_simulator():
    # Spelaren börjar med en viss mängd pengar
    player_money = 1000
    while True:
        # Låt spelaren skriva in sitt namn
        fighter_a_name = get_valid_name()

        # Slumpa namn för slagskämpe B
        random_names = ["Gladiator", "Samurai", "Ninja"]
        fighter_b_name = random.choice(random_names)

        # Skapa slagskämpar
        fighter_a = Fighter(fighter_a_name, 100, 10, 0.7)
        fighter_b = Fighter(fighter_b_name, 100, 10, 0.7)

        # Visa ASCII-art för slagskämpar
        print(f"\n{fighter_a_name} går in i ringen!")
        print(fighter_a_art)
        print(f"\n{fighter_b_name} går in i ringen!")
        print(fighter_b_art)

        # Låt användaren välja antal rundor
        while True:
            try:
                rounds = int(input("\nVälj antal rundor (min 3, max 10): "))
                if 3 <= rounds <= 10:
                    break
                else:
                    print("Antalet rundor måste vara mellan 3 och 10.")
            except ValueError:
                print("Ange ett giltigt nummer för antal rundor.")

        # Spelaren satsar pengar
        bet = place_bet(player_money)
        bet_type = choose_bet_type()

        # Fight loop
        for round_num in range(1, rounds + 1):
            print(f"\nRunda {round_num} börjar!")
            
            # Slagskämpe A attackerar B
            fighter_a.attack(fighter_b)

            # Kolla om B är utslagen
            if fighter_b.hp <= 0:
                print(f"\n{fighter_a.name} vann striden!")
                break

            # Slagskämpe B attackerar A (slumpmässig attack)
            attack_choice = random.choice(["1", "2"])
            print(f"\n{fighter_b.name} väljer attack {attack_choice}")
            fighter_b.attack(fighter_a)

            # Kolla om A är utslagen
            if fighter_a.hp <= 0:
                print(f"\n{fighter_b.name} vann striden!")
                break

        # Om ingen vann, avgör baserat på HP
        if fighter_a.hp > 0 and fighter_b.hp > 0:
            print("\nStriden är över! Räkna poäng...")
            if fighter_a.hp > fighter_b.hp:
                print(f"{fighter_a.name} vann på poäng!")
            elif fighter_b.hp > fighter_a.hp:
                print(f"{fighter_b.name} vann på poäng!")
            else:
                print("Det blev oavgjort!")

        # Bestäm om spelaren vann sin satsning
        if (fighter_a.hp > fighter_b.hp and bet_type == "v") or (fighter_a.hp <= fighter_b.hp and bet_type == "f"):
            player_money += bet
            print(f"Grattis! Du vann din satsning och nu har du {player_money} kr.")
        else:
            player_money -= bet
            print(f"Tyvärr, du förlorade din satsning och nu har du {player_money} kr.")

        # Om pengarna tar slut
        if player_money <= 0:
            print("Du har slut på pengar. Spelet är över.")
            break

        # Möjlighet att starta om spelet
        if input("\nVill du spela igen? (ja/nej): ").lower() != "ja":
            break

# Kör simulatorn
fight_simulator()
