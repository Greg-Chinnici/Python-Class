#battlegame2.py
import csv
import random
import math

'''
This is my class for all of special character classes. If I split it up it would only be repeated code, so I've decided against that.
this seems pretty robust while maintaing an good structure.
'''

class Character:
    def __init__(self, stats):
        self.name = stats["name"]
        self.className = stats["class"]
        self.special_attack_min = int(stats["special_attack_min"])
        self.special_attack_max = int(stats["special_attack_max"])
        self.health = int(stats["health"])
        self.cooldown = int(stats["cooldown"])
        self.turns_since = int(stats["turns_since"])
        self.armor = None
        self.weapon = None

    def set_armor(self, armor):
        self.armor = armor
        return

    def set_weapon(self, weapon):
        self.weapon = weapon
        return

    def attack(self, victim, requested_special_attack):
        damage = self.calculate_damage_given(requested_special_attack)
        if (damage < 0):
            print(f"{self.name} healed for {damage * -1} damage this round")
        else:
            print(f"{self.name} attacked for {damage} damage this round")
        victim.take_damage(damage)
        return

    def calculate_damage_given(self, requested_special_attack):
        if (requested_special_attack):
            print("Special Attack Attempted.")
            if (self.turns_since >= self.cooldown):
                print("Special Attack Used")
                self.turns_since = 0
                if (random.randint(0,10) <= 2):
                    return -2
                return random.randint(self.special_attack_min, self.special_attack_max)
        print("Basic Attack Used")
        if self.weapon.ideal == self.className:
            return random.randint(self.weapon.damage[0],self.weapon.damage[1])
        return random.randint(self.weapon.damage[0],self.weapon.damage[1] - 1)

    def calculate_damage_taken(self,damage):
        if (damage < 0): #healed
            return damage
        debuff = 0
        if (random.uniform(0,1) < self.armor.blocking_chance):
            debuff = random.randint(self.armor.block_range[0],self.armor.block_range[1])
        print(f"{self.name} was dealt {damage} and blocked {debuff}.")
        damage -= debuff
        if (damage < 0):
            damage = 0
        return damage

    def take_damage(self, damage):
        net_damage = self.calculate_damage_taken(damage)
        print(f"{self.name} took a total of {net_damage}.")
        self.health -= net_damage
        if (self.health < 0):
            self.health = 0
        print(f"{self.name} has {self.health} health points left.\n")
        return

    def nameplate(self):
        return f"{self.name} who is a {self.className}"

    def is_alive(self):
        return int(self.health) > 0

    def deathMessage(self):
        possibleMessages = [
            f"Looks like {self.name} has died",
            f"{self.name} has died",
            f"{self.name} has met his end",
            f"{self.name} has fallen and will never get up",
            f"{self.name} has ended thier journey",
            f"{self.name} flew too close ot the sun"
        ]
        return random.choice(possibleMessages)

    def cooldown_spec(self):
        self.turns_since += 1

class Weapon:
    def __init__(self, stats):
        self.name = stats["name"]
        self.damage = (stats["damage"])
        self.ideal = stats["ideal"]
    def nameplate(self):
        return f'This is a {self.name} it deals from {self.damage[0]} to {self.damage[1]} it is most useful to {self.ideal}'


class Armor:
    def __init__(self, stats):
        self.name = stats["name"]
        self.block_range = (stats["block_range"])
        self.blocking_chance = float(stats["blocking_chance"])
    def nameplate(self):
        return f'This is a {self.name} it blocks from {self.block_range[0]} to {self.block_range[1]} it has a {self.blocking_chance} chance to block incoming damage'



#usable Lists -----------------------------------------------


available_characters = {}

weapons = {
    'Vile Battle Axe' :{'name': 'Vile Battle Axe', 'damage': [10,12], 'ideal': 'dps'},
    'Vindicator Ironbark War Axe': {'name': 'Vindicator Ironbark War Axe', 'damage': [9,15], 'ideal': 'dps'},
    'Bloodcursed Bone Crescent' : {'name': 'Bloodcursed Bone Crescent', 'damage': [11,14], 'ideal': 'mage'},
    'Oracle, Call of the Summoner' : {'name': 'Oracle, Call of the Summoner', 'damage': [8,15], 'ideal': 'mage'},
    'Harbinger, Pike of Eternal Sorrow':{'name': 'Harbinger, Pike of Eternal Sorrow', 'damage': [9,12], 'ideal': 'tank'},
    'Kinslayer, Protector of the Damned':{'name': 'Kinslayer, Protector of the Damned', 'damage': [8,13], 'ideal': 'tank'},
    'Ballista, Piercer of the Forest': {'name': 'Ballista, Piercer of the Forest', 'damage': [4,20], 'ideal': 'ranger'},
    'Roaring Oak Crossbow': {'name': 'Roaring Oak Crossbow', 'damage': [8,11], 'ideal': 'ranger'},
    'Tooth and Claw, Protectors of Timeless Battles' :{'name': 'Tooth and Claw, Protectors of Timeless Battles', 'damage': [12,16], 'ideal': 'dps'},
    'Avalance, Reflex Bow of Redemption': {'name': 'Avalance, Reflex Bow of Redemption', 'damage': [11,14], 'ideal': 'ranger'}
}

