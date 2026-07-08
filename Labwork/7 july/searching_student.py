# Function to search student by roll number
def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"


# Main Program
students = {
    101: "Aman",
    102: "Priya",
    103: "Rahul",
    104: "Sneha",
    105: "Karan"
}

roll_no = int(input("Enter Roll Number: "))

result = search_student(students, roll_no)

print("Result:", result)







# output

# Enter Roll Number: 105
# Result: Karan