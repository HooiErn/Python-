import random

def hangman(incorrect_guesses):
    hangman_visual = [
        """
        --------
        """,
        """
        --------
        O
        """,
        """
        --------
        O
        |
        """,
        """
        --------
        O
        /|
        """,
        """
        --------
        O
        /|\\
        """,
        """
        --------
        O
        /|\\
        /
        """,
        """
        --------
        O
        /|\\
        / \\
        """
    ]
    return hangman_visual[incorrect_guesses]

def hangman():
    word_list = ["numbers", "hangman", "microsoft", "university", "software", "internet", "database"]
    word_to_guess = random.choice(word_list).upper()
    hidden_word = ["_"] * len(word_to_guess)
    guessed_letters = set()
    max_incorrect_guesses = 6
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(display_hangman(incorrect_guesses))
    print(" ".join(hidden_word))

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses and "_" in hidden_word:
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    hidden_word[idx] = guess
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. {max_incorrect_guesses - incorrect_guesses} guesses remaining.")

        print(display_hangman(incorrect_guesses))
        print(" ".join(hidden_word))

    if "_" not in hidden_word:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you've run out of guesses. The word was {word_to_guess}.")

# Run the hangman game
hangman()
