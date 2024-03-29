import random
import string

def generate_password(length):
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        desired_length = int(input("Enter the desired password length: "))
        if desired_length <= 0:
            print("Please enter a positive integer for the password length.")
            return

        generated_password = generate_password(desired_length)
        print(f"Generated password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
