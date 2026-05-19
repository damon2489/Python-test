# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

print("Welcome to the roller coaster, please answer these questions truthfully to see if you can ride")
# Get input
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
heart_condition = input("Do you have a heart condition? (yes/no)").strip().lower() == "yes"
vip_pass = input("Do you have a VIP pass? (yes/no)").strip().lower() == "yes"


# Check conditions and output verdict
if vip_pass == True:
        print("You can ride the roller coaster!")

else:
    if height > 150 and age > 10 and heart_condition == False:
        print("You can ride the roller coaster!")
    else:
        print("You cannot ride the roller coaster.")


# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules





# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient