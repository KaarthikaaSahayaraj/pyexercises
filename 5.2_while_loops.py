"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The user enters Yes or No.
# 2. Process:The program keeps asking until the user enters Yes.
# 3. Out:The program displays the number of attempts.
# 4. My stop condition, my attempt limit, my summary:Stop when the user enters Yes.
# Maximum attempts: 3.
# The summary shows the total attempts and the result.
# Capital letters and extra spaces are accepted.



# Your code below
attempts = 0
answer = ""

while answer != "yes" and attempts < 3:
    answer = input("Do you want to continue? (Yes/No): ")
    answer = answer.strip().lower()
    attempts = attempts + 1

if answer == "yes":
    print("You chose to continue!")
else:
    print("Maximum attempts reached.")

print("Total attempts:", attempts)
print("Final answer:", answer)