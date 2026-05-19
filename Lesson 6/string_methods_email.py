# Create a student email creator that uses first and last name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
id_number = input("Enter your ID number: ")

# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)

first_name = first_name.strip().lower()
last_name = last_name.strip().lower()
id_number = id_number.strip()

# Output the final email address

print("Your email address is: " + last_name + first_name + id_number + "@fake.school.nz")

# --------------------------------

# EXTENSION
# Create a temporary password to output as well
# It should be their names in all uppercase and their id divided by 10
temp_password = first_name.upper() + last_name.upper() + str(int(id_number) // 10)  
print("Your temporary password is: " + temp_password)

# --------------------------------

# EXPERT
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf.wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user