value = 5


while True:
    guess = int(input("Enter your guess: "))

    if value == guess:
        print("Yay! You guessed correctly.")
        break
    else:
        print("Wrong! Try again.")