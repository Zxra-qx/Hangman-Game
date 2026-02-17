import random

# word list (you can add more if you want)
words = ["python", "github", "coding", "hangman", "programming", "student"]

# pick random word
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.\n")

# display blanks
display = []
for letter in secret_word:
    display.append("_")

# main game loop
while wrong_guesses < max_wrong and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Enter a letter: ").lower()

    # check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess.")
        print("Attempts left:", max_wrong - wrong_guesses, "\n")

# result
if "_" not in display:
    print("You won! The word was:", secret_word)
else:
    print("You lost. The word was:", secret_word)
