import random

start_game = input("Do you want to play the guessing game? (yes/no): ").lower()


while start_game == "yes":
    random_num = random.randint(1, 10)
    num_left = 5
    guess_counter = 0
    while num_left > 0:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10.")
            continue

        num_left -= 1

        if guess == random_num:
            if guess_counter == 1:
                print("Wow! You guessed it on the first try! You are amazing!")
                start_game = input("Do you want to play again? (yes/no): ").lower()
                break
            else:
                print("Congratulations! You guessed the number!")
                print(f"It took you {guess_counter} tries.")
                start_game = input("Do you want to play again? (yes/no): ").lower()
                break
        elif num_left > 0:
            guess_counter += 1
            if guess < random_num:
                print("Too low! Try again.")
                print(f"You have {num_left} tries left.")
            elif guess > random_num:
                print("Too high! Try again.")
                print(f"You have {num_left} tries left.")
        else:
            print("Sorry, you've run out of tries. The number was:", random_num)
            start_game = input("Do you want to play again? (yes/no): ").lower()
            break
