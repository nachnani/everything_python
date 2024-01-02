class Student:
    def __init__(self,name1,age1,roll_number1):
        self.name = name1
        self.age = age1
        self.roll_number = roll_number1


class School:
    def __init__(self):
        self.students = []

    def add_student(self,name,age,roll_number):
        student = Student(name,age,roll_number)
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Roll_Number: {student.roll_number}")
            print("...........................")

    def edit_student(self,roll_number,new_name,new_age):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name = new_name
                student.age = new_age
                print("Student data has been updated successfully")
                return

    def delete_student(self,roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student {student.name} deleted successfully.")



#Creating school object
school = School()

while True:
    choice = input("Enter your choice: \n1) Add Student \n2) Display list of students \n3) Edit list \n4) Delete student \n5) Quit")
    if choice == "1":
        # Accepting data from the user to create a student object
        name = input("Enter name of the student: ")
        age = input("Enter age: ")
        roll_number = input("Enter roll number: ")

        school.add_student(name, age, roll_number)

    elif choice == "2":
        # Display list of students
        school.display_students()

    elif choice == "3":
        roll_number = input("Enter roll number which you want to edit: ")
        new_name = input("Enter a new name for the student: ")
        new_age = input("Enter new age for the student: ")

        school.edit_student(roll_number,new_name,new_age)

    elif choice == "4":
        roll_number = input("Enter roll number in which you want to delete: ")
        school.delete_student(roll_number)

    elif choice == "5":
        break

