"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: three values typed by the user for a new marketing campaign:
#    a campaign code, a contact email and a budget in euros.
# 2. Process: each value is checked against its own rule (a regular expression).
#    re.fullmatch() is used, so the WHOLE value must match, not just a part of it.
#    All three are checked. If at least one fails, every problem is shown and nothing
#    is saved. If all three pass, they are appended to the CSV file (header written
#    only the first time).
# 3. Out: campaigns.csv (separator ;) with columns campaign_code;contact_email;budget_eur,
#    or a list of what to fix.
# 4. My three fields and their rules, in plain English:
#
#    CAMPAIGN CODE
#    Accept: the capital letters "CMP", a dash, exactly 4 digits (the year), a dash,
#            exactly 3 digits (the campaign number). Example: CMP-2026-001
#    Reject: lowercase "cmp", missing dashes, a 2-digit year, fewer or more digits,
#            any extra character before or after.
#
#    CONTACT EMAIL
#    Accept: a name part made of letters, digits, dots, underscores, plus or minus signs,
#            then exactly one @, then a domain made of letters/digits/dashes, with dots
#            between parts, ending with a dot and at least 2 letters (.com, .fr, .co.uk).
#    Reject: no @, spaces anywhere, a domain without an ending (name@example),
#            an ending with digits (name@example.c0m).
#    Borderline case: "name@example.co.uk" -> accepted, because real domains can have
#            several parts.
#
#    BUDGET (EUR)
#    Accept: a whole number from 1 to 999999 with no leading zero, optionally followed
#            by a dot and EXACTLY 2 decimals. Examples: 1500, 1500.50
#    Reject: 0, negative numbers, leading zeros (0050), one decimal (12.5),
#            a comma (1500,50), a currency sign (1500€), more than 6 digits.
#    Borderline case: "12.5" -> rejected on purpose, because money is always written
#            with 2 decimals, so 12.5 is probably a typing mistake.
#
#
# THE PATTERNS, EXPLAINED PIECE BY PIECE
#
# CODE_PATTERN = r"CMP-\d{4}-\d{3}"
#    CMP-      the exact text "CMP-" (capital letters only)
#    \d{4}     \d means one digit (0-9), {4} means exactly 4 of them -> the year
#    -         an exact dash
#    \d{3}     exactly 3 digits -> the campaign number
#
# EMAIL_PATTERN = r"[A-Za-z0-9._+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
#    [A-Za-z0-9._+-]   square brackets = "one character from this list":
#                      a capital letter, a small letter, a digit, . _ + or -
#    +                 one or more of those -> the name part (can't be empty)
#    @                 exactly one @ sign
#    [A-Za-z0-9-]+     one or more letters, digits or dashes -> first part of the domain
#    (\.[A-Za-z0-9-]+)*  a group: a dot followed by more letters/digits/dashes.
#                      \. means a real dot (a plain . means "any character").
#                      * means this group can appear 0 or more times -> e.g. ".co"
#    \.                a real dot before the ending
#    [A-Za-z]{2,}      at least 2 letters, letters only -> the ending (com, fr, uk)
#
# BUDGET_PATTERN = r"[1-9]\d{0,5}(\.\d{2})?"
#    [1-9]       the first digit must be 1 to 9 -> no leading zero, no 0 budget
#    \d{0,5}     then 0 to 5 more digits -> max 6 digits in total (999999)
#    (\.\d{2})?  a group: a real dot and exactly 2 digits.
#                ? means the group is optional -> "1500" and "1500.50" both pass
#
# There is no ^ at the start or $ at the end because re.fullmatch() already demands
# that the whole value matches.
#
#
# TESTS (one pass + two fails per field, 9 values in 3 runs):
#    Field    | Must pass              | Must fail #1        | Must fail #2
#    code     | CMP-2026-001           | cmp-2026-001        | CMP-26-1
#    email    | test.user@example.com  | test.user@example   | test user@example.com
#    budget   | 1500.50                | 0050                | 12.5
#    Result: all 9 behaved as expected. Run 1 saved, runs 2 and 3 saved nothing.
#
# SURPRISE: "a..b@example.com" (two dots in a row) is ACCEPTED, because the pattern
#    allows any number of dots in the name part. Real email addresses don't allow that,
#    so my email rule is a bit too loose. I keep it simple on purpose and accept this.


# Your code below
import csv
import os
import re

FILE_NAME = "campaigns.csv"
COLUMNS = ["campaign_code", "contact_email", "budget_eur"]

CODE_PATTERN = r"CMP-\d{4}-\d{3}"
EMAIL_PATTERN = r"[A-Za-z0-9._+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
BUDGET_PATTERN = r"[1-9]\d{0,5}(\.\d{2})?"


def main():
    code = input("Campaign code (example CMP-2026-001): ").strip()
    email = input("Contact email: ").strip()
    budget = input("Budget in EUR (example 1500 or 1500.50): ").strip()

    errors = []
    if not re.fullmatch(CODE_PATTERN, code):
        errors.append(f"Campaign code '{code}' must look like CMP-2026-001 (capital CMP, 4-digit year, 3 digits).")
    if not re.fullmatch(EMAIL_PATTERN, email):
        errors.append(f"Email '{email}' must look like name@domain.com (no spaces, one @, ends with .com/.fr/...).")
    if not re.fullmatch(BUDGET_PATTERN, budget):
        errors.append(f"Budget '{budget}' must be 1 to 999999, no leading 0, and either no decimals or exactly 2.")

    # Save only when ALL three are acceptable
    if errors:
        print("\nNot saved. Please fix:")
        for error in errors:
            print("  -", error)
        return

    need_header = not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        if need_header:
            writer.writerow(COLUMNS)
        writer.writerow([code, email, budget])
    print(f"\nAll three values are valid. Saved to {FILE_NAME}")


main()