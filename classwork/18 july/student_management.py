class Student:
    def accept_data(self):
        self.student_id = input("Enter Student ID : ")
        self.name = input("Enter Name : ")
        self.course = input("Enter Course : ")
        self.marks = int(input("Enter Marks : "))

    def display_data(self):
        print("\n------ Student Details ------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Marks      :", self.marks)

    def check_result(self):
        if self.marks >= 35:
            print("Result     : Pass")
        else:
            print("Result     : Fail")


# Create an object of Student class
student1 = Student()

# Call all methods
student1.accept_data()
student1.display_data()
student1.check_result()