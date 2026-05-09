# PASSWORD GENERATOR BY JEBA CHRISTILDA.S

import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

print("\nSelect Password Complexity")
print("1. Digits Only")
print("2. Letters Only")
print("3. Letters and Digits")
print("4. Letters, Digits, and Symbols")

choice = input("Enter your choice: ")

if choice == '1':
    characters = string.digits

elif choice == '2':
    characters = string.ascii_letters

elif choice == '3':
    characters = string.ascii_letters + string.digits

elif choice == '4':
    characters = string.ascii_letters + string.digits + string.punctuation

else:
    print("Invalid choice!")
    exit()

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)
