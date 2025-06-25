import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for good strength."

    # All possible characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# User input
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Invalid input! Please enter a valid number.")
