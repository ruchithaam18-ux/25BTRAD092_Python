
import os
import re

filename = "application.log"

# Create a sample log file if it does not exist
if not os.path.exists(filename):
    sample_logs = [
        "2026-11-05 09:00:00 INFO Application started",
        "2026-11-05 09:05:00 INFO User logged in",
        "2026-11-05 09:10:00 WARNING High memory usage",
        "2026-11-05 09:15:00 ERROR Database connection failed",
        "2026-11-05 09:20:00 INFO Data loaded successfully",
        "2026-11-05 09:25:00 ERROR File not found",
        "2026-11-05 09:30:00 WARNING Low disk space",
        "2026-11-05 09:35:00 INFO User logged out"
    ]

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(sample_logs) + "\n")

    print("Sample log file created successfully!")

print("\n" + "=" * 65)
print("APPLICATION LOG FILE ANALYZER".center(65))
print("=" * 65)

counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_messages = []
total_lines = 0

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines or all(not line.strip() for line in lines):
        print("Log file is empty!")

    else:
        print(f"File Name: {filename}")
        print("\n" + "LOG ENTRIES".center(65))
        print("-" * 65)

        for line in lines:
            line = line.strip()

            if not line:
                continue

            total_lines += 1
            print(line)

            # Match log level as a separate word
            match = re.search(r"\b(ERROR|WARNING|INFO)\b", line, re.I)

            if match:
                category = match.group(1).upper()
                counts[category] += 1

                if category == "ERROR":
                    error_messages.append(line)

        print("\n" + "=" * 65)
        print("LOG ANALYSIS SUMMARY".center(65))
        print("=" * 65)

        print(f"{'Log Category':<25}{'Occurrences':>15}")
        print("-" * 45)

        for category, count in counts.items():
            print(f"{category:<25}{count:>15}")

        print("-" * 45)
        print(f"{'Total Log Entries':<25}{total_lines:>15}")
        print(f"{'Categorized Entries':<25}{sum(counts.values()):>15}")

        print("\n" + "ERROR DETAILS".center(65))
        print("-" * 65)

        if error_messages:
            for i, message in enumerate(error_messages, 1):
                print(f"{i}. {message}")
        else:
            print("No errors detected!")

        print("\n" + "=" * 65)
        print("LOG ANALYSIS COMPLETED SUCCESSFULLY".center(65))
        print("=" * 65)

except FileNotFoundError:
    print("Error: Log file not found!")

except PermissionError:
    print("Error: Permission denied while reading file!")

except OSError as e:
    print("File error:", e)
