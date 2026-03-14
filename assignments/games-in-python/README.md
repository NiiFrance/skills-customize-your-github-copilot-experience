
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a playable Hangman game in Python using loops, conditionals, and string operations. By completing this assignment, you will practice managing game state and handling user input clearly and correctly.

## 📝 Tasks

### 🛠️	Create the Hangman Game Loop

#### Description
Implement the main game flow so a player can guess letters until they either reveal the secret word or run out of attempts.

#### Requirements
Completed program should:

- Randomly choose one word from the provided `words` list.
- Initialize game state variables such as guessed letters, incorrect guesses, and maximum allowed incorrect guesses.
- Repeatedly prompt the player to enter one letter at a time until the game ends.
- Display the current word progress after each turn using placeholders for unguessed letters (example: `_ _ n g m a n`).


### 🛠️	Handle Guess Validation and End Conditions

#### Description
Add logic to validate user input, update the game state for correct or incorrect guesses, and show a final game result.

#### Requirements
Completed program should:

- Reject invalid guesses (for example: empty input, more than one character, or non-letter characters) and ask again.
- Prevent duplicate guesses from changing the game state.
- Decrease remaining attempts only for new incorrect guesses.
- End with a clear win message if the word is guessed or a clear lose message if attempts are exhausted.
