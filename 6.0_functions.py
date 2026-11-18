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

# 1. In: the function receives one list of marketing channel names,
#    e.g. the list from exercise 4.0:
#    ["Instagram", "Email", "SEO", "YouTube", "Google Ads", "Facebook", "Blogs", "TikTok"]
# 2. Process: it counts how many channels in the list are social media platforms
#    (Instagram, Facebook, TikTok, YouTube), then divides by the total number of
#    channels and multiplies by 100. Names are compared in lowercase, so "instagram"
#    and "Instagram" both count. If the list is empty, there is nothing to divide,
#    so it returns None.
# 3. Out: the function RETURNS the percentage of the channel mix that is social media
#    (a float, e.g. 50.0), or None for an empty list.
# 4. My function name, and why return rather than print:
#    The function is called social_media_share. The name says what it gives back
#    (a share) and of what (social media), without reading the code.
#    Why it is useful: if a marketing plan relies too much on social media, one algorithm
#    change or one account ban can hurt the whole campaign. This number shows how
#    dependent a plan is on social platforms.
#
#    Why RETURN and not print:
#    print() only shows the value on the screen. After that the value is gone, and the
#    function itself gives back None, so the rest of the program can't use the result.
#    return hands the value back to the code that called the function, so I can store it,
#    compare it, round it or save it to a file. In this program I use the returned value
#    to flag any plan above 60% as "too dependent on social media". That check is only
#    possible because the function returns its result. Printing is a decision for the
#    caller, not for the function.
#
# CHECK: calling it with an empty list
#    My first version was "return count / len(channels) * 100". With [] it crashed with
#    ZeroDivisionError, because len([]) is 0.
#    That is NOT acceptable: one empty plan would stop the whole program. Returning 0
#    would also be wrong, because it would look like a real plan with no social media.
#    So the function returns None, which means "no channels, nothing to measure", and the
#    code that calls it displays "no channels in this plan".


# Your code below
SOCIAL_MEDIA = ["instagram", "facebook", "tiktok", "youtube"]


def social_media_share(channels):
    """Return the percentage of channels that are social media, or None if the list is empty."""
    if len(channels) == 0:
        return None
    count = 0
    for channel in channels:
        if channel.lower() in SOCIAL_MEDIA:
            count += 1
    return count / len(channels) * 100


# The list from exercise 4.0
channels = ["Instagram", "Email", "SEO", "YouTube",
            "Google Ads", "Facebook", "Blogs", "TikTok"]

# Three different plans built from those channels, plus an empty one for the check
plans = {
    "All channels (4.0 list)": channels,
    "Small team plan": ["Email", "SEO", "Blogs", "Instagram"],
    "Influencer plan": ["Instagram", "TikTok", "YouTube", "Email"],
    "Empty plan": [],
}

for name, plan in plans.items():
    share = social_media_share(plan)          # the function returns, it doesn't print
    if share is None:
        print(f"{name:<25} no channels in this plan")
    elif share > 60:
        print(f"{name:<25} {share:.1f}% social media  <- too dependent on social media")
    else:
        print(f"{name:<25} {share:.1f}% social media")