import random

the_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
#print(f"TEST: the correct number is: {the_number}")


for i in range(1, 7):
    print("Take a guess ")
    guess = int(input())

    if guess > the_number:
        print(guess, "Your guess is too high")
    elif guess < the_number:
        print(guess, "Your guess is too low")
    else:
        break

if guess == the_number:
    print(f"Good job! You guessed my number in {i} guesses!")
else:
    print("Sorry you failed! The number I was thinking was " + str(the_number))