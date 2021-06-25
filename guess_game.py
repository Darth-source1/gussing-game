import random
number = random.randint(0,10)

guess=input('iam thinking about a number between zero and ten. can you guess it? ')

while True:
    if (guess == number):
        break
    else:
        guess= int(input('nope. Try again: '))
print('you gussed it:)')  
