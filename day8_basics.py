import json
import random
from pathlib import Path

HIGHSCORE_FILE = Path(__file__).with_name("high_scores.json")


def load_high_scores():
    default_high_scores = {"easy": None, "medium": None, "hard": None}

    if not HIGHSCORE_FILE.exists():
        save_high_scores(default_high_scores)
        return default_high_scores

    try:
        with HIGHSCORE_FILE.open("r", encoding="utf-8") as file:
            loaded_scores = json.load(file)
    except (json.JSONDecodeError, OSError):
        return default_high_scores

    if not isinstance(loaded_scores, dict):
        return default_high_scores

    return {
        difficulty: loaded_scores.get(difficulty)
        for difficulty in ("easy", "medium", "hard")
    }


def save_high_scores(high_scores):
    with HIGHSCORE_FILE.open("w", encoding="utf-8") as file:
        json.dump(high_scores, file, indent=2)


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
            return 10, 5, difficulty
        elif difficulty == "medium":
            return 50, 10, difficulty
        elif difficulty == "hard":
            return 100, 15, difficulty
        else:
            print("Invalid choice. Please choose 'easy', 'medium', or 'hard'.")


def print_high_scores(high_scores):
    print("Current session high scores:")
    for difficulty in ("easy", "medium", "hard"):
        score = high_scores[difficulty]
        display_score = score if score is not None else "No score yet"
        print(f"- {difficulty.title()}: {display_score}")
    print()


def update_high_score(high_scores, difficulty, tries):
    current_best = high_scores[difficulty]
    if current_best is None or tries < current_best:
        high_scores[difficulty] = tries

    save_high_scores(high_scores)


def play_game(high_scores):
    print_high_scores(high_scores)

    max_number, guesses_left, difficulty = choose_difficulty()
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

            update_high_score(high_scores, difficulty, guess_counter)
            print(f"New {difficulty.title()} high score: {high_scores[difficulty]} tries.")
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

    high_scores = load_high_scores()

    while start_game == "yes":
        play_game(high_scores)

        start_game = input("Do you want to play again? (yes/no): ").lower().strip()

    save_high_scores(high_scores)
    print("Thanks for playing!")
