

class Student:
    def __init__(self, roll, name, course):
        self.roll = roll
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.roll},{self.name},{self.course}"


class StudentManagementSystem:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")

        student = Student(roll, name, course)

        with open(self.filename, "a") as file:
            file.write(str(student) + "\n")

        print("Student Added Successfully")

    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                print("\n--- Student List ---")
                for line in file:
                    roll, name, course = line.strip().split(",")
                    print(f"Roll: {roll}, Name: {name}, Course: {course}")
        except FileNotFoundError:
            print(" No student record found")

    def search_student(self):
        roll_search = input("Enter Roll Number to Search: ")
        found = False

        with open(self.filename, "r") as file:
            for line in file:
                roll, name, course = line.strip().split(",")
                if roll == roll_search:
                    print(f" Found: {roll}, {name}, {course}")
                    found = True
                    break

        if not found:
            print(" Student Not Found")

    def delete_student(self):
        roll_delete = input("Enter Roll Number to Delete: ")
        lines = []
        found = False

        with open(self.filename, "r") as file:
            lines = file.readlines()

        with open(self.filename, "w") as file:
            for line in lines:
                roll, _, _ = line.strip().split(",")
                if roll != roll_delete:
                    file.write(line)
                else:
                    found = True

        if found:
            print(" Student Deleted Successfully")
        else:
            print(" Student Not Found")


def main():
    sms = StudentManagementSystem()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sms.add_student()
        elif choice == "2":
            sms.view_students()
        elif choice == "3":
            sms.search_student()
        elif choice == "4":
            sms.delete_student()
        elif choice == "5":
            print("👋 Exiting Program")
            break
        else:
            print("Invalid Choice")


main()
