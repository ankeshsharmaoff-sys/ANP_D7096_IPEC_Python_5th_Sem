# Input full name
name = input("Enter your full name: ")

first_name = ""

for ch in name:
    if ch == " ":
        break
    first_name += ch

print("First Name:", first_name)