def add_todo(database):
    todo = input("Todo: ").strip().capitalize()
    if not todo:
        print("Todo can not be empty!")
        return database
    database.append(todo)
    print("Todo Added..")
    return database

def view_todos(database):
    if not database:
        print("No todo added!")
        return
    for no, item in enumerate(database, 1):
        print(f"{no}. {item}")

def edit_todo(database):
    if not database:
        print("No todo added!")
        return database
    
    view_todos(database)
    try:
        index = int(input("Enter the number to edit: ").strip()) - 1
        if 0 <= index < len(database):
            new_todo = input("New todo: ").strip().capitalize()
            if not new_todo:
                print("Todo can not be empty!")
                return database
            database[index] = new_todo
            print("Todo Updated..")
        else:
            print("Invalid todo number!")
    except ValueError:
        print("Please enter a valid number!")
    return database

def delete_todo(database):
    if not database:
        print("No todo added!")
        return database
    
    view_todos(database)
    try:
        index = int(input("Enter the number to delete: ").strip()) - 1
        if 0 <= index < len(database):
            removed = database.pop(index)
            print(f"'{removed}' Deleted..")
        else:
            print("Invalid todo number!")
    except ValueError:
        print("Please enter a valid number!")
    return database

def main():
    database = []
    print("Welcome to myTodo app")
    
    while True:
        print("""
1. Add todo
2. View todo
3. Edit todo
4. Delete todo
#. Exit
        """)

        choice = input("Choice: ").strip()
        
        if choice == "1":
            database = add_todo(database)
        elif choice == "2":
            view_todos(database)
        elif choice == "3":
            database = edit_todo(database)
        elif choice == "4":
            database = delete_todo(database)
        elif choice == "#":
            print("Bye..")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()