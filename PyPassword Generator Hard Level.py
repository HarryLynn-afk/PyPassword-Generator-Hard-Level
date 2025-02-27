import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the PyPassword Generator!")
while True:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    if nr_letters > len(letters):
          print("Your number is out of range! Please try again")
    else:
        break
while True:
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    if nr_symbols > len(symbols):
        print("Your number is out of range! Please try again")
    else:
        break
while True:
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    if nr_numbers > len(numbers):
        print("Your number is out of range! Please try again")
    else:
        break

# Hard level
random_letters = random.sample(letters,nr_letters)
random_symbols = random.sample(symbols,nr_symbols)
random_numbers = random.sample(numbers,nr_numbers)
passwords = random_letters + random_symbols + random_numbers

final_passwords = ""
random.shuffle(passwords)
for char in passwords:
    final_passwords += char
print(final_passwords)

