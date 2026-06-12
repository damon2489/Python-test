# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# TODO Import random module
import random
# Wild Pokemon
# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
pokemon = [
    {"name": "Pikachu", "max_health": 100, "type": "Electric", "attacks": [20, 10, 15, 25]},
    {"name": "Charmander", "max_health": 120, "type": "Fire", "attacks": [15, 10, 20, 25]},
    {"name": "Bulbasaur", "max_health": 110, "type": "Grass", "attacks": [18, 12, 22, 30]},
    {"name": "Squirtle", "max_health": 90, "type": "Water", "attacks": [25, 15, 20, 35]}
]
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage


chikorita_attacks = [
    {"name": "Razor Leaf", "damage": 20, "attack_type": "Grass"},
    {"name": "Will-O-Wisp", "damage": 10, "attack_type": "Fire"},
    {"name": "Tackle", "damage": 10, "attack_type": "Normal"},
    {"name": "Vine Whip", "damage": 15, "attack_type": "Grass"}
]
cyndaquil_attacks = [
    {"name": "Ember", "damage": 15, "attack_type": "Fire"},
    {"name": "Scald", "damage": 10, "attack_type": "Water"},
    {"name": "Tackle", "damage": 10, "attack_type": "Normal"},
    {"name": "Flamethrower", "damage": 20, "attack_type": "Normal"}
]
totodile_attacks = [
    {"name": "Water Gun", "damage": 15, "attack_type": "Water"},
    {"name": "Hydro Pump", "damage": 25, "attack_type": "Water"},
    {"name": "Tackle", "damage": 10, "attack_type": "Normal"},
    {"name": "Bite", "damage": 15, "attack_type": "Dark"}
]



# TODO Create a variable to hold a randomised wild pokemon
random_pokemon = random.choice(pokemon)
# TODO Create a opponent_health variable and set it to the max health of the random pokemon
opponent_health = random_pokemon["max_health"]
# TODO Tell the user what pokemon they're facing
print("Choose your pokemon")
user_pokemon_choice = input("1. Chikorita  2. Cyndaquil  3. Totodile ")

user_pokemon = [{"name": "Chikorita", "type": "Grass", "attacks": chikorita_attacks},
    {"name": "Cyndaquil", "type": "Fire", "attacks": cyndaquil_attacks},
    {"name": "Totodile", "type": "Water", "attacks": totodile_attacks}]
print(f"You chose {user_pokemon[int(user_pokemon_choice)-1]['name']}!")

print(f"You're facing a wild {random_pokemon['name']}!")
# TODO Create a while loop that continues until opponent health <= 0
while opponent_health > 0:
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    attack_choice = input("Choose your attack, answer with a number (1-4): 1. " + user_pokemon[int(user_pokemon_choice)-1]['attacks'][0]['name'] + " 2. " + user_pokemon[int(user_pokemon_choice)-1]['attacks'][1]['name'] + " 3. " + user_pokemon[int(user_pokemon_choice)-1]['attacks'][2]['name'] + " 4. " + user_pokemon[int(user_pokemon_choice)-1]['attacks'][3]['name'])
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from opponent health
    opponent_health = opponent_health - user_pokemon[int(user_pokemon_choice)-1]['attacks'][int(attack_choice)-1]['damage']
    if attack_choice not in ["1", "2", "3", "4"]:
        print("Please enter a valid number (1-4).")
        continue

    # opponent uses attack
random_pokemon_attack = random.choice(random_pokemon["attacks"])


if opponent_health > 0:
        print(f"You used {user_pokemon[int(user_pokemon_choice)-1]['attacks'][int(attack_choice)-1]['name']}! The wild {random_pokemon['name']} has {opponent_health} health left.")

if opponent_health <= 0:
    print(f"You defeated the wild {random_pokemon['name']}!")
    


    

# TODO Tell the user they defeated the pokemon

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.