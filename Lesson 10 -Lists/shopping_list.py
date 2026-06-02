# =====================================================================
# PROJECT: Shopping List & Budget Tracker
# GOAL: Practice adding items to lists and calculating data from them.
# =====================================================================

# INITIALIZE YOUR LISTS
# TODO: Create an empty list called 'shopping_cart' to hold item names.
# TODO: Create an empty list called 'price_list' to hold item prices.

print("Welcome to the Shopping List")
shopping_cart = [
        
]

price_list = [
        
]

# MAIN
# TODO Create an infinite while loop

    # Info for user
    # TODO Output info for user:
    # Current cart/shopping list
    # Current prices

    # TODO Output Options for user: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout
    # TODO Get user input (1-4) and save in variable
while True:
    print("Current shopping cart:", shopping_cart)
    print("Current prices:", price_list)
    print("Options: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout")
    user_option = input("Please enter an option (1-4): ")


    # -----------------------------------------------------------------
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
    # TODO Check if option 1
        # TODO Ask user for the name of the item
        # TODO Add it to shopping list
        # TODO Add user for price of item
        # TODO Change price into a float
        # TODO Add price to price list
    if user_option == '1':
            item_name = input("Enter the name of the item you want to add: ")
            shopping_cart.append(item_name)
            item_price = float(input("Enter the price of the item: "))
            price_list.append(item_price)

    # -----------------------------------------------------------------
    # OPTION 2: REMOVE ITEM 
    # -----------------------------------------------------------------
    # TODO Else check if option 2
        # TODO Ask user for the name of the item they want to remove
        # TODO Use .index() to get the index of the item and save in variable
        # TODO Remove the item from cart
        # TODO Remove the price (using its index) from the price list
    elif user_option == '2':
        item_name = input("Enter the name of the item you want to remove: ")
        if item_name in shopping_cart:
            index = shopping_cart.index(item_name)
            shopping_cart.pop(index)
            price_list.pop(index)
        else:
            print("Item not found in cart.")


    # -----------------------------------------------------------------
    # OPTION 3: CLEAR CART (Practice clearing a list)
    # -----------------------------------------------------------------
    # TODO Else check if option 3
        # TODO: Use the .clear() method on both lists to empty them out.
        # TODO Tell them their cart is empty.
    elif user_option == '3':
        shopping_cart.clear()
        price_list.clear()
        print("Your cart has been cleared.")

    # -----------------------------------------------------------------
    # OPTION 4: CHECKOUT
    # -----------------------------------------------------------------
    # TODO Else check if option 4
        total_cost = sum(price_list)
    elif user_option == '4':
            
        print(f"Your total cost is: ${total_cost:.2f}")
        print("Thank you for shopping with us!")
        break

        # TODO Display the results
        # TODO Exit the loop (to exit the program)
    

    # -----------------------------------------------------------------
    # NO OPTION
    # -----------------------------------------------------------------
    # TODO Otherwise
        # TODO Tell them that option isn't valid
    else:
        print("Invalid option. Please try again.")

# ====================================================================
# EXTENSION
# Add a budget to the list
# TODO Tell them if their cart is over budget
# TODO Recommend items to remove based on their price.

# =====================================================================
# EXPERT
# Change your program to use dictionaries so prices are connected to shopping items
# Display the cart in alphabetical order
# Add an option to display the cart in order of price.