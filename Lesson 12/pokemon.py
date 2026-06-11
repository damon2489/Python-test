# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# TODO Import random module
import random
# Wild Pokemon
# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
pokemon = [
    ["Pikachu", 100],
    ["Charmander", 120],
    ["Bulbasaur", 110],
    ["Squirtle", 90]
    ]
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage
attacks = [
    ["Thunder bolt", 20],
    ["Flamethrower", 25],
    ["Vine Whip", 15],
    ["Water Gun", 18]
    ]


# TODO Create a variable to hold a randomised wild pokemon
random_pokemon = random.choice(pokemon)
# TODO Create a current_health variable and set it to the max health of the random pokemon
current_health = random_pokemon[1]
# TODO Tell the user what pokemon they're facing
print(f"You're facing a wild {random_pokemon[0]}!")
# TODO Create a while loop that continues until current health <= 0
while current_health > 0:
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    attack_choice = input("Choose your attack, answer with a number (1-4):  1. Thunder bolt  2. Flamethrower  3. Vine Whip  4. Water Gun ")
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health
    if attack_choice == "1":
        current_health = current_health - 20
    elif attack_choice == "2":
        current_health = current_health - 25
    elif attack_choice == "3":
        current_health = current_health - 15
    elif attack_choice == "4":
        current_health = current_health - 18
    else:
        print("Invalid input, please enter a number between 1 and 4.")
        continue

    if current_health > 0:
        print(f"You used {attacks[int(attack_choice)-1][0]}! The wild {random_pokemon[0]} has {current_health} health left.")

    if current_health <= 0:
        print(f"You defeated the wild {random_pokemon[0]}!")
        break


    

# TODO Tell the user they defeated the pokemon

if current_health <= 0:
    print(f"You defeated the wild {random_pokemon[0]}!")
# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.