
# PLP Python Week 8 - My Python Toolkit

print("Welcome to My Python Toolkit!")

# Keep displaying the menu until the user chooses to quit
while True:
    print("\n===== MY PYTHON TOOLKIT =====")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # Tool 1: Perform basic mathematical calculations
    if choice == "1":
        print("\n--- SIMPLE CALCULATOR ---")

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            operation = input("Enter your operation (1-4): ")

            if operation == "1":
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")

            elif operation == "2":
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")

            elif operation == "3":
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")

            elif operation == "4":
                if num2 == 0:
                    print("Sorry, division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")

            else:
                print("Invalid operation. Please choose between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    # Tool 2: Manage tasks using a changing list
    elif choice == "2":
        tasks = []

        while True:
            print("\n--- TO-DO LIST ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Return to main menu")

            task_choice = input("Enter your choice (1-4): ")

            if task_choice == "1":
                new_task = input("Enter the task you want to add: ")
                tasks.append(new_task)
                print(f"Task '{new_task}' has been added successfully!")

            elif task_choice == "2":
                if len(tasks) == 0:
                    print("Your to-do list is currently empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif task_choice == "3":
                if len(tasks) == 0:
                    print("There are no tasks to remove.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    try:
                        task_number = int(input("Enter the task number to remove: "))

                        if 1 <= task_number <= len(tasks):
                            removed_task = tasks.pop(task_number - 1)
                            print(f"Task '{removed_task}' has been removed.")
                        else:
                            print("Invalid task number.")

                    except ValueError:
                        print("Please enter a valid number.")

            elif task_choice == "4":
                print("Returning to the main menu...")
                break

            else:
                print("Invalid choice. Please select between 1 and 4.")

    # Tool 3: Check whether a number is positive, negative, zero, even or odd
    elif choice == "3":
        print("\n--- NUMBER CHECKER ---")

        try:
            number = int(input("Enter a whole number: "))

            if number > 0:
                print(f"{number} is a positive number.")
            elif number < 0:
                print(f"{number} is a negative number.")
            else:
                print("The number is zero.")

            if number != 0:
                if number % 2 == 0:
                    print(f"{number} is even.")
                else:
                    print(f"{number} is odd.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Exit the program
    elif choice == "4":
        print("Thank you for using My Python Toolkit. Goodbye!")
        break

    # Handle invalid main menu choices
    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please select 1, 2, 3, or 4.")

