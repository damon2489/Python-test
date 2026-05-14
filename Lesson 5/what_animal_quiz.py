# Write a 'what animal are you' quiz. 
print("Welcome to the quiz, Answer the questions to find out what animal you are.")
print("All questions are yes/no, so answer with 'yes' or 'no'.")
# You can base this on the picture from last lesson, but make it simpler - 
# 3 questions and 4 animals.
first = input("Do you enjoy travel and adventure? ")
if first == 'yes':
    ay = input("Are you a people person? ")
    if ay == 'yes':
        print("You are a Seal")
    elif ay == 'no':
        print("You are a Duck")
    else:
        print("Please answer with 'yes' or 'no'.")
if first == 'no':
    bn = input("Are you energetic? ")
    if bn == 'yes':
        print("You are a Tiger")
    elif bn == 'no':
        print("You are a Koala")
    else:
        print("Please answer with 'yes' or 'no'.")
# Ask your user a question about themselves, giving them 2 options


# Check if they picked the first option

    # Ask the next question

    # Check if they picked the first option

        # Tell them they're animal 1

    # Otherwise

        # Tell them they're animal 2

# Otherwise

    # Ask the next question

    # Check if they picked the first option

        # Tell them they're animal 3

    # Otherwise

        # Tell them they're animal 4 

# __________________________

# EXTENSION
# Extend the quiz so there are 8 possible animals

# __________________________

# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.