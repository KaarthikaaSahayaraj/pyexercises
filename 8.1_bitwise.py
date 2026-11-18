"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. In: four permissions for a blog post, each stored as one bit:
#    VIEW = 0001, WRITE = 0010, EDIT_SEO = 0100, PUBLISH = 1000
# 2. Process:
#    - Combine VIEW and WRITE with |  (this is what a writer gets)
#    - Test whether PUBLISH is there with &
#    - Add PUBLISH with |
#    - Remove WRITE with & ~
# 3. Out: after each step, the value in binary and the names of the permissions it has.
# 4. What my permissions are about: who can do what with an SEO blog post at a web
#    company. VIEW = read the draft, WRITE = write the content, EDIT_SEO = change the
#    title/meta description/keywords, PUBLISH = put it live on the website.


# Your code below
VIEW = 0b0001
WRITE = 0b0010
EDIT_SEO = 0b0100
PUBLISH = 0b1000

NAMES = {VIEW: "VIEW", WRITE: "WRITE", EDIT_SEO: "EDIT_SEO", PUBLISH: "PUBLISH"}


def show(step, perms):
    names = [name for bit, name in NAMES.items() if perms & bit]
    print(f"{step:<32}{perms:04b}   {', '.join(names) or '(none)'}")


print(f"{'Step':<32}Bits   Permissions")
print("-" * 60)

# 1. Combine two permissions
perms = VIEW | WRITE
show("Writer = VIEW | WRITE", perms)

# 2. Test whether a third one is present
has_publish = (perms & PUBLISH) != 0
print(f"{'Can publish?':<32}{has_publish}")

# 3. Add it
perms = perms | PUBLISH
show("Add PUBLISH", perms)
print(f"{'Can publish now?':<32}{(perms & PUBLISH) != 0}")

# 4. Remove one
perms = perms & ~WRITE
show("Remove WRITE", perms)