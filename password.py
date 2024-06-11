import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        chars = string.ascii_letters + string.digits
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level (low/medium/high): ").lower()

    if complexity not in ['low', 'medium', 'high']:
        print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        return

    password = generate_password(length, complexity)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
