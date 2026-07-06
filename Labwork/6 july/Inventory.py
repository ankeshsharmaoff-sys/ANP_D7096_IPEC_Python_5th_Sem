# Inventory Management System

inventory = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# Display inventory
print("Current Inventory:")
for product in inventory:
    print(product, ":", inventory[product])

# Add a new product
product = input("\nEnter new product name: ")
stock = int(input("Enter stock: "))
inventory[product] = stock

print("\nInventory After Adding Product:")
for product in inventory:
    print(product, ":", inventory[product])

# Update stock of an existing product
product = input("\nEnter product name to update: ")

if product in inventory:
    stock = int(input("Enter new stock: "))
    inventory[product] = stock
    print("Stock Updated Successfully.")
else:
    print("Product Not Found.")

print("\nInventory After Updating:")
for product in inventory:
    print(product, ":", inventory[product])

# Remove a product
product = input("\nEnter product name to remove: ")

if product in inventory:
    del inventory[product]
    print("Product Removed Successfully.")
else:
    print("Product Not Found.")

print("\nInventory After Removing Product:")
for product in inventory:
    print(product, ":", inventory[product])

# Display products having stock less than 20
print("\nProducts with Stock Less Than 20:")

for product in inventory:
    if inventory[product] < 20:
        print(product, ":", inventory[product])

# Display total number of items
total = 0

for product in inventory:
    total = total + inventory[product]

print("\nTotal Items Available =", total)










# Output
""""""Current Inventory:
Laptop : 15
Mouse : 40
Keyboard : 25
Monitor : 10

Enter new product name: Ankesh Sharma""""""