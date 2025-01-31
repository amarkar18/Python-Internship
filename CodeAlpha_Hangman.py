import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "software", "engineer", "codealpha"]
    word = random.choice(words)
    word_length = len(word)
    guessed_word = ["_" for _ in range(word_length)]
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")
    print("".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        print(f"\nAttempts remaining: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

        print("Word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word correctly!")
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()
