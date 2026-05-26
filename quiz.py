#Animal quiz

score=0
print("Welcome to the animal quiz!")

#Question 1
answer1 = input("What is the largest land animal? ")
if answer1.lower().strip() == "elephant":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer was elephant")

#Question 2
answer2 = input("What is the largest reptile? ")
if answer2.lower().strip() == "crocodile":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer was crocodile")

#Question 3
answer3 = input("What is the largest mammal? ")
if answer3.lower().strip() == "blue whale":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer was blue whale")

#Question 4
answer4 = input("What is the largest bird? ") 
if answer4.lower().strip() == "ostrich":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer was ostrich")

#Question 5
answer5 = input("What is the strongest animal relative to its size? ")
if answer5.lower().strip() == "dung beetle":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer was dung beetle")

#Question 6
answer6 = input("What is the fastest land animal? ")
if answer6.lower().strip() == "cheetah":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer was cheetah")

#Question 7
answer7 = input("What animal has 3 hearts? ")
if answer7.lower().strip() == "octopus" or answer7.lower().strip() == "squid" or answer7.lower().strip() == "cuttlefish":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer was octopus, squid or cuttlefish")

print(f"Your final score is: {score}/7")
print("Thank you for playing the animal quiz!")
