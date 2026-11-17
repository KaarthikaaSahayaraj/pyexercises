"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: # A list of product prices.
# 2. Process:Add all the product prices.
# 3. Out: The total shopping bill.
# 4. My function name, and why return rather than print:calculate_total()
# The name clearly explains its purpose.
# Return instead of print:
# Return sends the result back so it can be stored
# and reused in other calculations.

# Your code below
num1=3
num2=4
def addition(add):
    return sum(add)
result=addition([num1,num2])
result2=addition([2,3,5])
print(result2)
print(result)

def calculate_total(prices):
    return sum(prices)



print(calculate_total([100, 200, 300]))
print(calculate_total([50, 150]))
print(calculate_total([250, 350, 400]))


print(calculate_total([]))
empty_class = []


print("Empty Class Average:", calculate_total(empty_class))