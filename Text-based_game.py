#----THIS IS THE CLASSES TO USE WHEN CODING OOP----
class Item:
    def __init__(self, name, description, attack=0, defense=0, special=None):
        self.name = name
        self.description = description
        self.attack = attack
        self.defense = defense
        self.special = special
class Player:
    def __init__(self, name, path=None):
        self.name = name
        self.path = path
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
        self.attack += item.attack
        self.defense += item.defense
    def show_status(self):
        print(f"\n{self.name} | Path:{self.path} | Health:{self.health}")
        print(f"Inventory:", [i.name for i in self.inventory])

class Scenarios:
    def __init__(self, description, choices, core_event=None):
        self.description = description
        self.choices = choices
        self.core_event = core_event
    def play(self, player):
        print("\n" + self.description)
        for i, option in enumerate(self.choices.keys(), 1):
            print(f"{i}. {option}")
        choice = int(input("choose an option")) - 1
        option_text = list(self.choices.keys())[choice]
        self.choices[option_text](player)

#----SETTING UP THE COMBAT SYSTEM----
import random
import time
import math

def combat(player, enemy_name, enemy_health, enemy_attack, enemy_defense):
    print(f"You and {enemy_name} started clashing")
    print(f"{enemy_name} | Heath: {enemy_health} | Attack: {enemy_attack} | Defense: {enemy_defense}")
    player_actions = ["slashes in front with the sword", "stepped forward and delivered a deadly stab", "used a kick to create some distance", "tried to lunge forward with the blade", "delivered a deadly slash fatally wounding the enemy"]
    enemy_actions = ["delivered a fatal blow to the body", "slashes frantically", "performed a roll into a stab", "does a kick to the leg trying to knock you off balance", "jumped up and slam down with their sword", "gave you a jab with their left hand into your eye"]
    enemy_attack_multiplier = 1.0
    while player.health > 0 and enemy_health > 0:
        print("\nDecide on what to do next:")
        print("1. Attack")
        print("2. Defend")
        choice = input("> ")

        #This is your turn to attack
        if choice == "1" or choice == "Attack" or choice == "attack":
            verb = random.choice(player_actions)
            damage_to_enemy = max(player.attack - enemy_defense + random.randint(-2, 2), 0)
            enemy_health -= damage_to_enemy
            print(f"You {verb}, You managed to deal {damage_to_enemy} to {enemy_name}")
        elif choice == "2" or choice == "defend" or choice == "Defend":
            print("You brace yourself, raised your sword and ready to parry the next enemy attack")
            damage_reflected = math.ceil(enemy_attack * 0.5)
            enemy_health -= damage_reflected
            enemy_attack_multiplier *= 0.95
            print(f"You managed to deflect the enemy's attack dealing {damage_reflected} and reduced their strength")
        else:
            print("Confused, you hesitated and have lost your window...")
            damage_to_enemy = 0

        print(f"{enemy_name} | Health = {enemy_health}")
        time.sleep(1.5)

        if enemy_health <= 0:
            print(f"\nYou have overcome your challenge. Very impressive {player.name}!\n")
            return True

        #This is the enemy's turn to attack
        enemy_verb = random.choice(enemy_actions)
        damage_to_player = math.ceil(max(enemy_attack - player.defense + random.randint(-2, 1), 0) * enemy_attack_multiplier)
        player.health -= damage_to_player
        print(f"{enemy_name} {enemy_verb}. Dealing {damage_to_player} to you")
        print(f"Your remaining health: {player.health}")
        time.sleep(1.5)

        if player.health <= 0:
            print("\nYou have been defeated...This is where your journey ends.")
            return False

#----FUNCTIONS TO USE FOR THE 1ST SCENARIO----
def join_shinsengumi(player):
    player.path = "Shinsengumi"
    print(f"\nYou run to assist the Shinsengumi. The rebel managed to escape but you were then noticed by their officer for you exceptional skills.")
    shinsengumi_test(player)

def join_rebel(player):
    player.path = "Rebel"
    print(f"\nYou decided to help the samurai. both of you managed to escape. The rebel thank you and offered you a spot in the organisation")
    rebel_test(player)

def join_ronin(player):
    player.path = "Ronin"
    print(f"\nYou decided not to help anyone, keep going your own path as a samurai with no master. A Ronin.")
    ronin_demon_fight(player)

#----FUNCTIONS FOR THE SECOND SCENARIO----
def shinsengumi_test(player):
    print("Your commander tests your loyalty and skill in a duel.")
    result = combat(player, "Shinsengumi Commander Saito", 100, 12, 0)
    if not result:
        return
    print("You fight bravely and earned their respect.")
    katana_of_justice = Item("Blade of the Wind", "A polished blade symbolizing honor and loyalty to the Tokugawa shogunate", 15, 0)
    player.add_item(katana_of_justice)
    inn_scene(player)

def rebel_test(player):
    print("The rebel have decided to put a test to your skills in a duel.")
    result = combat(player, "Rebel Elite Honda", 100, 7, 5)
    if not result:
        return
    print("You managed to show your ways with the blade and they have deemed you worthy for their cause.")
    rebel_crimson_armor = Item("Crimson Armor", "An armor created by the rebe showing that they no longer depend on the shogunate", 0, 15)
    player.add_item(rebel_crimson_armor)
    inn_scene(player)

