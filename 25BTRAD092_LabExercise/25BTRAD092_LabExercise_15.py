
import random

print("=" * 55)
print("DICE ROLLING SIMULATOR".center(55))
print("=" * 55)

frequency = {}
total_rolls = 0

while True:
    print("\n" + "=" * 45)
    print("DICE SIMULATOR MENU".center(45))
    print("=" * 45)
    print("1. Roll Dice")
    print("2. View Frequency Analysis")
    print("3. Reset Simulation")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        try:
            dice = int(input("Enter number of dice (1-10): "))
            trials = int(input("Enter number of rolls (1-10000): "))

            if not 1 <= dice <= 10 or not 1 <= trials <= 10000:
                print("Invalid number of dice or rolls!")
                continue

            # Start a new experiment
            frequency = {}
            total_rolls = trials

            print("\n" + "=" * 55)
            print("DICE ROLL RESULTS".center(55))
            print("=" * 55)

            print(f"{'Roll No.':<12}{'Dice Outcomes':<28}{'Total':>10}")
            print("-" * 55)

            for i in range(1, trials + 1):
                outcomes = [
                    random.randint(1, 6) for _ in range(dice)
                ]

                total = sum(outcomes)
                frequency[total] = frequency.get(total, 0) + 1

                if trials <= 20 or i <= 10:
                    result = ", ".join(map(str, outcomes))
                    print(f"{i:<12}{result:<28}{total:>10}")

            if trials > 20:
                print(f"... {trials - 10} more rolls completed")

            print("=" * 55)
            print("Simulation completed successfully!")

        except ValueError:
            print("Invalid input! Enter whole numbers only.")

    elif choice == "2":
        if total_rolls == 0:
            print("No simulation data! Roll dice first.")
            continue

        print("\n" + "=" * 60)
        print("DICE FREQUENCY ANALYSIS".center(60))
        print("=" * 60)

        print(
            f"{'Outcome':<12}"
            f"{'Frequency':>12}"
            f"{'Probability':>16}"
            f"{'Bar Chart':>20}"
        )
        print("-" * 60)

        for outcome in sorted(frequency):
            count = frequency[outcome]
            probability = count / total_rolls * 100
            bar = "*" * round(count / max(frequency.values()) * 15)

            print(
                f"{outcome:<12}"
                f"{count:>12}"
                f"{probability:>15.2f}%"
                f"  {bar}"
            )

        most_common = max(frequency.values())
        common_outcomes = [
            value for value, count in frequency.items()
            if count == most_common
        ]

        print("=" * 60)
        print(f"Total Rolls       : {total_rolls}")
        print(f"Most Frequent     : {common_outcomes}")
        print(f"Highest Frequency : {most_common}")
        print("=" * 60)

    elif choice == "3":
        frequency = {}
        total_rolls = 0
        print("Simulation data reset successfully!")

    elif choice == "4":
        print("\nThank you for using Dice Simulator!")
        break

    else:
        print("Invalid choice! Please try again.")
