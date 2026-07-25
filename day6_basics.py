import random


def get_valid_guess(max_number):
    while True:
        guess_input = input(f"Guess a number between 1 and {max_number}: ")

        try:
            guess = int(guess_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if 1 <= guess <= max_number:
            return guess

        print(f"Please enter a number between 1 and {max_number}.")

def choose_difficulty():
    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower().strip()

        if difficulty == "easy":
            return 10, 5  
        elif difficulty == "medium":
            return 50, 10   
        elif difficulty == "hard":
            return 100, 15   
        else:
            print("Invalid choice. Please choose 'easy', 'medium', or 'hard'.")


def play_game():
    
    max_number, guesses_left = choose_difficulty()
    random_num = random.randint(1, max_number)
    guess_counter = 0

    while guesses_left > 0:
        guess = get_valid_guess(max_number)

        guess_counter += 1
        guesses_left -= 1

        if guess == random_num:
            if guess_counter == 1:
                print("Wow! You guessed it on the first try! You are amazing!")
            else:
                print("Congratulations! You guessed the number!")
                print(f"It took you {guess_counter} tries.")

            return

        if guess < random_num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        if guesses_left > 0:
            print(f"You have {guesses_left} tries left.")

    print(f"Sorry, you've run out of tries. The number was {random_num}.")


if __name__ == "__main__":
    start_game = (
        input("Do you want to play the guessing game? (yes/no): ").lower().strip()
    )

    while start_game == "yes":
        play_game()

        start_game = input("Do you want to play again? (yes/no): ").lower().strip()

    print("Thanks for playing!")
