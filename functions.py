"""skills-1/functions.py

Complete each of the prompts below.
"""

##
# Write a function called get_hometown that returns the name of your
# hometown as a string. NOTE: your function *must* have the name,
# get_hometown *exactly* or you won't pass the tests!
##

# Replace this with your code


##
# Complete the function below. It should take in 2 arguments: a first
# name and a last name. Then, it should return a full name (ex. Balloon Icorn)
#
# Don't forget the docstring!
##


def get_full_name():
    pass  # Replace this line with your code


##
# Complete the function so it prints a different greeting, depending on
# whether or someone comes from your hometown. It should take in a first
# name, last name, and a hometown (all 3 args are strings).
#
# If the person is from your hometown, print
#     Hi <full name>, we're from the same place!
#
# Otherwise, print
#     Hi <full name>, I'd like to visit <town name>!
#
# Examples: (assume my hometown is San Francisco)
#     - "Fido", "Bark", "Oakland" -> Hi Fido Bark, I'd like to visit Oakland!
#     - "Mel", "M", "San Francisco" -> Hi Mel M, we're from the same place!
##


def output_greeting():
    pass  # Replace this line with your code


##
# Complete the function below so it generates a list with the specified
# length.
#
# It should take in at least 1 argument --- the length of the list they
# want to create as an integer.
#
# The user can pass in a 2nd argument if they want to fill the list with
# a specific value. For ex., here's a 5-item list that's filled
# with 100s: [100, 100, 100, 100, 100]
#
# Otherwise, just populate the list with None. For ex., here's a 5-item
# list: [None, None, None, None, None]
##


def get_filled_list():
    pass  # Replace this line with your code


##
# Complete the function so it detects if something is a berry.
#
# It should take in 1 argument, a string, and return True if it's the name
# of a berry.
#
# A berry is anything with the word "berry" in it. Ex.: "strawberry",
# "catberry", "hi berry", "!!!! berry !!!!" all count as berries.
##


def is_berry():
    pass  # Replace this line with your code


"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

# Write your function here


##
# Complete the function below. It should take in a list as well as
# 0 or more *additional* arguments.
#
# The function should add all those items to the end of the list and return
# a new list. For example:
#
# >>> list_extender([1], 500, "hi", None)
# [1, 500, "hi", None]
# >>> list_extender([1, 2, 3])
# [1, 2, 3]
#
# We haven't taught you how to do this (at least, not explicitly) so this
# is your chance to test your googling abilities! You'll need to do some
# research on your own --- find a way to write a Python function that can
# take in an arbitrary amount of arguments.
##


def list_extender():
    pass  # Replace this line with your code


##
# Complete the function below so that it takes in a word and returns a tuple.
# You'll do this in an interesting way though, so make sure you read these
# directions thoroughly.
#
# First, the return value should be a tuple with 2 items in it ---
# the given word and a string that's the word 3 times. Ex.: if the word is
# "hi", then wordx3 is "hihihi"
#
# But here's how you need to do it:
#
# Your function will create an *inner* function. The *inner* function
# will return wordx3. Then, call the *inner* function when you create the
# tuple. If the word is "hi", you should return ("hi", "hihihi")
##


def word_tripler():
    pass  # Replace this line with your code