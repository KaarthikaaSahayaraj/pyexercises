"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In:
# A list containing students' marks.

# 2. Process, function by function:
# Function 1: calculate_total() adds all the marks.
# Function 2: count_students() counts the students.
# Function 3: calculate_average() divides total by student count.
# Function 4: get_class_average() uses the first three functions.

# 3. Out:
# The average mark of the class.

# 4. The question my fourth function answers:
# What is the average mark of the class?
# Splitting the work into small functions makes each step easier to test.



# Your code below
def total(marks):
    return sum(marks)

def count_students(marks):
    return len(marks)

def class_average(total,count):
    return total/count

def get_class_average(marks):
    Total=total(marks)
    count=count_students(marks)
    average= class_average(Total,count)
    return average

print(total([10,20,30]))
print(count_students([10,30,40]))
print(class_average(40,4))

class_a = [80, 90, 70]
class_b = [60, 70, 80, 90]
class_c = [100, 90, 80]

print("Class A Average:", get_class_average(class_a))
print("Class B Average:", get_class_average(class_b))
print("Class C Average:", get_class_average(class_c))