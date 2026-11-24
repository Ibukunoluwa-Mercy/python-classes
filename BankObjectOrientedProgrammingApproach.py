class BankApp:
    app_name = "MercyBank"

    def __init__(self):
        self.database = []

    def signup(self):
        print("\n--- CREATE ACCOUNT ---")
        fullname = input("Fullname: ").strip().capitalize()
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()

        if not fullname or not email or not password:
            print("All fields are required!")
            return

        for user in self.database:
            if user["email"] == email:
                print("Email already exists!")
                return

        user_data = {
            "fullname": fullname,
            "email": email,
            "password": password,
            "balance": 0
        }
        self.database.append(user_data)
        print("Account created successfully!")

    def login(self):
        print("\n--- LOG IN ---")
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()

        for user in self.database:
            if user["email"] == email and user["password"] == password:
                print("Login successful!")
                self.home(user)
                return

        print("Invalid email or password!")

    def deposit(self, user):
        try:
            amount = float(input("Amount: ").strip())
            if amount < 1:
                print("Amount can not be less than 1")
            else:
                user["balance"] += amount
                print("Your new balance is:", user["balance"])
        except ValueError:
            print("Please enter a valid number!")

    def withdraw(self, user):
        try:
            amount = float(input("Amount: ").strip())
            if amount < 1:
                print("Amount can not be less than 1")
            elif amount > user["balance"]:
                print("Insufficient funds")
            else:
                user["balance"] -= amount
                print("Your new balance is:", user["balance"])
        except ValueError:
            print("Please enter a valid number!")

    def check_balance(self, user):
        print("Your current balance is:", user["balance"])

    def home(self, user):
        while True:
            print(f"""
Welcome to {self.app_name}, {user['fullname']}

1. Deposit
2. Withdraw
3. Check Balance
#. Logout
            """)
            choice = input("Choice: ").strip()
            if choice == "1":
                self.deposit(user)
            elif choice == "2":
                self.withdraw(user)
            elif choice == "3":
                self.check_balance(user)
            elif choice == "#":
                print("Logged out..")
                break
            else:
                print("Invalid input. Try again")

    def start(self):
        while True:
            print(f"""
Welcome to {self.app_name}

1. Sign Up
2. Log In
#. Exit
            """)
            choice = input("Choice: ").strip()
            if choice == "1":
                self.signup()
            elif choice == "2":
                self.login()
            elif choice == "#":
                exit("Goodbye..!")
            else:
                print("Invalid input. Try again")


if __name__ == "__main__":
    my_bank = BankApp()
    my_bank.start()