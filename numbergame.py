#this is a guess the number game.
import random

print('hello. whats ur name?')
name = input()

print('well, '+name+', im thinking of a numba between 1 n 20')
secretNumber =random.randint(1,20)

for guessesTaken in range(1,7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('ur guess is too low')
    elif guess > secretNumber:
        print('ur guess is too high')
    else:
        break #this condition is for the correct guess

if guess == secretNumber:
    print('GJ, '+name+'! U guessed ma numba in '+str(guessesTaken) +' guesses!')
else:
    print('nah. da numba i was thinking of was '+str(secretNumber))


