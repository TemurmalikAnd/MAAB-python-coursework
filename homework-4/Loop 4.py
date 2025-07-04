"""4. Number Guessing Game Create a simple number guessing game.

    The computer randomly selects a number between 1 and 100.
    If the guess is high, print "Too high!".
    If the guess is low, print "Too low!".
    If they guess correctly, print "You guessed it right!" and exit the loop.
    The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
    If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.
"""
from random import randint

def number_generator():
    random_number = randint(1, 100)  # Generate new number each game
    print("I've guessed a number between 1 and 100")
    
    for i in range(1, 11):
        while True:
            user_input = input('Your guess: ')
            try:
                if user_input.strip() == '':  # Check for empty input properly
                    print('Please input an integer')
                    continue
                user_guess = int(user_input)  # Convert to integer
                break
            except ValueError:
                print('Please enter an integer!')
                continue  # Continue the while loop, not break
        
        # Compare integers, not string with integer
        if user_guess < random_number:
            print('Too low!')
        elif user_guess > random_number:
            print('Too high!')
        else:
            print('You guessed it right!')
            return  # Exit the function when they win
    
    # This runs only if the loop completes without breaking (they lost)
    print(f'You lost. The number was {random_number}.')
    permission_asker()

def permission_asker():
    accept_list = ['Y', 'YES', 'y', 'yes', 'ok', 'OK']
    user_input = input('Want to play again? ')
    if user_input in accept_list:
        number_generator()
    else:
        print('Thanks for playing!')

# Start the game
number_generator()