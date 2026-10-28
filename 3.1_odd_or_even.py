"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the user inputs the value or integer in the variable x 
# 2. Process: the operator // is used to check whether the number is odd or even It divides two numbers and returns the largest integer less than or equal to the result.
#    If function performs operations based on the condition if its true or false 
#.   if its true the operation is executed if false it moves to the elif or else statement 
# 3. Out: based on the satisfied statement and condition the operation is executed accordingly
# 4. What happens on 0, on a negative number, on a very large number:if its zero it returns saying its zero 
#    if its negative it is negative it returns negative and followed by odd or even 
#     very large number works the returns the same output.


# Your code below
x= int(input("enter a number:"))
if x==0:
    print("the number is zero")
elif x>0 and x//2==0 :
    print("The number",x,"is positive even number")
elif x<0 and x//2==0:
    print("The number",x,"is negative even number")
elif x>0 and x//2!=0 :
    print("The number",x,"is positive odd number")
else:
    print("The number",x,"is negative odd number")


