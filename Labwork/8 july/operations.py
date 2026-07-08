# from twodfigures import *

print("===== Geometry Calculator =====")
print("1. Square")
print("2. Circle")
print("3. Triangle")
print("4. Rectangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    side = float(input("Enter side: "))
    print("Area =", square_area(side))
    print("Perimeter =", square_perimeter(side))

elif choice == 2:
    radius = float(input("Enter radius: "))
    print("Area =", circle_area(radius))
    print("Circumference =", circle_perimeter(radius))

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))

    print("Area =", triangle_area(base, height))
    print("Perimeter =", triangle_perimeter(side1, side2, side3))

elif choice == 4:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    print("Area =", rectangle_area(length, breadth))
    print("Perimeter =", rectangle_perimeter(length, breadth))

else:
    print("Invalid Choice")