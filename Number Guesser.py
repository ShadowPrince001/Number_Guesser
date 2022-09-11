import random

level = int(input("Welcome to Number Guesser. You have to guess a randomly generated number. Enter 1 for easy difficulty between 1 and 10, enter 2 for medium difficulty between 1 and 100 and enter 3 for hard difficulty between 1 and 1000. Choose difficulty: "))

if level == 1:
    random_number = random.randint(1,10)
    guess_number = 0
    while guess_number < 20:
        guess_number = guess_number + 1
        guess = int(input("Enter number: "))

        if guess > random_number:
            print("Your number is greater than the generated number. Try again. "),
         
        if guess < random_number:
            print("Your number is lesser than the generated number. Try again")
        if guess == random_number:
            print("Well done you have guessed correctly in",guess_number, "guesses.")
            break

if level == 2:
    random_number = random.randint(1,100)
    guess_number = 0
    while guess_number < 20:
        guess_number = guess_number + 1
        guess = int(input("Enter number: "))

        if guess > random_number:
            print("Your number is greater than the generated number. Try again. "),
         
        if guess < random_number:
            print("Your number is lesser than the generated number. Try again")
        if guess == random_number:
            print("Well done you have guessed correctly in" ,guess_number,"guesses.")
            break

if level == 3:
    random_number = random.randint(1,1000)
    guess_number = 0
    while guess_number < 20:
        guess_number = guess_number + 1
        guess = int(input("Enter number: "))

        if guess > random_number:
            print("Your number is greater than the generated number. Try again. "),
         
        if guess < random_number:
            print("Your number is lesser than the generated number. Try again")
        if guess == random_number:
            print("Well done you have guessed correctly in", guess_number, "guesses.")
            break






