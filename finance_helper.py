"""
PROGRAM: Finance Helper Dashboard
This program helps to calulate different finacial values (discounts, gst)
"""

# =====================================================================
# FUNCTIONS
# =====================================================================

# TODO Create a function for calculating discount. 
# TODO Copy and paste all the relevent code from below (all of choice 1) into new function.
# TODO Write a comment above the function to explain what it does
# TODO Replace the copied code below with a function call.


# TODO Create a function for calculating gst. 
# TODO Copy and paste all the relevent code from below (all of choice 2) into new function.
# TODO Write a comment above the function to explain what it does
# TODO Replace the copied code below with a function call.


# TODO Create a main function for running the program.
# TODO Copy and paste all remaining code (including your new calls) into this function.
# TODO Replace the copied code below with a main function call.


# =====================================================================
# MAIN EXECUTION
# =====================================================================

# price
def price():
    price = input("What is the full price of the item? (number only)")
    try:
        price = float(price)
        return price    
    except:
            print("That's not a valid price")

    discount = input("What is the discount percentage? (number only)")
    try:
        discount = float(discount/100)
        return discount
    except:
        print("That's not a valid percentage")



print("📱 Welcome to the Finance Helper Dashboard 📱\n")
print("1. Discount Calculator")
print("2. GST Calculator")

choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

if choice == "1":
    while True:
         