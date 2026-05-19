#  Water Usage Billing
# Goal: Charge $5/L, but apply a bulk rate ($4/L) if usage is MORE than 20L.

# Get and output total daily water cost
litres = float(input("Enter litres of water used today: "))

if litres > 20:
    cost = litres * 4
else:
    cost = litres * 5
   
print("Total Water Cost: $" , cost)

# Monthly cost
cont = input("Would you like to know the monthly cost based on this?")
if cont == "yes":
    m_cost = cost * 30
    print("Total Monthly Water Cost: $", m_cost)

print("--- End of Report ---")
