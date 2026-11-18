"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - There are empty lines (after "grace hopper", after "GUIDO van rossum", and at the end).
# - Some lines start with extra spaces ("  alan TURING", "  linus torvalds").
# - Capitalisation is inconsistent: "ada LOVELACE", "grace hopper", "GUIDO van rossum".
# - One name has three words ("GUIDO van rossum"), so "last word = last name" is not
#   enough on its own. "van" is a particle that is part of the last name.
# - The names are not in any order.

# 1. In: names.txt, one name per line ("first last"), messy.
# 2. Process, problem by problem:
#    - Empty lines -> skipped.
#    - Extra spaces -> strip() on each line, and split() so double spaces don't matter.
#    - Capitalisation -> each word gets a capital first letter, except particles
#      like "van" and "de", which stay lowercase ("Guido van Rossum").
#    - Three-word name -> first word = first name, everything after it = last name.
#    - Order -> sorted by last name, ignoring particles (van Rossum is sorted under R).
#    names.txt is only opened for reading ("r"), so it is never modified.
# 3. Out: names_sorted.txt, one clean name per line, sorted by last name.
# 4. How I decide which word is the last name: the first word is the first name and all the
#    other words are the last name. For sorting I skip a leading particle (van, de, von...),
#    so "van rossum" is sorted as "rossum".
#    Check: names.txt has 10 lines, the output has 8 (the 2 blank lines are removed).
#    First = Margaret Hamilton, last = Alan Turing.


# Your code below
INPUT_FILE = "names.txt"
OUTPUT_FILE = "names_sorted.txt"
PARTICLES = ["van", "von", "de", "der", "da", "di", "le", "la"]


def clean_word(word):
    word = word.lower()
    if word in PARTICLES:
        return word
    return word.capitalize()


def sort_key(person):
    first, last_words = person
    words = list(last_words)
    while len(words) > 1 and words[0] in PARTICLES:
        words = words[1:]
    return (" ".join(words).lower(), first.lower())


people = []
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        words = line.split()          # removes spaces at start/end and between words
        if len(words) == 0:           # empty line
            continue
        if len(words) == 1:           # only one word: no last name, skip it
            print(f"Skipped (no last name): {line.strip()}")
            continue
        words = [clean_word(w) for w in words]
        first_name = words[0].capitalize()   # first name always has a capital letter
        last_name_words = words[1:]
        people.append((first_name, last_name_words))

people.sort(key=sort_key)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    for first_name, last_name_words in people:
        file.write(f"{first_name} {' '.join(last_name_words)}\n")

print(f"{len(people)} names written to {OUTPUT_FILE}")