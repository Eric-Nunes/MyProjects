import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main game loop
def hangman():
    attempts = 6
    word = choose_word()
    guessed_letters = []
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        display = display_word(word, guessed_letters)
        print(display)
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if display == word:
            print("Congratulations! You guessed the word:", word)
            print("You win!")
            return
    
    if attempts == 0:
        print("\nOut of attempts! The word was:", word)
        print("Game over. You lost.")

# Run the game
hangman()
