"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two values written in the code: a = "Python" and b = "python"
#    (the same word, but the first one starts with a capital letter).
# 2. Process: Python compares them with ==, !=, <, >, <= and >=, then combines those
#    results with and, or and not. Each result goes into a list with its expression.
# 3. Out: a table on the screen, one line per expression with its result.
# 4. Which two values, and what surprised me: "Python" and "python". It surprised me that
#    "Python" < "python" is True. Python compares the letter codes, and capital P (80)
#    comes before small p (112). It also surprised me that "a and b" gives back 'python'
#    instead of True or False: "and" returns one of the values themselves.


# Your code below
a = "Python"
b = "python"

rows = [
    # comparisons
    ("a == b", lambda: a == b),
    ("a != b", lambda: a != b),
    ("a < b", lambda: a < b),
    ("a > b", lambda: a > b),
    ("a <= b", lambda: a <= b),
    ("a >= b", lambda: a >= b),
    ("a.lower() == b.lower()", lambda: a.lower() == b.lower()),
    # logical combinations
    ("(a == b) and (a < b)", lambda: (a == b) and (a < b)),
    ("(a == b) or (a < b)", lambda: (a == b) or (a < b)),
    ("not (a == b)", lambda: not (a == b)),
    ("(a < b) and (a != b)", lambda: (a < b) and (a != b)),
    ("a and b", lambda: a and b),
    ("a or b", lambda: a or b),
    ("not a", lambda: not a),
]

print(f"a = {a!r}   b = {b!r}")
print()
print(f"{'Expression':<26}Result")
print("-" * 40)
for text, check in rows:
    try:
        result = repr(check())
    except TypeError:
        result = "TypeError (cannot compare)"
    print(f"{text:<26}{result}")
