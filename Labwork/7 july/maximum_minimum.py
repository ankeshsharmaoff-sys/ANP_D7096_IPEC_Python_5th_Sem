# Function to find the maximum number
def find_max(numbers):
    return max(numbers)


# Function to find the minimum number
def find_min(numbers):
    return min(numbers)


# Function to find the average
def find_average(numbers):
    return sum(numbers) / len(numbers)


# Main Program
numbers = []

# Accept 10 integers from the user
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Call the functions
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

# Display the results
print("\nList:", numbers)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Average:", average)








# output

# Enter number 1: 56
# Enter number 2: 77
# Enter number 3: 43
# Enter number 4: 23
# Enter number 5: 43
# Enter number 6: 65
# Enter number 7: 55
# Enter number 8: 55
# Enter number 9: 44
# Enter number 10: 65

# List: [56, 77, 43, 23, 43, 65, 55, 55, 44, 65]
# Maximum Value: 77
# Minimum Value: 23
# Average: 52.6