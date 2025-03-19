import random

number = random.randint(0, 111)
guesses = 0

print("Welcome to the Number Guesser Game!")
print("I'm thinking of a number between 0 and 111.")
print("Enter your guess, or 'q' to quit.")

while True:
    guess_input = input("Your guess: ").strip()
    if guess_input.lower() == 'q':
        print("Exiting game... The number was", number)
        break

    try:
        guess = int(guess_input)
    except ValueError:
        print("Please enter a valid number between 0 and 111, or 'q' to quit.")
        continue

    if guess < 0 or guess > 111:
        print("Please enter a number between 0 and 111.")
        continue

    guesses += 1

    if guess < number:
        print("Too low! Try a higher number.")
    elif guess > number:
        print("Too high! Try a lower number.")
    else:
        print("Congratulations! You guessed the number:", number)
        print("It took you", guesses, "guesses.")
        break