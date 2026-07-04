#wap to create a list of 20 number given by user ,ask the user to input any number ,if then nuumber is present in list then remove its all duplicate occurence

numbers = []

# Input 20 numbers
for i in range(20):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Original List:", numbers)

# Number to check
value = int(input("Enter number: "))

if value in numbers:
    first = numbers.index(value)   # First occurrence index

    for i in range(len(numbers) - 1, first, -1):
        if numbers[i] == value:
            numbers.pop(i)

    print("Duplicate occurrences removed.")
else:
    print("Number not found.")

print("Updated List:", numbers)