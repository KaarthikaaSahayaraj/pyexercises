"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A marketing campaign with five details.
# 2. Process:# Read a detail, change a detail, remove a detail,
# and display all the remaining details.
# 3. Out:# The updated campaign details.
# 4. My object, my five fields, and why those:# A marketing campaign.
# Name, channel, budget, duration, and audience.
# These details help plan a campaign.


# Your code below
campaign = {
    "name": "Summer Sale",
    "channel": "Instagram",
    "budget": 5000,
    "duration": "2 weeks",
    "target": "Young adults"
}

# Read
print(campaign["name"])

# Handle a missing field
print(campaign.get("location", "Field not found"))
# Accessing campaign["location"] directly causes a KeyError.

# Change
campaign["budget"] = 7000

# Remove
campaign.pop("duration")

# Display all fields
for key, value in campaign.items():
    print(key, ":", value)