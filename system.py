# Question 1 — Student Management System

# Create a Student class.

# Features:

# name
# roll number
# marks (dictionary)

# Methods:

# add_marks(subject, marks)
# calculate_average()
# display_report()

# Use constructors.

# class Student:
#     def __init__(self,name,roll_number):
#         self.name = name
#         self.roll_number = roll_number 
#         self.marks = {}
    
#     def add_marks(self,subject,marks):
#         self.marks[subject] = marks 
#         print(f"Marks added for {subject} sucessfully!")
    
#     def calculate_average(self):
#         if len(self.marks) == 0:
#             print("Marks need to be added first.")
#         else:
#             average = sum(self.marks.values()) / len (self.marks)
#             print(f"Average Marks: {average}")

#     def display_report(self):
#         print(f"\n Student Name: {self.name}")
#         print(f"Student Roll Number: {self.roll_number}")
#         print(f"Marks: ")
#         for subject,marks in self.marks.items():
#             print(f"Subject: {subject} :: Marks: {marks}")
#         self.calculate_average()

# s1 = Student("Dipro", 37)
# s1.add_marks("Maths",100)
# s1.add_marks("Computer Science", 94)
# s1.add_marks("Logical Reasoning", 88)
# s1.display_report()

# making it menu driven 

class Student:
    def __init__(self,name,roll_number):
        self.name = name 
        self.roll_number = roll_number
        self.marks = {}
    
    def add_marks(self,subject,marks):
        self.marks[subject] = marks
        print(f"{marks} added for {subject} successfully.")
    
    def calculate_mean(self):
        if len(self.marks) == 0:
            print("Records need to be added")
        else:
            average = sum(self.marks.values()) / len(self.marks)
            print(f"Average Marks: {average}")
    
    def display_report(self):
        print(f"\n Student Name: {self.name}")
        print(f"Student Roll Number: {self.roll_number}")
        for subject,marks in self.marks.items():
            print(f"Subject: {subject}")
            print(f"Marks: {marks}")


name = input("Enter the name of the student: ")
roll_number = int(input("Enter the roll number of the student: "))

s = Student(name,roll_number)

while True:
    print("\n -------------STUDENT RESULT SYSTEM--------------")
    print("1. Add Marks")
    print("2. Calculate Average")
    print("3. Display Report")
    print("4. Exit")

    choice = input("Enter your choice: (1-4)")

    if choice == "1":
        subject = input("Enter the subject to add: ")
        marks = int(input("Enter the marks to add: "))
        if marks<0 and marks > 100:
            print("Marks out of range. Must be between 0-100.")
        else:
            s.add_marks(subject,marks)
    elif choice == "2":
        s.calculate_mean()
    elif choice == "3":
        s.display_report()
    elif choice == "4":
        print("Exiting the system......GoodBye!!")
        break
    else:
        print("Invalid Choice. Please Choose (1-4)")

        