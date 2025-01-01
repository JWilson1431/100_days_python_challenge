import random

#Lists to hold letters, numbers, symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator! Follow the prompts to generate your password.")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))


password = []
#Append the user chosen # of letters to the password
for item in range(0, num_letters):
    password.append(random.choice(letters))

#Append the user chosen # of symbols to the password
for item in range(0, num_symbols):
    password.append(random.choice(symbols))

#Append the user chosen # of numbers to the password
for char in range(0, num_numbers):
    password.append(random.choice(numbers))

#Shuffle the characters
random.shuffle(password)

final_password = ""
for char in password:
    final_password += char

print(f"Your password is: {final_password}")