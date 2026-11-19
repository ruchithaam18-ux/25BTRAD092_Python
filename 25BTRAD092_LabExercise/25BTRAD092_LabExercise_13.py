
class BankAccount:

    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount! Enter a positive value.")
            return

        self.__balance += amount
        self.__transactions.append(("Deposit", amount))
        print(f"Rs. {amount:.2f} deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount! Enter a positive value.")
        elif amount > self.__balance:
            print("Transaction Failed! Insufficient balance.")
        else:
            self.__balance -= amount
            self.__transactions.append(("Withdrawal", amount))
            print(f"Rs. {amount:.2f} withdrawn successfully!")

    def check_balance(self):
        print("\n" + "=" * 45)
        print("ACCOUNT BALANCE ENQUIRY".center(45))
        print("=" * 45)
        print(f"Account Number : {self.account_no}")
        print(f"Account Holder : {self.name}")
        print(f"Available Balance : Rs. {self.__balance:.2f}")
        print("=" * 45)

    def transaction_history(self):
        print("\n" + "=" * 50)
        print("TRANSACTION HISTORY".center(50))
        print("=" * 50)

        if not self.__transactions:
            print("No transactions available!")
        else:
            print(f"{'No.':<8}{'Type':<20}{'Amount (Rs.)':>18}")
            print("-" * 50)

            for i, (type_, amount) in enumerate(
                self.__transactions, 1
            ):
                print(f"{i:<8}{type_:<20}{amount:>18.2f}")

        print("=" * 50)


accounts = {}

while True:
    print("\n" + "=" * 50)
    print("BANK ACCOUNT MANAGEMENT SYSTEM".center(50))
    print("=" * 50)
    print("1. Create Bank Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Balance Enquiry")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        acc_no = input("Enter Account Number: ").strip()

        if not acc_no or acc_no in accounts:
            print("Invalid or existing account number!")
            continue

        name = input("Enter Account Holder Name: ").strip()

        if not name:
            print("Account holder name cannot be empty!")
            continue

        try:
            balance = float(input("Enter Initial Balance: Rs. "))

            if balance < 0:
                print("Initial balance cannot be negative!")
                continue

            accounts[acc_no] = BankAccount(
                acc_no, name, balance
            )
            print("Bank Account Created Successfully!")

        except ValueError:
            print("Invalid balance!")

    elif choice in ("2", "3", "4", "5"):
        acc_no = input("Enter Account Number: ").strip()

        if acc_no not in accounts:
            print("Account not found!")
            continue

        account = accounts[acc_no]

        if choice in ("2", "3"):
            try:
                amount = float(input("Enter Amount: Rs. "))

                if amount != amount or amount == float("inf") or amount == float("-inf"):
                    print("Invalid amount!")
                    continue

                if choice == "2":
                    account.deposit(amount)
                else:
                    account.withdraw(amount)

            except ValueError:
                print("Invalid amount! Enter a number.")

        elif choice == "4":
            account.check_balance()

        elif choice == "5":
            account.transaction_history()

    elif choice == "6":
        print("\nThank you for using Bank Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
