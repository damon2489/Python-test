#Animal quiz
from py_compile import main
import random
#sets score to zero at start
score=0
print("Welcome to the animal quiz!")
print("You will be asked 14 questions about animals")

#dictionary with question and answer
questions = [
    {"question": "What is the largest land animal?", "answer": ["Elephant"]},
    {"question": "What is the largest reptile?", "answer": ["Crocodile"]},
    {"question": "What is the largest mammal?", "answer": ["Blue whale"]},
    {"question": "What is the largest bird?", "answer": ["Ostrich"]},
    {"question": "What is the strongest animal relative to its size?", "answer": ["Dung beetle", "Beetle"]},
    {"question": "What is the fastest land animal?", "answer": ["Cheetah"]},
    {"question": "What animal has 3 hearts?", "answer": ["Octopus", "Squid", "Cuttlefish"]},
    {"question": "What is the sleepiest animal?", "answer": ["Koala"]},
    {"question": "What is the only bird that can fly backwards?", "answer": ["Hummingbird"]},
    {"question": "What is the only mammal capable of flight?", "answer": ["Bat"]},
    {"question": "Out of the following 4 animals, which can hold their breath the longest underwater? A) Dolphin B) Orca C) Seal D) Sloth", "answer": ["D", "Sloth", "D) Sloth"]},
    {"question": "What animal laughs when tickled?", "answer": ["Rat"]},
    {"question": "What is the only animal to have cube shaped poop?", "answer": ["Wombat"]},
    {"question": "What mammal has the strongest bite force?", "answer": ["Hippopotamus", "Hippo"]}
]


#shuffles the question so they are in a random order every time
random.shuffle(questions)


#A loop that randomly goes through the questions and asks for an answer, adding one to the score if right, not adding anything if wrong.

for q in questions:
    user_answer = input(q["question"] + " ")
    if user_answer.lower().strip() in [str(a).strip().lower() for a in q["answer"]]:
        score += 1
        print("Correct!")
    else:
        print("Wrong")

#final score
print("Your final score is:", score, "out of", len(questions))


#checks if user wants to know answers
know_ans = input("Do you want to know the answers? (yes/no) ")
if know_ans.lower() == "yes":
    for q in questions:
        print(q["question"], "-", q["answer"])

print("Thanks for playing!")