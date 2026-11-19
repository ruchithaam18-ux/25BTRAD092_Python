
import csv
import os

FILENAME = "students.csv"
FIELDS = ["USN", "Name", "Branch", "Semester", "Marks"]


def load_students():
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_students(students):
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def find_student(students, usn):
    for student in students:
        if student["USN"].upper() == usn.upper():
            return student
    return None


def get_marks():
    while True:
        try:
            marks = float(input("Enter Marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100!")
        except ValueError:
            print("Enter a valid number!")


def add_student():
    students = load_students()

    usn = input("Enter Student USN: ").strip().upper()

    if not usn or find_student(students, usn):
        print("Invalid or duplicate USN!")
        return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch: ").strip()
    semester = input("Enter Semester (1-8): ").strip()

    if not name or not branch:
        print("Name and Branch cannot be empty!")
        return

    if not semester.isdigit() or not 1 <= int(semester) <= 8:
        print("Invalid semester!")
        return

    marks = get_marks()

    students.append({
        "USN": usn,
        "Name": name,
        "Branch": branch,
        "Semester": semester,
        "Marks": str(marks)
    })

    save_students(students)
    print("Student record saved successfully!")


def search_student():
    students = load_students()
    usn = input("Enter USN to search: ").strip()

    student = find_student(students, usn)

    if student:
        print("\n" + "=" * 45)
        print("STUDENT DETAILS".center(45))
        print("=" * 45)

        for key, value in student.items():
            print(f"{key:<15}: {value}")

        print("=" * 45)
    else:
        print("Student record not found!")


def update_student():
    students = load_students()
    usn = input("Enter USN to update: ").strip()

    student = find_student(students, usn)

    if not student:
        print("Student record not found!")
        return

    print("\nEnter new details (leave blank to keep old values)")

    name = input("New Name: ").strip()
    branch = input("New Branch: ").strip()
    semester = input("New Semester: ").strip()
    marks = input("New Marks: ").strip()

    if semester and (
        not semester.isdigit() or not 1 <= int(semester) <= 8
    ):
        print("Invalid semester! Update cancelled.")
        return

    if marks:
        try:
            value = float(marks)
            if not 0 <= value <= 100:
                print("Marks must be between 0 and 100!")
                return
        except ValueError:
            print("Invalid marks! Update cancelled.")
            return

    if name:
        student["Name"] = name
    if branch:
        student["Branch"] = branch
    if semester:
        student["Semester"] = semester
    if marks:
        student["Marks"] = str(float(marks))

    save_students(students)
    print("Student record updated successfully!")


def display_students():
    students = load_students()

    if not students:
        print("No student records available!")
        return

    print("\n" + "=" * 80)
    print("COLLEGE STUDENT RECORD MANAGEMENT".center(80))
    print("=" * 80)

    print(
        f"{'USN':<18}"
        f"{'Name':<20}"
        f"{'Branch':<15}"
        f"{'Semester':>10}"
        f"{'Marks':>12}"
    )
    print("-" * 80)

    for student in students:
        print(
            f"{student['USN']:<18}"
            f"{student['Name'][:19]:<20}"
            f"{student['Branch'][:14]:<15}"
            f"{student['Semester']:>10}"
            f"{float(student['Marks']):>12.1f}"
        )

    print("=" * 80)
    print(f"Total Students: {len(students)}")


def delete_student():
    students = load_students()
    usn = input("Enter USN to delete: ").strip()

    student = find_student(students, usn)

    if not student:
        print("Student record not found!")
        return

    students.remove(student)
    save_students(students)
    print("Student record deleted successfully!")


while True:
    print("\n" + "=" * 45)
    print("STUDENT DATA MANAGER".center(45))
    print("=" * 45)
    print("1. Add Student Record")
    print("2. Search Student Record")
    print("3. Update Student Record")
    print("4. Display All Students")
    print("5. Delete Student Record")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using Student Data Manager!")
        break
    else:
        print("Invalid choice! Please try again.")
