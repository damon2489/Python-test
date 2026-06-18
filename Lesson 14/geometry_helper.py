"""
PROGRAM: Geometry Helper
This program helps to calculate the area and circumference of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing functions for calculating the area and circumference 
# taking the user input and returning it, 
# and calling each function based on user choice


# =====================================================================
# FUNCTIONS
# =====================================================================

# TODO ------->>>> Write a function here for calculating the area of a rectangle using passed values. 
def rectangle_area(length,width):
    area = length * width
    return area
# TODO ------->>>> Return the result.



# TODO ------->>>> Write a function here for calculating the circumference using passed values. 
def rectangle_perimeter(length,width):
    perimeter = 2 * (length + width)
    return perimeter
# TODO ------->>>> Return the result.

def display_result(message):
    print("\n------------------")
    print(message)
    print("------------------")

# Run the main program
def main():

    print("Welcome to the Geometry Helper for rectangles!\n")
    print("1. Area Calculator")
    print("2. Perimeter Calculator")

    length = int(input("What is the length of your rectangle?").strip())
    width = int(input("What is the width of your rectangle?").strip())

    choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

    # Trigger function based on user choice
    if choice == "1":
        
        # TODO ------->>>> Call the function for calculating area here and save it into variable 'area'
        area = rectangle_area(length, width)
        display_result(f"The area of your rectangle is {area} units².")

    elif choice == "2":

        # TODO ------->>>> Call the function for calculating perimeter here and save it into variable 'perimeter'
        perimeter = rectangle_perimeter(length, width)
        display_result(f"The perimeter of your rectangle is {perimeter} units.")

    else:
        print("Invalid choice. Exiting dashboard.")


# =====================================================================
# EXECUTION
# =====================================================================

main()