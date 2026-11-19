a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor Division")
print("7. Power (Square)")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(f"Result: {a + b:.2f}")
elif choice == 2:
    print(f"Result: {a - b:.2f}")
elif choice == 3:
    print(f"Result: {a * b:.2f}")
elif choice == 4:
    print(f"Result: {a / b:.2f}")
elif choice == 5:
    print(f"Result: {a % b:.2f}")
elif choice == 6:
    print(f"Result: {a // b:.2f}")
elif choice == 7:
    print(f"Square of {a}: {a ** 2:.2f}")
    print(f"Square of {b}: {b ** 2:.2f}")
else:
    print("Invalid choice")