# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 200)
print('Hi, ' + myName + ', I am thinking of a number between 1 and 200.')

for guessesTaken in range(6):
    print('Take a guess.') 
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Nope, your guess is too low.') 

    if guess > number:
        print('Nope, your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
