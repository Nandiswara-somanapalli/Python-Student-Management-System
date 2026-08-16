import json
from pathlib import Path

DATA_FILE = Path("students.json")


def load_students():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def get_student_id():
    while True:
        value = input("Enter student ID: ").strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a valid positive number.")


def add_student(students):
    student_id = get_student_id()

    if any(student["id"] == student_id for student in students):
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    branch = input("Enter branch: ").strip().upper()

    while True:
        try:
            age = int(input("Enter age: "))
            if 15 <= age <= 100:
                break
            print("Age must be between 15 and 100.")
        except ValueError:
            print("Please enter a valid age.")

    while True:
        try:
            marks = float(input("Enter marks (%): "))
            if 0 <= marks <= 100:
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    student = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n" + "-" * 75)
    print(f'{"ID":<8}{"Name":<22}{"Branch":<12}{"Age":<8}{"Marks":<10}')
    print("-" * 75)

    for student in students:
        print(
            f'{student["id"]:<8}'
            f'{student["name"]:<22}'
            f'{student["branch"]:<12}'
            f'{student["age"]:<8}'
            f'{student["marks"]:<10.2f}'
        )

    print("-" * 75)


def search_student(students):
    student_id = get_student_id()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print(f'ID     : {student["id"]}')
            print(f'Name   : {student["name"]}')
            print(f'Branch : {student["branch"]}')
            print(f'Age    : {student["age"]}')
            print(f'Marks  : {student["marks"]}%')
            return

    print("Student not found.")


def update_student(students):
    student_id = get_student_id()

    for student in students:
        if student["id"] == student_id:
            name = input(f'Enter new name [{student["name"]}]: ').strip()
            branch = input(f'Enter new branch [{student["branch"]}]: ').strip().upper()

            if name:
                student["name"] = name
            if branch:
                student["branch"] = branch

            age_input = input(f'Enter new age [{student["age"]}]: ').strip()
            if age_input:
                try:
                    age = int(age_input)
                    if 15 <= age <= 100:
                        student["age"] = age
                    else:
                        print("Invalid age. Old age kept.")
                except ValueError:
                    print("Invalid age. Old age kept.")

            marks_input = input(f'Enter new marks [{student["marks"]}]: ').strip()
            if marks_input:
                try:
                    marks = float(marks_input)
                    if 0 <= marks <= 100:
                        student["marks"] = marks
                    else:
                        print("Invalid marks. Old marks kept.")
                except ValueError:
                    print("Invalid marks. Old marks kept.")

            save_students(students)
            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student(students):
    student_id = get_student_id()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
