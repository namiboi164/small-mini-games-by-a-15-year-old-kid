import random

def play_guessing_game():
    print("Welcome to the Number Guessing Challenge!")
    print("I'm thinking of a number between 1 and 100.")
    
    # The computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"Can you guess it? You have {max_attempts} attempts!")
    print("-" * 40)

    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Oops! Please enter a valid number.")
            continue
        
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too low! ⬆️ Try a higher number.")
        elif guess > secret_number:
            print("Too high! ⬇️ Try a lower number.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!")
            break
    else:
        print(f"\nGame Over! You've run out of attempts. The number was {secret_number}. 😔")

# Run the game
play_guessing_game()