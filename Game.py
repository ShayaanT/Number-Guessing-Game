import random


guesses = 0


score = 0


print('Hello! What is your name?')

name = input()




 
number = random.randint(1, 100)


print('Well, ' + name + ', I am thinking of a number between 1 and 100.')


while guesses < 5:

    print('Take a guess.') 

    user_input = input()

    user_input = int(user_input)


    guesses = guesses + 1


    if user_input < number:

        print('Your guess is too low.') 


    if user_input > number:

        print('Your guess is too high.')


    if user_input == number:

        break



if user_input == number:

    guesses = str(guesses)

    print('Good job, ' + name + '! You guessed my number in ' + guesses + ' guesses!')

    if guesses == 5:

        score = score + 1


    if guesses == 4:

        score = score + 2


    if guesses == 3:

        score = score + 3


    if guesses == 2:

        score = score + 4


    if guesses == 1:

        score = score + 5


    else:

        score = score



if user_input != number:

    number = str(number)

    print('Nah the number I was looking for was ' + (number)+ '.'


print('Thank you for playing! Your final score is' + str(score) + '.')


