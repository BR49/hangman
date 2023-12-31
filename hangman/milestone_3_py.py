# -*- coding: utf-8 -*-
"""milestone_3.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lxhDwgypai16ckMdmWGip9d3fc3NutDz
"""

import random

# Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["apple", "banana", "orange", "strawberry", "pineapple"]

# Assign the list to a variable called word_list.
word_list = favorite_fruits

# Create the random.choice method and pass the word_list variable into the choice method.
word = random.choice(word_list)

# Step 1: Define a function called check_guess.
def check_guess(guess):
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()

    # Step 3: Check if the guess is in the word.
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 1: Define a function called ask_for_input.
def ask_for_input():
    # Step 2: Create a while loop and set the condition to True.
    while True:
        # Ask the user to guess a letter and assign this to a variable called guess.
        guess = input("Guess a letter: ")

        # Check that the guess is a single alphabetical character.
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word.
            check_guess(guess)
            # If the guess passes the checks, break out of the loop.
            break
        else:
            # If the guess does not pass the checks, print an error message.
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call the ask_for_input function to test your code.
ask_for_input()

# Print out the randomly selected fruit.
print("Randomly selected fruit:", word)