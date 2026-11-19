
import csv
import os

INPUT_FILE = "employees.csv"
OUTPUT_FILE = "payroll_report.csv"

# Sample payroll rates for academic demonstration
HRA_RATE = 0.20
DA_RATE = 0.10
PF_RATE = 0.12
TAX_RATE = 0.05

# Create sample employee CSV file
if not os.path.exists(INPUT_FILE):
    employees = [
        ["E101", "Ravi", "Manager", 50000],
        ["E102", "Ananya", "Developer", 40000],
        ["E103", "Rahul", "Designer", 30000],
        ["E104", "Priya", "Analyst", 35000]
    ]

    with open(INPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Designation", "Basic"])
        writer.writerows(employees)

    print("Sample employee CSV file created successfully!")

payroll = []
total_gross = 0
total_deductions = 0
total_net = 0

try:
    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required = {"ID", "Name", "Designation", "Basic"}

        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            print("Invalid CSV format!")
            raise ValueError("Missing required columns")

        for row in reader:
            try:
                emp_id = row["ID"].strip()
                name = row["Name"].strip()
                designation = row["Designation"].strip()
                basic = float(row["Basic"])

                if not emp_id or not name or not designation or basic < 0:
                    print("Skipping invalid employee record!")
                    continue

                # Salary calculations
                hra = basic * HRA_RATE
                da = basic * DA_RATE
                gross = basic + hra + da

                pf = basic * PF_RATE
                tax = gross * TAX_RATE
                deductions = pf + tax
                net = gross - deductions

                payroll.append({
                    "ID": emp_id,
                    "Name": name,
                    "Designation": designation,
                    "Basic": round(basic, 2),
                    "HRA": round(hra, 2),
                    "DA": round(da, 2),
                    "Gross": round(gross, 2),
                    "PF": round(pf, 2),
                    "Tax": round(tax, 2),
                    "Deductions": round(deductions, 2),
                    "Net": round(net, 2)
                })

                total_gross += gross
                total_deductions += deductions
                total_net += net

            except (ValueError, TypeError, AttributeError):
                print("Skipping invalid employee record!")

    if payroll:
        # Save payroll report to CSV
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=list(payroll[0].keys())
            )
            writer.writeheader()
            writer.writerows(payroll)

        # Display payroll report
        print("\n" + "=" * 88)
        print("EMPLOYEE PAYROLL MANAGEMENT SYSTEM".center(88))
        print("=" * 88)

        print(
            f"{'ID':<8}{'Employee Name':<18}"
            f"{'Basic':>12}{'Gross':>14}"
            f"{'Deductions':>17}{'Net Salary':>17}"
        )
        print("-" * 88)

        for emp in payroll:
            print(
                f"{emp['ID']:<8}"
                f"{emp['Name'][:17]:<18}"
                f"{emp['Basic']:>12.2f}"
                f"{emp['Gross']:>14.2f}"
                f"{emp['Deductions']:>17.2f}"
                f"{emp['Net']:>17.2f}"
            )

        print("=" * 88)
        print("PAYROLL SUMMARY".center(88))
        print("-" * 88)

        print(f"Total Employees       : {len(payroll)}")
        print(f"Total Gross Salary    : Rs. {total_gross:.2f}")
        print(f"Total Deductions      : Rs. {total_deductions:.2f}")
        print(f"Total Net Salary      : Rs. {total_net:.2f}")
        print(f"Average Net Salary    : Rs. {total_net / len(payroll):.2f}")

        highest = max(payroll, key=lambda x: x["Net"])
        print(f"Highest Paid Employee : {highest['Name']}")
        print(f"Highest Net Salary    : Rs. {highest['Net']:.2f}")

        print("=" * 88)
        print(f"Payroll report saved to '{OUTPUT_FILE}'")
        print("PAYROLL PROCESSING COMPLETED SUCCESSFULLY")

    else:
        print("No valid employee records found!")

except FileNotFoundError:
    print("Employee CSV file not found!")

except (OSError, ValueError) as e:
    print("Error:", e)
