import random
from logo_number_game import logo
print(logo)
number = random.randint(1,100)
# print(number)

print("The number is between 1 and 100.")
end=False
while end is False:
    difficulty=input("Choose difficulty, Type 'Easy' or 'Hard' : ").lower()
    if difficulty=='easy':
        attempt=10
        end=True
    elif difficulty=='hard':
        attempt=5
        end=True
    else:
        print("Type a valid difficulty level.")


guess_list=[]

while attempt!=0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess : "))

    if guess != number:
        if guess not in guess_list:
            attempt-=1
        else:
            print("You have already typed this number.")
    elif guess == number:
        print()
        print("You guessed it right.")
        print("You won. :)")
        break

    guess_list.append(guess)
    # print(guess_list)

    if guess < number:
        if abs(number-guess) < 5:
            print(f"You are too close and the {guess} is lower than actual number.") 
        else:
            print(f"{guess} is LOWER than actual number.")
    elif guess > number:
        if abs(guess-number) < 5:
            print(f"You are too close and the {guess} is higher than actual number.") 
        else:
            print(f"{guess} is HIGHER than the actual number.")
    if attempt > 0:
        print("Guess again")
    if attempt<1:
        print()
        print("You have run out of guesses, YOU LOSE :( ")