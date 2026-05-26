print("Welcome to the product pricer, this program determines the price of a product")

#Asks the user questions so that the final price can be determined for a product.
cost_of_materials = float(input("What was the cost of materials? (answer in numbers) ").strip())
hours_of_labour = float(input("How many hours of labour? (answer in numbers) ").strip())
hourly_wage = float(input("What is the hourly wage for labour? (answer in numbers) ").strip())
profit_margin = float(input("What is the desired profit margin? (answer in percentage, don't write percentage sign) ").strip())
profit_margin = profit_margin / 100
#Calculates total cost for the product.

final_price = int(cost_of_materials + (hours_of_labour * hourly_wage) + ((cost_of_materials + (hours_of_labour * hourly_wage)) * (profit_margin)))

final_price = int(final_price)
profit_margin = int(profit_margin)

# sale price is when there is no profit margin.
sale_price = int(cost_of_materials + (hours_of_labour * hourly_wage))
# Normal price is just the final price, with all calculations included.
normal_price = final_price
# Inflated price is the final price with an additional 20% added to it.
inflated_price = (final_price * 1.20)

# printing the prices for the product.
print("The sale price for your product is: " + str(sale_price))
print("The normal price for your product is: " + str(normal_price))
print("The inflated price for your product is: " + str(inflated_price))
