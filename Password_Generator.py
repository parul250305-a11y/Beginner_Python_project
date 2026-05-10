import string
import random

def generate_password():
    length = int(input("Enter password length: "))
    
    # Character sets
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(chars) for i in range(length))
    
    print("Generated Password:", password)

if __name__ == "__main__":
    generate_password()
