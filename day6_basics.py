import random


def get_valid_guess():
    while True:
        guess_input = input("Guess a number between 1 and 10: ")

        try:
            guess = int(guess_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if 1 <= guess <= 10:
            return guess

        print("Please enter a number between 1 and 10.")


def play_game():
    random_num = random.randint(1, 10)
    guesses_left = 5
    guess_counter = 0

    while guesses_left > 0:
        guess = get_valid_guess()

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
