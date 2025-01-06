import string
import random


def generate_pass(length=None, uppercase=True, numbers=True, specialCharacters=True):
    password = []
    characters = string.ascii_lowercase
    if uppercase:
       characters += string.ascii_uppercase
       password.append(random.choice(string.ascii_uppercase))
    if numbers:
       characters += string.digits
       password.append(random.choice(string.digits))
    if specialCharacters:
       characters += string.punctuation
       password.append(random.choice(string.punctuation))
    password += random.choices(characters, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

length = int(input("Length of Pass: "))
password = generate_pass(length)
print(f"Password generated: {password}")
