# =====================================================================
# Task: Country Guessing Game
# =====================================================================
print("Welcome to the Country Guessing Game!")
print("You have 3 guesses")
# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
# TODO: Create a variable to keep track of the user's current guess. 
#       (Hint: Start it as an empty string "" so the loop runs at least once!)

import random
countries = ['italy', 'france', 'spain', 'germany', 'japan',
              'brazil', 'canada', 'australia', 'india', 'mexico',
                'china', 'russia', 'egypt', 'greece', 'turkey']
correct_country = random.choice(countries)
user_guess = "".lower().strip()

counter=0
# LOOP
# TODO: Start a 'while' loop. 
#       The loop should keep running AS LONG AS the user's guess 
#       is NOT EQUAL to the correct country.
while user_guess != correct_country:

    # TODO: Ask the user for their guess and save it to your guess variable.
    #       (Remember: This changes the loop condition so it doesn't run forever!)
    user_guess = input("Guess the country: ")

    # TODO: (Optional) Add an 'if' statement inside the loop.
    #       If they guessed wrong, print an encouraging message or an extra hint.
    #       If they guessed right, the loop will automatically exit on the next check!
    if user_guess != correct_country:
        print("Wrong guess! Try again.")
        print("Hint: The name of the country has", len(correct_country), "letters.")
        hint1=len(correct_country)
        
    counter += 1
    if counter==2:
        print("Hint: The name of the country starts with", correct_country[0])    
    elif counter==3:
        print("Game over! You've used all your guesses. The correct country was:", correct_country)
        break


# GAME OVER / WINNING MESSAGE
# TODO: Print a congratulatory message celebrating their win!
if user_guess == correct_country:
    print("Congratulations! You guessed the correct country!")

# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option