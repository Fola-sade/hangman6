import random
def check_guess(guess, word):
    guess = guess.lower()

    if guess in word:  # Check if the guess is in the secret word
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(word):
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            if guess in word:  # Step 1: Check if the guess is in the secret word
                print(f"Good guess! '{guess}' is in the word.")  # Step 2: If guess is correct, print a success message
            else:
                print(f"Sorry, '{guess}' is not in the word. Try again.")  # Step 3: If guess is incorrect, print an error message
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Secret word chosen by the computer
word = random.choice(["apple", "banana", "cherry", "date", "elderberry"])

# Start the game by calling ask_for_input
ask_for_input(word)
