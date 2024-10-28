import random

def choose_word():
    # List of possible words for the game
    words = ["python", "hangman", "programming", "developer", "computer"]
    # Randomly select a word from the list
    return random.choice(words)

def display_hangman(tries):
    # Function to display the hangman based on the number of incorrect tries
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |
        """,
        """
           ------
           |    
           |    
           |    
           |    
           |
        """
    ]
    return stages[tries]

def play_hangman():
    # Main function to play the game
    word = choose_word()  # Choose a random word
    word_completion = "_" * len(word)  # Create a string of underscores for the word
    guessed = False  # Flag to check if the word has been guessed
    guessed_letters = []  # List to store guessed letters
    guessed_words = []  # List to store guessed words
    tries = 6  # Number of tries allowed

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()  # Get user input

        # Check if the input is a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        # Check if the input is the entire word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word. Try again.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please guess a letter or a word.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'.")

# Run the game
if __name__ == "__main__":
    play_hangman()