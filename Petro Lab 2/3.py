from random import randint

num = randint(1, 10)

user_num = int(input('Guess number between 1 and 10'))

if num == user_num:
    print('Correct')
else:
    print('Wrong')
