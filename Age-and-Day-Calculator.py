import tkinter as tk
from datetime import date
import calendar


def calculator():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entery.get())

        dob = date(y, m, d)
        today = date.today()

        age_years = today.year - y - ((today.month, today.day) < (m, d))
        total_days = (today - dob).days
        born_day = calendar.day_name[dob.weekday()]

        result.config(
            text=f"You are {age_years} years old\n"
                 f"You were born on a {born_day}\n"
                 f"You have lived {total_days} days"
        )

    except:
        result.config(
            text="Please enter correct date!\nEx: 15 5 2008"
        )


def clear():
    day_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    year_entery.delete(0, tk.END)
    result.config(text="Enter your date of birth")


# Window
win = tk.Tk()
win.title("Age and Day Calculator")
win.geometry("380x380")
win.config(bg="#0A2342")


tk.Label(
    win,
    text="AGE AND DAY CALCULATOR",
    font=("Arial", 20, "bold"),
    bg="#0A2342",
    fg="white"
).pack(pady=20)


tk.Label(
    win,
    text="Calculate your age and birth day",
    bg="#0A2342",
    fg="white"
).pack()


f = tk.Frame(win, bg="#0A2342")
f.pack(pady=20)


tk.Label(
    f,
    text="Date",
    bg="#0A2342",
    fg="white"
).grid(row=0, column=0, padx=10)

tk.Label(
    f,
    text="Month",
    bg="#0A2342",
    fg="white"
).grid(row=0, column=1, padx=10)

tk.Label(
    f,
    text="Year",
    bg="#0A2342",
    fg="white"
).grid(row=0, column=2, padx=10)


day_entry = tk.Entry(
    f,
    width=8,
    justify="center"
)
day_entry.grid(row=1, column=0, padx=10, pady=5)


month_entry = tk.Entry(
    f,
    width=8,
    justify="center"
)
month_entry.grid(row=1, column=1, padx=10, pady=5)


year_entery = tk.Entry(
    f,
    width=8,
    justify="center"
)
year_entery.grid(row=1, column=2, padx=10, pady=5)


tk.Button(
    win,
    text="CALCULATE AGE",
    bg="#E67E22",
    fg="white",
    font=("Arial", 12, "bold"),
    command=calculator
).pack(pady=10)


tk.Button(
    win,
    text="CLEAR",
    bg="#E67E22",
    fg="white",
    width=10,
    command=clear
).pack(pady=5)


result = tk.Label(
    win,
    text="Enter your date of birth",
    bg="#0A2342",
    fg="#2ECC71",
    font=("Arial", 10)
)
result.pack(pady=20)


win.mainloop()
