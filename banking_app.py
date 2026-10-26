def main():
    balance = 10000

    print("Welcome to Kiran Bank")
    print(f"Opening Balance: {balance}")

    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print(f"Current Balance: {balance}")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                if amount > 0:
                    balance += amount
                    print("Deposit successful.")
                    print(
                        f"Updated Balance: {int(balance) if balance.is_integer() else balance}"
                    )
                else:
                    print("Error: Deposit amount must be greater than 0.")
            except ValueError:
                print("Error: Invalid amount entered.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Error: Withdrawal amount must be greater than 0.")
                elif amount > balance:
                    print("Transaction failed: Insufficient balance.")
                    print(
                        f"Current Balance: {int(balance) if balance.is_integer() else balance}"
                    )
                else:
                    balance -= amount
                    print("Withdrawal successful.")
                    print(
                        f"Updated Balance: {int(balance) if balance.is_integer() else balance}"
                    )
            except ValueError:
                print("Error: Invalid amount entered.")

        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()