"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: asking input from the user of two integers stored in the variable x and y 
# 2. Process:using different arithmetic operators such as (+,-,*,/,%,**)
# 3. Out:print() function is used to display the result 
# 4. What happens when the second number is zero, and why: when the second number is zero the product of two numbers are zero but the division gives a zerodivisionerror


# Your code below
x= int(input("Enter number 1:"))
y= int(input("Enter number 2:"))
print("The 2 numebers are ",x," and",y)
print("The sum of the numbers"," ",x+y)
print("The difference between the two numbers"," ",x-y)
print("The product of the two numbers"," ",x*y)
print("The quotient of the two number"," ",x/y)
print("The exponent of ",x,"on",y,"is",x**y)
print("The remainder of the two numbers"," ", x%y)
