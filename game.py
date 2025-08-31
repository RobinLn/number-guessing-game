import random

# This function display welcome message
def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("Enter a number between 1 and 100.")

def choose_difficulty():

    print("\nSelect Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return 50
        elif choice == "2":
            return 100
        elif choice == "3":
            return 200
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_guess(low, high):
    while True:
        try:
            guess = int(input(f"Enter your guess ({low}-{high}): "))
            if low <= guess <= high:
                return guess
            else:
                print(f" Please enter a number between {low} and {high}.")
        except ValueError:
            print(" Invalid input. Enter an integer.")
def play_game():
    welcome_message()
    high = choose_difficulty()
    low = 1
    secret_number = random.randint(low, high)
    attempts = 0
    guess = 0

    while guess != secret_number:
        guess = get_guess(low, high)
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts.")
def play_again():
                while True:
                    again = input("Do you want to play again? (yes/no): ").lower()
                    if again in ["yes", "y"]:
                        return True
                    elif again in ["no", "n"]:
                        return False
                    else:
                        print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    while True:
        play_game()
        if not play_again():
            print("👋 Thanks for playing! Goodbye!")
            break