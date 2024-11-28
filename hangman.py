import random

# List of words
word_list = ["python", "programming", "developer", "hangman", "keyboard", "laptop", "internet"]

# Function to display the hangman progress
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
              ---
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
              ---
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
              ---
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
              ---
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
              ---
        """,
        """
           -----
           |   |
           O   |
               |
               |
              ---
        """,
        """
           -----
           |   |
               |
               |
               |
              ---
        """
    ]
    return stages[tries]

# Function to play Hangman
def play_hangman():
    # Select a random word
    word_to_guess = random.choice(word_list).upper()
    word_display = ["_"] * len(word_to_guess)  # Display as underscores
    guessed_letters = []  # List of already guessed letters
    tries = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(" ".join(word_display))
    print("\n")

    while tries > 0 and "_" in word_display:
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    word_display[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            tries -= 1

        print(display_hangman(tries))
        print(" ".join(word_display))
        print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    if "_" not in word_display:
        print(f"Congratulations! You've guessed the word: {word_to_guess}")
    else:
        print(f"You've run out of tries. The word was: {word_to_guess}")

# Run the game
if __name__ == "__main__":
    play_hangman()
