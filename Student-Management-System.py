class Student:
    def __init__(self, name, roll_no, student_id, marks):
        self.name = name
        self.roll_no = roll_no
        self.student_id = student_id
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Student ID:", self.student_id)
        print("Marks:", self.marks)
        print("Grade:", self.grade())


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i+1}")

    name = input("Name: ")
    roll_no = input("Roll No: ")
    student_id = input("Student ID: ")
    marks = int(input("Marks: "))

    students.append(Student(name, roll_no, student_id, marks))

print("\nSTUDENT RECORDS")

for student in students:
    student.display()