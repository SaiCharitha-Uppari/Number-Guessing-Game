import random


def game():
    print('')
    max_range = 500
    n = random.randint(1, max_range)
    guess_allowed = 15
    print('WELCOME TO NUMBER GUESSING GAME!!!')
    print('')
    name = input('Please enter your name::')
    user = print('Hello {} ....ALL THE BEST!!'.format(name))

    while (True):
        level = input('Select Your level(easy,medium,hard):').lower()
        if level in ['easy', 'medium', 'hard']:
            break
        else:
            print('Please choose correctly')
    if level == 'easy':
        guess_allowed = 15
        max_range = 50
    elif level == 'medium':
        guess_allowed = 10
        max_range = 100
    else:
        guess_allowed = 5
        max_range = 500
    n = random.randint(1, max_range)
    for i in range(1, guess_allowed + 1):
        try:
            print(("Attempts left: {}".format(guess_allowed - i + 1)))
            usr = input('Guess Number Between 1 and 500::')
            num = int(usr)
            if n == num:
                print('congratulations!!!!....YOU WON!!')

                break
            else:
                if n < num:
                    print('too high :')

                else:
                    print('too low : ')


        except ValueError:
            print('dont enter symbols,str and alnums')

    else:
        print('out of attempts...Better luck Next Time')
        print('Correct Answer:{}'.format(n))


# main program
while True:
    game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
    else:
        print('thank you for playing')