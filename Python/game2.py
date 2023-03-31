import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Start the game
print('Welcome to the number guessing game!')

while True:
    # Ask the user to guess a number
    guess = int(input('Guess a number between 1 and 100: '))
    
    # Check if the guess is too high or too low
    if guess < secret_number:
        print('Too low, try again.')
    elif guess > secret_number:
        print('Too high, try again.')
    else:
        print('Congratulations, you guessed the secret number!')
        break
