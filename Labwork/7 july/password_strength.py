# Function to check password strength
def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False

    # Check each character
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    # Check all conditions
    if len(password) >= 8 and has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"


# Main Program
password = input("Enter Password: ")

result = check_password(password)

print(result)











# output

# Enter Password: hekklo7658
# Weak Password