# Employee Information System

employees = {}

# Input details of 3 employees
for i in range(3):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employees[emp_id] = {
        "Name": name,
        "Department": department,
        "Salary": salary
    }

# Display all employee details
print("\nEmployee Details:")
for emp_id in employees:
    print("Employee ID:", emp_id)
    print("Name:", employees[emp_id]["Name"])
    print("Department:", employees[emp_id]["Department"])
    print("Salary:", employees[emp_id]["Salary"])
    print()

# Search employee by ID
search_id = input("Enter Employee ID to search: ")

if search_id in employees:
    print("\nEmployee Found:")
    print("Name:", employees[search_id]["Name"])
    print("Department:", employees[search_id]["Department"])
    print("Salary:", employees[search_id]["Salary"])
else:
    print("Employee Not Found")

# Increase salary by 10%
for emp_id in employees:
    employees[emp_id]["Salary"] = employees[emp_id]["Salary"] * 1.10

print("\nSalary Increased by 10%")

# Display updated details
print("\nUpdated Employee Details:")
for emp_id in employees:
    print("Employee ID:", emp_id)
    print("Name:", employees[emp_id]["Name"])
    print("Department:", employees[emp_id]["Department"])
    print("Salary:", employees[emp_id]["Salary"])
    print()

# Display employees of a specific department
dept = input("Enter Department to search: ")

print("\nEmployees in", dept, "Department:")

found = False

for emp_id in employees:
    if employees[emp_id]["Department"] == dept:
        print("Employee ID:", emp_id)
        print("Name:", employees[emp_id]["Name"])
        print("Salary:", employees[emp_id]["Salary"])
        print()
        found = True

if found == False:
    print("No employee found in this department.")











# Output
""" Enter Employee ID: 18
Enter Employee Name: Ankesh Sharma
Enter Department: CSE
Enter Salary: 70000"""