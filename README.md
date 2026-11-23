
# PLP Python Week 8 - My Python Toolkit

## Project Description

My Python Toolkit is a menu-driven Python program that combines three useful tools into one application. The program allows users to perform basic mathematical calculations, manage a to-do list, and check numbers. The menu continues running until the user chooses to quit.

## Tools Included

### 1. Simple Calculator
The calculator allows users to perform addition, subtraction, multiplication, and division using two numbers. It also handles invalid inputs and prevents division by zero.

### 2. To-Do List
The to-do list allows users to add tasks, view their tasks, and remove tasks. It uses a Python list to store tasks while the program is running.

### 3. Number Checker
The number checker allows users to enter a whole number and determine whether it is positive, negative, or zero, and whether it is even or odd.

## Concepts Used

- Variables
- User input and output
- If, elif, and else statements
- While loops and for loops
- Lists and list methods
- Arithmetic operators
- Modulo operator
- F-strings
- Exception handling
- Comments

## Files Included

- `toolkit.py` - Contains the complete menu-driven Python program.
- `toolkit_plan.txt` - Contains the project plan and selected tools.
- `screenshots/` - Contains screenshots showing the menu and tools working.

## How to Run the Program

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or another Python editor.
4. Open the terminal in the project folder.
5. Run the following command:

   ```bash
   python toolkit.py
   ```

6. Select a tool from the displayed menu and follow the instructions.

## Screenshots

The `screenshots` folder contains evidence of the program working, including invalid menu choice handling and each tool running.

## Reflection

The hardest part of this project was combining all three tools into one menu-driven program while ensuring that the menu continued running after each tool was used. The bug that took the longest to fix was indentation and ensuring that each tool was correctly placed inside the main menu loop. I learned how to use lists to store and modify tasks while a program runs. I also improved my understanding of loops, conditionals, user input, and error handling. Testing each tool helped me identify mistakes and verify that the program worked as expected. The project helped me understand how different Python concepts can be combined into one practical application. If I had one more week, I would improve the to-do list by saving tasks permanently in a file so they would not disappear when the program closes.
