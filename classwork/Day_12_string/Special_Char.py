#wap to count number special chracters in a given setence.

sentence = input("Enter a sentence: ")

numbers = 0
special = 0

for x in sentence:
    if x.isdigit():
        numbers = numbers + 1
    elif not x.isalpha() and not x.isspace():
        special = special + 1

print("Number of digits =", numbers)
print("Number of special characters =", special)