"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the variable x and y containing the user input value stirng and integer
# 2. Process:the input is asked to user and the value is then displayed using the print function 
# 3. Out:the values are displayed at the same time 
# 4. My two fields, and what I would do with them:two different values are created for the variable and x and y and print function is used to display the input values, this is used to extract value from the user and then perform operation on them and display the output using the print function .


# Your code below
x=input("Name of the product :")
y=int(input("Price the product:"))
print("The Price of",x,"is",y,"euros")
