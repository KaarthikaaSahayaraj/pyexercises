"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the number of conversions for one campaign, typed by the user.
# 2. Process: the campaign budget (500 EUR) is divided by the number of conversions to get
#    the cost per conversion. If the input is a problem, the user gets a message and can
#    try again, up to 3 attempts. After that the program stops politely instead of crashing.
# 3. Out: "Cost per conversion: xx.xx EUR", or a clear message that explains what went wrong.
# 4. The two failures, and whether they deserve the same message:
#    - ValueError: the user typed something that is not a whole number ("abc", "2.5").
#      That is a TYPING mistake, so the message tells them how to type it correctly.
#    - ZeroDivisionError: the user typed 0. That is valid data, not a mistake: the
#      campaign really had 0 conversions. The message says there is no cost per
#      conversion because the budget brought no result.
#    So they should NOT get the same message. One means "type it again properly", the
#    other means "your number is right, but there is nothing to calculate".
#    An empty line also gets its own message ("you didn't type anything"), which is
#    clearer than the ValueError message.
#
# Why I catch each error separately instead of catching every error at once:
#    With a single "except Exception" (or a bare "except:"), every problem gets the same
#    vague message, so the user doesn't know whether they typed it wrong or whether the
#    campaign really had 0 conversions. It would also hide real bugs in my own code
#    (a typo in a variable name, for example) behind "invalid input", so I would never
#    find them. Catching ValueError and ZeroDivisionError separately gives the right
#    message for each case and lets any unexpected bug still show up.
#
# Number of attempts: 3. After 3 bad inputs the program says so and stops cleanly.
#
# Test results (my four runs):
#    25    -> Cost per conversion: 20.00 EUR, then the program ends normally.
#    0     -> "This campaign has 0 conversions..." and asks again (no crash).
#    abc   -> "'abc' is not a whole number..." and asks again (no crash).
#    empty -> "You didn't type anything..." and asks again (no crash).
#    3 bad inputs in a row -> "No valid number after 3 attempts. Stopping."


# Your code below
BUDGET = 500.00
MAX_ATTEMPTS = 3


def main():
    print(f"Campaign budget: {BUDGET:.2f} EUR")
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        attempts += 1

        try:
            text = input(f"Number of conversions (attempt {attempts}/{MAX_ATTEMPTS}): ").strip()
        except (EOFError, KeyboardInterrupt):     # Ctrl+C or Ctrl+Z: stop politely
            print("\nInput stopped. Exiting without a result.")
            return

        if text == "":
            print("  You didn't type anything. Please type a number, for example 25.")
            continue

        try:
            conversions = int(text)
            if conversions < 0:
                print("  Conversions can't be negative.")
                continue
            cost = BUDGET / conversions
        except ValueError:
            print(f"  '{text}' is not a whole number. Please type digits only, for example 25.")
        except ZeroDivisionError:
            print("  This campaign has 0 conversions, so there is no cost per conversion.")
            print("  The budget was spent with no result. Type another number to try again.")
        else:
            print(f"  Cost per conversion: {cost:.2f} EUR")
            return

    print(f"No valid number after {MAX_ATTEMPTS} attempts. Stopping.")


main()
