import random

words = ['apple', 'banana', 'orange', 'grape', 'lemon']
word = random.choice(words)
word_letters = set(word)
guessed_letters = set()
incorrect_guesses = 0
max_incorrect = 6

# Replace with your predefined guesses for simulation
predefined_guesses = ['a', 'e', 'o', 'g', 'r', 'n', 'p', 'l', 'b']

print("Simulated Hangman Game")

for guess in predefined_guesses:
    if incorrect_guesses >= max_incorrect or not word_letters:
        break

    print("\nGuessed letters:", " ".join(sorted(guessed_letters)))
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word:", " ".join(display_word))
    print(f"Guess: {guess}")

    if guess in guessed_letters:
        print("Already guessed.")
        continue

    guessed_letters.add(guess)
    if guess in word_letters:
        word_letters.remove(guess)
        print(f"Correct!")
    else:
        incorrect_guesses += 1
        print(f"Wrong! {max_incorrect - incorrect_guesses} left.")

if not word_letters:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame over! The word was: {word}")
