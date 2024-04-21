import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 20.")
print("You have 5 guesses to get it right.")

rand_num = random.randint(1, 20)

guessed_correctly = False
for x in range(5):
    print("Guess the number:")
    guess = int(input())
    if ( guess > rand_num ):
        print("Too high! Try again.")
    elif ( guess < rand_num ):
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the number correctly!")
        guessed_correctly = True
        break

if ( guessed_correctly == False ):
    print(f"Unfortunately, the correct number is {rand_num}")

