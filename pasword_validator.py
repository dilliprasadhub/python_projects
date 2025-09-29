while True:
    password = input("Create a password: ")
    
    # Initialize validations
    length_valid = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    
    # Check each character
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True