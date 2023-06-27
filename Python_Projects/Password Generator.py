import random
import string

print("Welcome to a Password Generator")


nPos = int(input("Number of Passwords to generate: "))
nlen = int(input("Enter Password length: "))

print("\nPasswords Generated: ")

for pwd in range(nPos):
    passwords = ''
    for c in range(nlen):
        passwords += random.choice(string.ascii_letters + string.digits)
    print(passwords)