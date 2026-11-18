"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: one expense typed by the user: date, category, description, amount.
# 2. Process: each value is checked. If a value is not acceptable, the program says why
#    and asks again until it gets a good one. If expenses.csv does not exist yet (or is
#    empty), the header line is written first. The entry is then APPENDED, so earlier
#    entries are kept.
# 3. Out: expenses.csv (separator ;) with the columns date;category;description;amount
# 4. Why these columns, and what this file is for: I want to track my spending. "date" lets
#    me group by month, "category" lets me see where the money goes, "description" helps me
#    remember what it was, and "amount" is what I add up. With 200 rows I would get the
#    total per month and per category, and find the category I should cut down on.


# Your code below
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
COLUMNS = ["date", "category", "description", "amount"]
CATEGORIES = ["food", "transport", "rent", "bills", "shopping", "health", "other"]


def ask_date():
    while True:
        text = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
        if text == "":
            return datetime.today().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("  Not a valid date. Example: 2026-11-18")


def ask_category():
    while True:
        text = input(f"Category {CATEGORIES}: ").strip().lower()
        if text in CATEGORIES:
            return text
        print("  Please choose one of the categories in the list.")


def ask_description():
    while True:
        text = input("Description: ").strip()
        if text != "":
            return text
        print("  Description cannot be empty.")


def ask_amount():
    while True:
        text = input("Amount: ").strip().replace(",", ".")
        try:
            amount = float(text)
        except ValueError:
            print("  Please type a number, for example 12.50")
            continue
        if amount <= 0:
            print("  Amount must be greater than 0.")
            continue
        return f"{amount:.2f}"


def main():
    date = ask_date()
    category = ask_category()
    description = ask_description()
    amount = ask_amount()

    # First time: the file does not exist (or is empty), so it needs the header line
    need_header = not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0

    # "a" = append, so a second run adds a line instead of overwriting
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        if need_header:
            writer.writerow(COLUMNS)
        writer.writerow([date, category, description, amount])

    print(f"Saved to {FILE_NAME}")


main()
