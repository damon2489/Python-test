### Secret Agent Login
# Create a login process for a secret agent 

# Ask for the user's name and save it in a variable
name = input("What is your name? ")
# Ask for the password and save it in a variable
password = input("What is the password? ")

# Check if the password == 'Falcon'

if password == 'Falcon':

    # Ouput that access has been granted and welcome user using their name
    print("Access granted, " + name + "!")

    # Ask for the user's age and save it in a variable
    age = input("What is your age? ")

    # Change the age into an integer
    age = int(age)

    # If the user's age is under 13, tell them they are a spy in training
    if age < 13:
        print("You are a spy in training")
    # If their age is under 18, tell them they are a junior spy
    elif age < 18:
        print("You are a junior spy")
    # If their age is 18 or over, tell them they are a Field Agent
    else:
        print("You are a Field Agent")
    # Output a goodbye
    print("Good luck on your mission, " + name + "!")

else:
    print("Access denied")
# ___________________________
# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)
# ___________________________

# EXPERT (For those who already know python)

# Create a SPY ID GENERATOR
# Your user must login using the correct password to access the generator
# Use a bunch of questions to generate an id. Eg. If their name has 4 or fewer letters, their ID is a random fruit plus other logic...
