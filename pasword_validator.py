while True:
    password = input("Create a password: ")
    
    
    length_valid = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if length_valid and has_upper and has_lower and has_digit:
        print("Password is valid!")
        break
    else:
        print("Password must be at least 8 characters and contain:")
        if not length_valid:
            print("- At least 8 characters")
        if not has_upper:
            print("- At least one uppercase letter")
        if not has_lower:
            print("- At least one lowercase letter")
        if not has_digit:
            print("- At least one digit")