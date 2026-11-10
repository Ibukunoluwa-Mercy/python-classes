class TodoApp:
    def __init__(self):
        self.database = []

    def add_todo(self):
        todo = input("Todo: ").strip().capitalize()
        if not todo:
            print("Todo can not be empty!")
            return
        self.database.append(todo)
        print("Todo Added..")

    def view_todos(self):
        if not self.database:
            print("No todo added!")
            return
        for no, item in enumerate(self.database, 1):
            print(f"{no}. {item}")

    def edit_todo(self):
        if not self.database:
            print("No todo added!")
            return
        
        self.view_todos()
        try:
            index = int(input("Enter the number to edit: ").strip()) - 1
            if 0 <= index < len(self.database):
                new_todo = input("New todo: ").strip().capitalize()
                if not new_todo:
                    print("Todo can not be empty!")
                    return
                self.database[index] = new_todo
                print("Todo Updated..")
            else:
                print("Invalid todo number!")
        except ValueError:
            print("Please enter a valid number!")

    def delete_todo(self):
        if not self.database:
            print("No todo added!")
            return
        
        self.view_todos()
        try:
            index = int(input("Enter the number to delete: ").strip()) - 1
            if 0 <= index < len(self.database):
                removed = self.database.pop(index)
                print(f"'{removed}' Deleted..")
            else:
                print("Invalid todo number!")
        except ValueError:
            print("Please enter a valid number!")

    def run(self):
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
                self.add_todo()
            elif choice == "2":
                self.view_todos()
            elif choice == "3":
                self.edit_todo()
            elif choice == "4":
                self.delete_todo()
            elif choice == "#":
                print("Bye..")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    app = TodoApp()
    app.run()