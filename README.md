# 🎂 Age and Day Calculator

## 📌 Project Description

The **Age and Day Calculator** is a simple Python GUI-based application developed using the Tkinter library. This application allows users to calculate their current age, find the day of the week on which they were born, and calculate the total number of days they have lived.

Users can enter their date of birth (day, month, and year), and the application automatically calculates the results based on the current date.

This project is designed for beginners to understand Python programming, GUI development, date calculations, and basic error handling.

## ✨ Features

- **Age Calculation:** Calculates the user's current age in years.
- **Birth Day Finder:** Identifies the day of the week on which the user was born (Monday, Tuesday, etc.).
- **Total Days Calculation:** Calculates the total number of days the user has lived.
- **User-Friendly Interface:** Provides a simple and easy-to-use graphical interface.
- **Calculate Button:** Calculates the age and other date information.
- **Clear Button:** Clears all input fields and resets the result.
- **Date Validation:** Displays an error message if the user enters an invalid date.

## 🛠️ Technologies Used

- **Python:** Main programming language.
- **Tkinter:** Used to create the graphical user interface (GUI).
- **Datetime:** Used to work with dates and calculate age.
- **Calendar:** Used to find the weekday of the user's birth date.

## 📂 Project Structure

```text
Age-and-Day-Calculator/
│
├── age_calculator.py
│
└── README.md
```

## ⚙️ Requirements

To run this project, you need:

- Python 3.x installed on your computer.
- Tkinter library (usually included with standard Python installations).

No additional third-party libraries are required.

## 🚀 How to Run the Project

Follow these steps to run the application:

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code or any Python editor.
3. Make sure Python is installed.
4. Open the terminal.
5. Run the following command:

```bash
python age_calculator.py
```

6. The Age and Day Calculator window will appear.
7. Enter your date of birth:
   - Date
   - Month
   - Year
8. Click the **CALCULATE AGE** button.
9. Your age, birthday, and total lived days will be displayed.
10. Click the **CLEAR** button to reset the application.

## 📖 How It Works

The application uses Python's built-in date and calendar modules.

- The `date()` function creates a valid date of birth.
- `date.today()` gets the current date.
- Age is calculated by comparing the birth date with today's date.
- The `weekday()` function identifies the birth weekday.
- The `calendar.day_name` function converts the weekday number into its name.
- Date subtraction calculates the total number of days lived.

## 🖥️ Application Interface

The application includes:

- A dark blue background.
- A title: Age and Day Calculator.
- Three input fields for date, month, and year.
- An orange Calculate Age button.
- A Clear button.
- A result section displaying calculated information.

## 🎯 Learning Objectives

Through this project, I practiced:

- Python fundamentals.
- Creating GUI applications with Tkinter.
- Using Python modules.
- Working with dates and time.
- Performing mathematical calculations.
- Handling user input.
- Basic exception handling.
- Designing interactive applications.

## 🔮 Future Improvements

Possible future improvements include:

- Adding months and days to the age calculation.
- Improving the graphical interface.
- Adding input validation with more specific error messages.
- Displaying the next birthday countdown.
- Adding a more attractive and modern design.

## 👩‍💻 Author

**Mahrukh Fatima**

Python Beginner | Graphic Designer | QA Testing Learner

## 📜 License

This project is created for educational and learning purposes. You are welcome to explore and learn from the source code.
