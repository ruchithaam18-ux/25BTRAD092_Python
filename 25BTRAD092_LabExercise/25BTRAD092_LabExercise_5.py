# --- Prime Number Program ---
def is_prime(n):
    if n <= 1:
        return False
    # Only need to check for factors up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("--- Prime Number Checker ---")
try:
    num_to_check = int(input("Enter a number to check if it's prime: "))
    if is_prime(num_to_check):
        print(f"{num_to_check} is a prime number.\n")
    else:
        print(f"{num_to_check} is not a prime number.\n")
except ValueError:
    print("Invalid input. Please enter a whole number.\n")


# --- Factorial Program ---
def get_factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("--- Factorial Calculator ---")
try:
    fact_num = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {fact_num} is {get_factorial(fact_num)}.")
except ValueError:
    print("Invalid input. Please enter a whole number.")