import random
num = random.randint(1,100)

print("""WELCOME TO GUESSING GAME!
I'm thinking of a number between 1 and 100.
If your guess is more than 10 away from my number, I'll tell you you're COLD.
If your guess is within 10 of my number, I'll tell you you're WARM.
If your guess is farther than your most recent guess, I'll say you're getting COLDER.
If your guess is closer than your most recent guess, I'll say you're getting WARMER.
LET'S PLAY!""")

guesses = [0]

while True:
    guess = int(input("Guess the number I'm thinking of: "))

    if guess < 1 or guess > 100:
        print('Out of bounds! Please try again:')
        continue

    if guess == num:
        print(f'Congratulations! You guessed in only {len(guesses)} guesses!')
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
