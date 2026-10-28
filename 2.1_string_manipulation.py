"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the string is stored in the variable book 
# 2. Process:funtions strip(),title(),upper(),lower and replace() to transform the string
# 3. Out:
#.      strip()- removed leading and trailing  white spacea 
#       title()- Change the font in title format that is capitalize first letter of each word
#       upper()- capitalize every letter of the string 
#       lower()- writes all letter in small case 
#       replace()- replaced all the whitespace with "|" 
#.      repr()- returns the original for of the string 
# 4. My four transformations, and when each is useful: each are used to modify and display the fonts such as capitalizing and spliting without making iteration to the original string or variable 


# Your code below
book= " The invisible hand "
print("original....:",repr(book))
print("Using strip()","."*5,":",book.strip())
print("Using title())","."*5,":",book.title())
print("Using upper()","."*5,":",book.upper())
print("Using lower())","."*5,":",book.lower())
print("Using Replace()",".",":",book.strip().replace(" ","|"))
print("original....:",repr(book))