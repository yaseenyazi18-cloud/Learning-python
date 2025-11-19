import random
import string

def generatePasword(pass_len, uppercase, lowercase, numbers, symbols):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if not characters:
        print("Error: no characters found: ")

    password = ''.join(random.choice(characters) for ln in range(pass_len) )
    return password

try:
   pass_len = int(input("Enter length of password: "))
   lowercase = input("include Lowercase Yes/No: ").lower() == 'yes'
   uppercase = input("include Uppercase Yes/No: ").lower() == 'yes'
   numbers = input("include Numbers Yes/No: ").lower() == 'yes'
   symbols = input("include Symbols Yes/No: ").lower() == 'yes'
   res = generatePasword(pass_len, uppercase,lowercase, numbers, symbols)
   print("Password: ",res)
except ValueError as ve:
    print(ve)

