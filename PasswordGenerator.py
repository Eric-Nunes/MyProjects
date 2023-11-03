import random
import string

def generate_password(length=12):
    # Define the character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_-+=<>?"

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password with the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    # Get the desired password length from the user
    try:
        password_length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        exit()

    if password_length < 8:
        print("Password length should be at least 8 characters.")
    else:
        # Generate and print the password
        password = generate_password(password_length)
        print("Generated Password:", password)
