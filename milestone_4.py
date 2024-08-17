import random
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        # Step 3: Initialise the attributes
        self.word = random.choice(word_list)  # Randomly choose a word from the word_list
        self.word_guessed = ['_'] * len(self.word)  # List with underscores for each letter in the word
        self.num_letters = len(set(self.word))  # Number of unique letters in the word
        self.num_lives = num_lives  # Number of lives the player starts with
        self.word_list = word_list  # The list of words
        self.list_of_guesses = []  # List to store the guesses that have been tried
    
    def check_guess(self, guess):
        # Convert the guessed letter to lowercase
        guess = guess.lower()

        # Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            
            # Loop through each letter in the word
            for index, letter in enumerate(self.word):
                # Check if the current letter matches the guess
                if letter == guess:
                    # Replace the corresponding "_" in word_guessed with the guessed letter
                    self.word_guessed[index] = guess
            
            # Reduce the num_letters by 1 for each unique correct guess
            self.num_letters -= 1
        else:
            # Reduce num_lives by 1
            self.num_lives -= 1
            
            # Print the appropriate messages
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Example usage:
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
game = Hangman(word_list)
game.ask_for_input()
