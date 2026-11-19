
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\n--- Student {i + 1} ---")
    name = input("Enter student name: ").strip()

    while not name or name in students:
        print("Name cannot be empty or duplicated!")
        name = input("Enter student name: ").strip()

    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                break
            print("Marks must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number!")

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    students[name] = {"marks": marks, "grade": grade}

print("\n" + "=" * 54)
print("             STUDENT GRADE REPORT")
print("=" * 54)

print(f"{'No.':<6}{'Student Name':<24}{'Marks':>10}{'Grade':>10}")
print("-" * 54)

for i, (name, details) in enumerate(students.items(), 1):
    print(f"{i:<6}{name:<24}{details['marks']:>10.1f}{details['grade']:>10}")

print("=" * 54)

if students:
    average = sum(s["marks"] for s in students.values()) / len(students)
    highest = max(s["marks"] for s in students.values())
    toppers = [name for name, s in students.items()
               if s["marks"] == highest]
    passed = sum(1 for s in students.values() if s["marks"] >= 50)
    failed = len(students) - passed

    print("\n             CLASS PERFORMANCE")
    print("-" * 54)
    print(f"{'Total Students':<25}: {len(students)}")
    print(f"{'Class Average':<25}: {average:.2f}")
    print(f"{'Topper(s)':<25}: {', '.join(toppers)}")
    print(f"{'Highest Marks':<25}: {highest:.1f}")
    print(f"{'Students Passed':<25}: {passed}")
    print(f"{'Students Failed':<25}: {failed}")
    print(f"{'Pass Percentage':<25}: {passed / len(students) * 100:.1f}%")

print("=" * 54)
print("        Grading Completed Successfully!")
print("=" * 54)