def ronin_demon_fight(player):
    print("You seek refuge at nearby temple where a previous dealy battle has happened. At night there has been rumours of a mysterious samurai ghost wandering around the temple")
    result = combat(player, "Dead Samurai Demon", 120, 10, 5)
    if not result:
        return
    print("You managed to defeat the ghost commander Honda")
    cursed_blade = Item("Cursed Odachi", "A massive Katana that was used by the demon commander. There is a strange aura coming from it", 30, -5, "Cursed")
    print("Barely alive, you slay the demon — and claim its cursed blade.")
    player.add_item(cursed_blade)
    inn_scene(player)

#----FUNCTIONS FOR THE 3RD SCENARIO----
def flirt_with(player):
    print("\nYou tell her her music sounds like the sound of heaven itself.")
    print("She blushes, her fingers trembling over the shamisen strings. 'You're quite bold, samurai.'")

def talk_with(player):
    print("\nYou ask how she came to play at the inn.")
    print("'My family once served the court,' she says quietly. 'Now I serve travelers like you.'")

def stay_quiet(player):
    print("\nYou stay silent, letting her music wash over you.")
    print("She glances at you and smiles faintly, as if she can already read your heart.")

def inn_scene(player):
    print("\nAfter the battle, You decided to go to a nearby inn in Kyoto.")
    print("Inside, a graceful woman who is playing the Shamisen by the candlelight. She had eyes like the ocean, shiny long black hair and a smile bright like the morning sun. Her name is Akane")

    inn_choices = {
        "Compliment her playing": flirt_with,
        "Ask about her life": talk_with,
        "stay quiet and listen": stay_quiet
    }
    inn_scenario = Scenarios("You want to make a move.", inn_choices)
    inn_scenario.play(player)


    #The fight at the inn
    print('\nSuddenly, "what the hell is this music it sounds horrid! I will have your head for this." a drunk samurai shouted. He unsheathed his blade ready to slice down anything in his path')
    print("The drunk samurai charges at Akane. What will you do!")
    result = combat(player, "Drunk Samurai", 50, 15, 5)
    if not result:
        return
    print("\nYou have defeated the attacker! Akane looks at you with gratitude")
    print("Her eyes shine with warmth. - She has fallen in love with you")
    akane_picture = Item("Akane's picture", "The picture of the one you love", 0, 5)
    player.add_item(akane_picture)
    player.show_status()

    #restoring your hp
    player.health = 100
    print("\nYou both slept at the inn after that incident. Akane leaning into your chest. Your health has been restored fully.")
    time.sleep(6.5)
    kyoto_war(player)

#----FUNCTION FOR THE 4TH AND LAST SCENARIO----
def kyoto_war(player):
    print("\nAs you woke up in the morning. You heard the sounds of battle eachoed throughout Kyoto. It was a battlefield between the Rebels and Shinsengumi")
    if player.path == "Shinsengumi":
        print("Even though Akane is trying to stop you from joining the battle.")
        print("As a Shinsengumi officer you feel the need to help your comrades and charge into battle")
        print("\nYou found yourself surrounded by rebel samurais in the midst of the chaos")
        for i in range (3):
            battle = combat(player, "Rebel Samurai", 120, 15,5 )
            if not battle:
                return
        print("\nNo matter how many rebel you end up killing. Their was too many of them. The Shinsengumi has been defeated and the capital is burned down.")
        print("You were surrounded and killed despite all the efforts.")
        print("\n----THE END----")
    elif player.path == "Rebel":
        print("Even though Akane is trying to stop you from joining the battle.")
        print("You found yourself wanting to help out the rebellion for a greater good")
        print("\n The rebellion is going well and smoothly until you met the Shinsengumi squadron captain Okita Souji.")
        battle = combat(player, "Okita Souji", 250, 25, 20)
        if not battle:
            return
        print("\nDespite managing to defeat Okita, the wound you received were too much")
        print("You eventually succumbs to your wounds and die")
        print("\n----THE END----")
    elif player.path == "Ronin":
        print("Akane convinced you to not join the battle.")
        print("You decided not join join the battle and promise to Akane that you will protect her for the rest of your life")
        print("\nSome rebels broke into the inn trying to sack it and kill everyone")
        for i in range(3):
            battle = combat(player, "Rebel Samurai", 75, 15, 5)
            if not battle:
                return
        print("\nThe Shinsengumi Okita Souji stormed into the inn thinking you are a Rebel")
        battle = combat(player, "Okita Souji", 150, 25, 10)
        if not battle:
            return
        print("\nYou and Akane managed to flee Kyoto")
        print("Both of you guys managed to start a happy life together in the country side and live happily ever after")
        print("\n----THE END----")

#----THIS IS THE BASIC CODE FOR THE GAME----(a function that helps start everything and innitiate everything via function call)
def start_game():
    print("You're wandering the streets of Kyoto...")
    name = input("What should you be called?")
    player = Player(name)
    print(f"\nWelcome {player.name}. The winds of Kyoto will take you to many things.")
    starter_sword = Item("Rusty Katana", "A sword with a fading edge that has witnessed many battles", 5, 0)
    player.add_item(starter_sword)
    player.show_status()

    first_scene = Scenarios(
        "You witnessed a fierce clash between a Shinsengumi officer Kondo and Rebel samurai Batosai",
        {
            "Help the Shinsengumi officer Kondo": join_shinsengumi,
            "Help the rebel samurai Batosai": join_rebel,
            "Do nothing and continue on": join_ronin,
        }
    )
    first_scene.play(player)
    player.show_status()



#----RUNNING THE GAME----
if __name__ == "__main__":
    start_game()








