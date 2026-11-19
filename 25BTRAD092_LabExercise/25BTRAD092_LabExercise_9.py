import string

print("=" * 50)
print("             FREQUENCY COUNTER")
print("=" * 50)

print("1. Word Frequency in a Sentence")
print("2. Element Frequency in a List")

choice = input("\nEnter your choice (1/2): ")

frequency = {}

if choice == "1":
    sentence = input("\nEnter a sentence: ").lower()
    sentence = sentence.translate(
        str.maketrans("", "", string.punctuation)
    )
    items = sentence.split()
    title = "WORD FREQUENCY REPORT"

elif choice == "2":
    items = input(
        "\nEnter list elements separated by spaces: "
    ).split()
    title = "ELEMENT FREQUENCY REPORT"

else:
    print("Invalid choice!")
    exit()

for item in items:
    frequency[item] = frequency.get(item, 0) + 1

print("\n" + "=" * 50)
print(title.center(50))
print("=" * 50)

print(f"{'No.':<6}{'Word / Element':<25}{'Frequency':>15}")
print("-" * 50)

for i, (item, count) in enumerate(frequency.items(), 1):
    print(f"{i:<6}{item:<25}{count:>15}")

print("=" * 50)

if frequency:
    highest = max(frequency.values())
    most_common = [
        item for item, count in frequency.items()
        if count == highest
    ]

    print("\n" + "FREQUENCY ANALYSIS".center(50))
    print("-" * 50)
    print(f"{'Total Elements':<25}: {len(items)}")
    print(f"{'Unique Elements':<25}: {len(frequency)}")
    print(f"{'Most Frequent':<25}: {', '.join(most_common)}")
    print(f"{'Highest Frequency':<25}: {highest}")
else:
    print("No elements entered!")

print("=" * 50)
print("       Frequency Counting Completed!")
print("=" * 50)
