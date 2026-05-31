
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python that uses loops, string handling, and user input to let players guess a hidden word before they run out of attempts.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create the game setup so the program randomly chooses a word from a fixed list and initializes the hidden word display.

#### Requirements
Completed program should:

- Use a predefined list of words and select one at random
- Initialize the word display as underscores for each hidden letter
- Track letters that have been guessed already
- Show the current progress to the player before each guess

### 🛠️ Game Loop and End Conditions

#### Description
Implement the Hangman game loop to process player guesses, update the display, and determine win or loss.

#### Requirements
Completed program should:

- Accept single-letter guesses from the player
- Reveal correct letters and keep incorrect guesses separate
- Decrease remaining attempts for wrong guesses
- End when the player guesses the word or runs out of attempts
- Display a win message if the player guesses the word or a lose message with the correct word otherwise
