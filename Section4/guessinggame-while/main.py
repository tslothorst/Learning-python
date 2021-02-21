import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = None

print("Please guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    if guess > answer:   # guess must be greater than answer
        print("Please guess lower")
    if guess == answer:
        print("Well done, you guessed it")


