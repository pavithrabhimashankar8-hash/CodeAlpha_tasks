import random

def play_hangman():
    # --- Step 1: Predefine a list of words ---
    # According to simplified scope, using a small list of 5 words.
    words = ["python", "programming", "internship", "project", "codealpha"]
    
    # --- Step 2: Choose a random word ---
    word_to_guess = random.choice(words)
    
    # --- Step 3: Game Setup Variables ---
    # Create a string of underscores to represent the hidden word
    display_word = ["_" for _ in word_to_guess]
    
    # Store all correctly guessed letters
    correct_guesses = []
    
    # Store all incorrectly guessed letters
    incorrect_guesses = []
    
    # Set the maximum number of incorrect guesses allowed
    max_turns = 6
    turns_remaining = max_turns
    
    # State variable for the main game loop
    game_over = False

    # --- Step 4: Game Introduction ---
    print("\n--- Welcome to Hangman! ---")
    print("Try to guess the secret word.")
    print(f"The word has {len(word_to_guess)} letters.")
    print(f"You have {turns_remaining} turns (incorrect guesses allowed).")
    
    # --- Step 5: Main Game Loop ---
    while not game_over and turns_remaining > 0:
        # Display the current state of the game
        print("\n" + " ".join(display_word))
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Turns remaining: {turns_remaining}")

        # Get player input
        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter (a-z).")
            continue
        
        # Check if letter has already been guessed
        if guess in correct_guesses or guess in incorrect_guesses:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        # --- Step 6: Handle Correct Guesses ---
        if guess in word_to_guess:
            print(f"Yes! '{guess}' is in the word.")
            correct_guesses.append(guess)
            # Update the display word with the correct letter(s)
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    display_word[i] = guess
        
        # --- Step 7: Handle Incorrect Guesses ---
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses.append(guess)
            turns_remaining -= 1

        # --- Step 8: Check for Game Over Conditions ---
        
        # Check for a win: are all letters revealed?
        if "_" not in display_word:
            game_over = True
            print("\n" + " ".join(display_word)) # Show the final word
            print("\n*** Congratulations! You guessed the word! ***")
            print(f"It was '{word_to_guess}'.")

        # Check for a loss: are all turns gone?
        if turns_remaining == 0:
            print("\n--- Game Over ---")
            print("You have no turns left.")
            print(f"The word was '{word_to_guess}'.")

# --- Step 9: Start the game ---
if __name__ == "__main__":
    play_hangman()
    