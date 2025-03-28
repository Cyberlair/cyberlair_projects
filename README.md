# Cyberlair Projects

A collection of Python projects.

## Projects
- `sum_numbers.py`: Takes 6 numbers from the user and prints their sum. Example: Input "1 2 3 4 5 6" outputs "21".
- `calculator.py`: Evaluates math expressions (e.g., 'tan(45)+2-3*sqrt(4)') and functions like 'sin(30)'. Supports long expressions (up to 12 terms), parentheses, exponentiation, square root, trigonometric functions, implicit multiplication (e.g., 'sin(30)2' as 'sin(30)*2'), standard precedence rules, and displays results with 6 decimal places. Example: Input "tan(45)+2-3*sqrt(4)" outputs "-3.000000", "sin(30)" outputs "0.500000".
- `number_guesser.py`: A number guessing game where the user guesses a random number between 0 and 111, with feedback on whether the guess is too high or too low, and tracks the number of guesses. Example: Guess "50" for number 42 outputs "Too high! Try a lower number.", correct guess outputs "Congratulations! You guessed the number: 42" and "It took you 3 guesses."
- `rock_paper_scissors.py`: An interactive rock, paper, scissors game where the user competes against the computer, with the option to play multiple rounds. Example: Input "rock" against computer's "scissors" outputs "Computer chose: scissors" and "You win!".
- `todo_list.py`: A to-do list manager that allows users to add, show, delete, or mark tasks as complete, with persistent storage in a file. Example: Input "add" and "Buy groceries" adds the task, "complete" and "1" marks it as done, "show" displays "1. [✔] Buy groceries".
- `text_analyzer.py`: Analyzes a text (entered in a single line) by counting words, letters, sentences, listing words repeated more than once, and finding all most frequent words (if tied) using NLTK. Example: Input "I love to code. I love coding!" outputs "Words repeated more than once: 'i' (used 2 times), 'love' (used 2 times)", "Most frequent word(s): 'i' (used 2 times), 'love' (used 2 times)", "Number of words: 7", "Number of letters: 19", "Number of sentences: 2", "Enter another text to analyze, or type 'q' to quit.".

## How to Run
1. Clone the repository: `git clone https://github.com/Cyberlair/cyberlair_projects.git`
2. Navigate to the project folder: `cd cyberlair_projects`
3. Run the program: `python sum_numbers.py` or `python calculator.py` or `python number_guesser.py` or `python rock_paper_scissors.py` or `python todo_list.py` or `python text_analyzer.py`

## Setup
- Requires Python 3.11 or higher.
- Install dependencies for `text_analyzer.py`: `pip install nltk`