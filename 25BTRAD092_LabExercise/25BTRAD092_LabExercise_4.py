import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")


number_guessing_game()