armor = {
    "Warlord's Bronze Chestplate": {"name": "Warlord's Bronze Chestplate", "block_range": [5,10], "blocking_chance": 0.5},
    "Soul Obsidian Greatplate": {"name": "Soul Obsidian Greatplate", "block_range": [5,13], "blocking_chance": 0.7},
    "Head of Slain Wolf": {"name": "Head of Slain Wolf", "block_range": [3,13], "blocking_chance": 0.7},
    "Wartorn Chestpiece":{"name": "Wartorn Chestpiece", "block_range": [5,12], "blocking_chance": 0.6},
    "Heavy Helmet of the Defeated" : {"name": "Heavy Helmet of the Defeated", "block_range": [2,12], "blocking_chance": 0.75},
    "Scaled Leggings of a Dragon": {"name": "Scaled Leggings of a Dragon", "block_range": [5,11], "blocking_chance": 0.7},
    "Bloodied Mail Platelegs":{"name": "Bloodied Mail Platelegs", "block_range": [7,12], "blocking_chance": 0.7},
    "Ghastly Cloth Robes":{"name": "Ghastly Cloth Robes", "block_range": [3,12], "blocking_chance": 0.6},
    "Plaid Kilt": {"name": "Plaid Kilt", "block_range": [5,10], "blocking_chance": 0.6},
    "Underwear": {"name": "Underwear", "block_range": [0,5], "blocking_chance": 0.4}
}

def choose_player_char():
    for key in available_characters.keys():
        print(available_characters[key].nameplate())
    player_choice_name = input("Who do you want to play as?  ").lower()
    while player_choice_name not in available_characters:
        print('not a valid character, wait for dlc')
        player_choice_name = input("Who do you want to play as?  ").lower()
    player_choice = available_characters[player_choice_name]
    del available_characters[player_choice_name]
    return player_choice

def choose_computer_character(characterDictionary): #computer
    return random.choice(list(characterDictionary.values()))

def choose_player_weapon(weaponDictionary):
    for key in weaponDictionary.keys():
        print(weaponDictionary[key].nameplate())
    player_choice_weapon = input("What weapon do you want to use?  ").lower()
    while player_choice_weapon not in weaponDictionary:
        print('not a valid weapon, wait for dlc')
        player_choice_weapon = input("What weapon do you want to use?  ").lower()
    player_choice = weaponDictionary[player_choice_weapon]
    return player_choice

def choose_computer_weapon(weaponDictionary):
    return random.choice(list(weaponDictionary.values()))

def choose_player_armor(armorDictionary):
    for key in armorDictionary.keys():
        print(armorDictionary[key].nameplate())
    player_choice_armor = input("What armor do you want to use?  ").lower()
    while player_choice_armor not in armorDictionary:
        print('not a valid armor, wait for dlc')
        player_choice_armor = input("What armor do you want to use?  ").lower()
    player_choice = armorDictionary[player_choice_armor]
    return player_choice

def choose_computer_armor(armorDictionary):
    return random.choice(list(armorDictionary.values()))

#Gameplay Functions -----------------------------------------------

def getIsAttackSpecialPlayer1():
    response = input('What attack do you want to use? (basic,special):   ').lower()
    print(' ')
    print(' ')
    while (response != 'special' and response != 'basic'):
        response = input('What attack do you want to use? (basic,special):   ').lower()
    return (response == 'special')

def getIsAttackSpecialPlayer2():
        return random.choice([True,False])

def round(playerCharacter, computerCharacter, round_count):
    print(f"ROUND {round_count} ---------------------")
    playerCharacter.attack(computerCharacter, getIsAttackSpecialPlayer1())
    if (not computerCharacter.is_alive()):
        print(computerCharacter.deathMessage())
        print("You Win.")
        return

    computerCharacter.attack(playerCharacter, getIsAttackSpecialPlayer2())
    if (not playerCharacter.is_alive()):
        print(playerCharacter.deathMessage())
        print(f"Sorry, {computerCharacter.name} won")
        return

def initialize_character_dictionary():
    #prints char and their class
    char_csv = csv.DictReader(open('chars.csv' , 'r'))
    for line in char_csv:
        available_characters[line['name']] = Character(line)

def initialize_weapons_dictionary(weaponDictionary):
    for key in weaponDictionary.keys():
        available_weapons[key.lower()] = Weapon(weaponDictionary[key])
    return
available_weapons = {}
def initialize_armor_dictionary(armorDictionary):
    for key in armorDictionary.keys():
        available_armor[key.lower()] = Armor(armorDictionary[key])
    return
available_armor = {}

def game():
    playerCharacter = choose_player_char()
    computerCharacter = choose_computer_character(available_characters)


    playerCharacter.set_weapon(choose_player_weapon(available_weapons))
    computerCharacter.set_weapon(choose_computer_weapon(available_weapons))


    playerCharacter.set_armor(choose_player_armor(available_armor))
    computerCharacter.set_armor(choose_computer_armor(available_armor))

    print("Welcome to Battledome. You\'re playing as " + playerCharacter.nameplate())
    print("Welcome your advesary to the Battledome. You\'re playing against " + computerCharacter.nameplate())

    round_count = 0
    while (playerCharacter.is_alive() and computerCharacter.is_alive()):
        round_count += 1
        round(playerCharacter, computerCharacter, round_count)
        playerCharacter.cooldown_spec()
        computerCharacter.cooldown_spec()

###Main -----------------------------------------------

initialize_character_dictionary()
initialize_weapons_dictionary(weapons)
initialize_armor_dictionary(armor)
game()
