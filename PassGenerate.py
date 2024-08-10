import random
import string

def generate_password(num_letters, num_symbols, num_numbers):
    # Generate random letters
    letters = random.choices(string.ascii_letters, k=num_letters)

    # Generate random symbols
    symbols = random.choices(string.punctuation, k=num_symbols)

    # Generate random numbers
    numbers = random.choices(string.digits, k=num_numbers)

    # Combine all the characters
    password_list = letters + symbols + numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    return password

print("Welcome to Password Generator")

while True:
    num_letters = int(input("How many letters would you like in your password? "))
    num_symbols = int(input("How many symbols would you like? "))
    num_numbers = int(input("How many numbers would you like? "))

    password = generate_password(num_letters, num_symbols, num_numbers)
    print("Generated Password:", password)

    another = input("Would you like to generate another password? (yes/no): ").strip().lower()

    if another != 'yes':
        print("Thank you for using the Password Generator. Goodbye!")
        break
