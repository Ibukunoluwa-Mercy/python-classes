database = [
    {
        "fullname": "Tolulope",
        "email": "tolu@gmail.com",
        "password": "1234",
        "balance": 0
    }
]


def signup():
    print("\n--- CREATE ACCOUNT ---")
    fullname = input("Fullname: ").strip().capitalize()
    email = input("Email: ").strip().lower()
    password = input("Password: ").strip()

    if not fullname or not email or not password:
        print("All fields are required!")
        return

    for user in database:
        if user["email"] == email:
            print("Email already exists!")
            return

    new_user = {
        "fullname": fullname,
        "email": email,
        "password": password,
        "balance": 0
    }
    database.append(new_user)
    print("Account created successfully!")


def deposit(user):
    try:
        amount = float(input("Amount: ").strip())
        if amount < 1:
            print("Amount can not be less than 1")
        else:
            user["balance"] += amount
            print("Your new balance is:", user["balance"])
    except ValueError:
        print("Please enter a valid number!")


def withdraw(user):
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


def check_balance(user):
    print("Your current balance is:", user["balance"])


def home(user):
    while True:
        print(f"""
Welcome to MyBank, {user['fullname']}

1. Deposit
2. Withdraw
3. Check Balance
#. Logout
        """)
        choice = input("Choice: ").strip()
        if choice == "1":
            deposit(user)
        elif choice == "2":
            withdraw(user)
        elif choice == "3":
            check_balance(user)
        elif choice == "#":
            print("Logged out..")
            break
        else:
            print("Invalid input. Try again")


def login():
    print("\n--- LOG IN ---")
    email = input("Email: ").strip().lower()
    password = input("Password: ").strip()

    for user in database:
        if user["email"] == email and user["password"] == password:
            print("Login successful!")
            home(user)
            return

    print("Invalid email or password!")


def start():
    while True:
        print("""
Welcome to MyBank Auth

1. Sign Up
2. Log In
#. Exit
        """)
        choice = input("Choice: ").strip()
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "#":
            exit("Goodbye..!")
        else:
            print("Invalid input. Try again")


if __name__ == "__main__":
    start()