import random

# Define a list of words
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Use random.choice to select a random word from the list
word = random.choice(word_list)
guess = input('Enter a single letter: ')
print(f"You entered: {guess}")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")