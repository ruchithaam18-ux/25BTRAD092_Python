# MINI PROJECT 3: STUDENT ATTENDANCE TRACKER

students = []
threshold = 75.0


def find_student(roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def add_student():
    roll = input("Enter Roll Number: ").strip()

    if not roll or find_student(roll):
        print("Invalid or duplicate roll number!")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    students.append({
        "roll": roll,
        "name": name,
        "attendance": []
    })

    print("Student added successfully!")


def mark_attendance():
    roll = input("Enter Roll Number: ").strip()
    student = find_student(roll)

    if student is None:
        print("Student not found!")
        return

    status = input("Present or Absent (P/A): ").upper().strip()

    if status not in ("P", "A"):
        print("Invalid attendance status!")
        return

    student["attendance"].append(status)
    print("Attendance marked successfully!")


def update_attendance():
    roll = input("Enter Roll Number: ").strip()
    student = find_student(roll)

    if student is None:
        print("Student not found!")
        return

    if not student["attendance"]:
        print("No attendance records available!")
        return

    print("Total classes:", len(student["attendance"]))

    try:
        day = int(input("Enter class number to update: "))
    except ValueError:
        print("Invalid class number!")
        return

    if not 1 <= day <= len(student["attendance"]):
        print("Class number not found!")
        return

    status = input("New status (P/A): ").upper().strip()

    if status not in ("P", "A"):
        print("Invalid attendance status!")
        return

    student["attendance"][day - 1] = status
    print("Attendance updated successfully!")


def display_attendance():
    print("\n" + "=" * 80)
    print("STUDENT ATTENDANCE REPORT".center(80))
    print("=" * 80)

    print(
        f"{'Roll':<10}{'Student Name':<22}"
        f"{'Total':>8}{'Present':>10}"
        f"{'Absent':>10}{'Percentage':>12}"
        f"{'Status':>8}"
    )

    print("-" * 80)

    for student in students:
        total = len(student["attendance"])
        present = student["attendance"].count("P")
        absent = total - present
        percentage = (present / total * 100) if total else 0

        if total == 0:
            status = "N/A"
        elif percentage >= threshold:
            status = "ELIGIBLE"
        else:
            status = "LOW"

        print(
            f"{student['roll']:<10}"
            f"{student['name'][:21]:<22}"
            f"{total:>8}{present:>10}"
            f"{absent:>10}{percentage:>11.1f}%"
            f"{status:>8}"
        )

    print("=" * 80)


def low_attendance():
    print(f"\nSTUDENTS BELOW {threshold}% ATTENDANCE")
    print("-" * 50)

    found = False

    for student in students:
        total = len(student["attendance"])

        if total == 0:
            continue

        present = student["attendance"].count("P")
        percentage = present / total * 100

        if percentage < threshold:
            print(
                f"{student['name']:<25}"
                f"{percentage:.2f}%"
            )
            found = True

    if not found:
        print("No students below the threshold!")


def change_threshold():
    global threshold

    try:
        value = float(input("Enter new threshold (0-100): "))

        if 0 <= value <= 100:
            threshold = value
            print("Threshold updated successfully!")
        else:
            print("Threshold must be between 0 and 100!")

    except ValueError:
        print("Invalid input!")


while True:
    print("\n" + "=" * 45)
    print("STUDENT ATTENDANCE TRACKER".center(45))
    print("=" * 45)
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Update Attendance")
    print("4. Display Attendance Report")
    print("5. Students Below Threshold")
    print("6. Change Attendance Threshold")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        update_attendance()
    elif choice == "4":
        display_attendance()
    elif choice == "5":
        low_attendance()
    elif choice == "6":
        change_threshold()
    elif choice == "7":
        print("Thank you for using Attendance Tracker!")
        break
    else:
        print("Invalid choice! Try again.")
