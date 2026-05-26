#Animal quiz

score=0
print("Welcome to the animal quiz!")

#Question 1
answer1 = input("What is the largest land animal? ")
if answer1.lower().strip() == "elephant":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 2
answer2 = input("What is the largest reptile? ")
if answer2.lower().strip() == "crocodile":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 3
answer3 = input("What is the largest mammal? ")
if answer3.lower().strip() == "blue whale":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 4
answer4 = input("What is the largest bird? ") 
if answer4.lower().strip() == "ostrich":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 5
answer5 = input("What is the strongest animal relative to its size? ")
if answer5.lower().strip() == "dung beetle":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 6
answer6 = input("What is the fastest land animal? ")
if answer6.lower().strip() == "cheetah":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 7
answer7 = input("What animal has 3 hearts? ")
if answer7.lower().strip() == "octopus" or answer7.lower().strip() == "squid" or answer7.lower().strip() == "cuttlefish":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 8
answer8 = input("What is the sleepiest animal? ")
if answer8.lower().strip() == "koala":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 9
answer9 = input("What is the only bird that can fly backwards? ")
if answer9.lower().strip() == "hummingbird":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 10
answer10 = input("What is the only mammal capable of flight? ")
if answer10.lower().strip() == "bat":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 11
answer11 = input("Out of the following 4 animals, which can hold their breath the longest underwater? A) Dolphin B) Orca C) Seal D) Sloth")

if answer11.lower().strip() == "d" or answer11.lower().strip() == "sloth" or answer11.lower().strip() == "d) sloth":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Final score out of the 11 questions
print(f"Your final score is: {score}/11")
if score >= 9:
    print("Excellent work! You are an animal expert!")
elif score >= 6:
    print("Good job! You have a good knowledge of animals!")
elif score >= 3:
    print("Better luck next time")

# sees if user wants to know the answers, tells them the answers if yes, if not, ends the quiz.
if score != 11:
    print("Would you like to know the answers to the questions you got wrong? (yes/no)")
    know_answers = input().lower().strip()
    if know_answers == "yes":
        print("Here are the correct answers:")
        print("1. Elephant")
        print("2. Crocodile")
        print("3. Blue whale")
        print("4. Ostrich")
        print("5. Dung beetle")
        print("6. Cheetah")
        print("7. Octopus, squid or cuttlefish")
        print("8. Koala")
        print("9. Hummingbird")
        print("10. Bat")
        print("11. D) Sloth")
    else: print("Ok")

#end of quiz
print("Thank you for playing the animal quiz!")
