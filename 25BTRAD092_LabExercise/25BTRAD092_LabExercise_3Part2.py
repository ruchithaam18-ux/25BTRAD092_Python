
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Square")
print("4. Area of Triangle")
print("5. Area of Parallelogram")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print(f"Area of Circle: {3.14 * r * r:.2f}")

elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print(f"Area of Rectangle: {l * b:.2f}")

elif choice == 3:
    s = float(input("Enter side: "))
    print(f"Area of Square: {s * s:.2f}")

elif choice == 4:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print(f"Area of Triangle: {0.5 * b * h:.2f}")

elif choice == 5:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print(f"Area of Parallelogram: {b * h:.2f}")

else:
    print("Invalid choice")
