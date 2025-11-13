
class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        """Add money into the account and return the new balance."""
        self.balance += amount
        print(f"${amount} deposited successfully.")
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from the account and return the withdrawn amount."""
        if amount > self.balance:
            print("Insufficient funds!")
            return 0
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            return amount

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current balance: ${self.balance:.2f}")

if __name__ == "__main__":
    my_account = BankAccount("John", "Doe", 1001, "Savings", 1234, 0.0)

    my_account.deposit(96)

    my_account.withdraw(25)

    my_account.display_balance()
