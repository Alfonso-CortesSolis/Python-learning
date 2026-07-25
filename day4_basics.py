import random

start_game = input("Do you want to play the guessing game? (yes/no): ").lower()

while start_game == "yes":
    random_num = random.randint(1, 10)
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < 1 or guess > 10:
        print("Please guess a number between 1 and 10.")
        continue

    guess_counter = 1

    if guess == random_num:
        print("Wow! You guessed it on the first try! You are amazing!")
        start_game = input("Do you want to play again? (yes/no): ").lower()
    else:
        while guess != random_num:
            guess_counter += 1
            if guess < random_num:
                print("Too low! Try again.")
            elif guess > random_num:
                print("Too high! Try again.")

            guess = int(input("Try again! Guess a number between 1 and 10: "))

        print("Congratulations! You guessed the number!")
        print(f"It took you {guess_counter} tries.")

        start_game = input("Do you want to play again? (yes/no): ").lower()
