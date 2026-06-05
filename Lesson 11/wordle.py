# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# TODO Import random so you can randomise the word
import random


# VALUES
# TODO Create a list of at least 5 different 5-letter words
words = [
    "apple", "grape", "lemon", "mango", "peach", "berry", "cherry", "pearl",
    "plumb", "prune", "cider", "bread", "crane", "flame", "glove", "heart", "jelly",
    "knife", "light", "mouse", "noble", "ocean", "piano", "queen", "river", "stone",
    "tiger", "ultra", "vivid", "wheat", "xenon", "yacht", "zebra", "cable", "dance",
    "eagle", "fable", "giant", "honey", "ivory", "jewel", "alloy", "lucky", "magic",
    "ninja", "oasis", "plier", "quilt", "robot", "sugar", "tulip", "unity", "vapor",
    "whale", "table", "zesty", "slate", "crisp", "flock", "lucky"
    ]
# TODO Create a variable called play and set it to True
play = True

# INTRODUCTION
# TODO Tell your user how to play wordle (make sure they know they must input 5 letter words)

print("Welcome to Wordle, guess the 5 letter word")

# game loop
while play:
    word = random.choice(words)
    attempts = 7
    print("You have 6 attempts to guess the word.")

    for attempt in range(1, attempts):
        guess = input(f"Attempt {attempt} - Enter your 5-letter guess: ").lower().strip()
        while len(guess) != 5:
            guess = input("Invalid entry. Please enter a 5-letter word: ").lower().strip()

        if guess == word:
            print(f"Correct! The word was '{word}'. You guessed it in {attempt} attempts.")
            break
        
        # build feedback list   
        feedback = []
        for letter in range(5):
            if guess[letter] == word[letter]:
                feedback.append(f"\033[42m{guess[letter].upper()}\033[0m")  # correct position
            elif guess[letter] in word:
                feedback.append(f"\033[43m{guess[letter].upper()}\033[0m")  # wrong position, right letter
            else:
                feedback.append(f"\033[41m{guess[letter].upper()}\033[0m")  # incorrect

                # make it so that if multiple letters are the same, it only gives feedback for the correct number of letters in the word
                

        print("Feedback:", "".join(feedback))

     #user failed, out of guesses
    if guess != word:
        print(f"Out of attempts. The word was '{word}'.")

    again = input("Play again? (yes/no): ").lower().strip()
    if again != 'yes':
        play = False
    


# ==========================================================
# EXTENSION
# Instead of telling the user one by one about their letters, put each correct letter and _ for a wrong letter into a list. 
# Then finally print the list (you can use "".join(list_name) to merge them into a string if you like)

# ==========================================================
# EXPERT
# Following on from the extension, add colour to the letters instead (Don't use _ for incorrect anymore). Green for correct, orange for wrong place, red for incorrect. You'll need to add the colour as you add them to the list

# print("\033[31mThis is Red Text\033[0m")
# print("\033[38;2;255;165;0mThis is Orange Text\033[0m")
# print("\033[32mThis is Green Text\033[0m")

