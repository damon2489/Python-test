#Animal quiz

score=0
print("Welcome to the animal quiz!")

questions = [
    {"question": "What is the largest land animal?", "answer": "Elephant"},
    {"question": "What is the largest reptile?", "answer": "Crocodile"},
    {"question": "What is the largest mammal?", "answer": "Blue whale"},
    {"question": "What is the largest bird?", "answer": "Ostrich"},
    {"question": "What is the strongest animal relative to its size?", "answer": "Dung beetle"},
    {"question": "What is the fastest land animal?", "answer": "Cheetah"},
    {"question": "What animal has 3 hearts?", "answer": "Octopus" or "Squid" or "Cuttlefish"},
    {"question": "What is the sleepiest animal?", "answer": "Koala"},
    {"question": "What is the only bird that can fly backwards?", "answer": "Hummingbird"},
    {"question": "What is the only mammal capable of flight?", "answer": "Bat"},
    {"question": "Out of the following 4 animals, which can hold their breath the longest underwater (answer with the letter)? A) Dolphin B) Orca C) Seal D) Sloth", "answer": "D"}
]

#Make a loop that randomly goes through the questions and asks for an answer, adding one to the score if right, not adding anything if wrong.
import random
random.shuffle(questions)

for q in questions:
    answer = input(q["question"] + " ")
    if answer.lower().strip() == q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong")

print("Your final score is:", score, "out of", len(questions))
# Asks if the user wants to play again
play_again = input("Would you like to play again? (yes/no) ")
if play_again.lower() == "yes":
    score = 0
    random.shuffle(questions)
    for q in questions:
        answer = input(q["question"] + " ")
        if answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong")
    print("Your final score is:", score, "out of", len(questions))
else:
    print("Thanks for playing!")