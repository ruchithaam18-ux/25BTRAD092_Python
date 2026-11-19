def recursive_fibonacci(n):
    # Base cases: the first two numbers are 0 and 1
    if n <= 1:
        return n
    # Recursive step
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

num_terms = 10

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence ({num_terms} terms):")
    for i in range(num_terms):
        print(recursive_fibonacci(i), end=" ")