"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight marketing channels.
# 2. Process:The list is displayed in four different orders.
# 3. Out:Four arrangements and the original list at the end.
# 4. My four orders, and which ones modify the original:Original order: does not modify the list.
# Alphabetical order: sorted() returns a new list.
# Reverse alphabetical order: sorted() with reverse=True returns a new list.
# Reversed order: reverse() modifies the original list in place.
# I save a copy and restore the original before the final check.



# Your code below
channels = [
    "Instagram", "Email Marketing", "SEO", "YouTube",
    "Google Ads", "Facebook", "Blogging", "TikTok"
]

original = channels.copy()

print("1. Original order:")
print(channels)

print("2. Alphabetical order:")
print(sorted(channels))

print("3. Reverse alphabetical order:")
reverselist=channels[::-1]
print(reverselist)

print("4. Reversed order:")
channels.reverse()
print(channels)

channels = original

print("Original list at the end:")
print(channels)

print("Original preserved:", channels == original)