from random import randint


def guess_a_number():
    """Game to guess a number the computer randomly generated."""

    # TODO:
    # generate a random number (uniformly distributed between 0 and 100)
    # read input from the user and validate that the input is numeric (use the function check_raw)
    # check whether the number was guessed 
    # implement the functions evaluate_my_number, which checks whether the number is too high or too low
    # and print this information to the user
    # let the computer guess, therefore implement the demo_a_number function
    random_number=randint(0,100)
   
    '''versuche=0
    max_versuche=5
    guess=-1
    test= False
    while guess != random_number:
        while test == False:
            guess= input('Gib eine Zahl zwischen 0 und 100 ein: ')
            try:
                guess= int(guess)
                test=True
            except ValueError:
                print('Try Again')
            
        if guess == random_number:
            print('Du hast die Zahl erraten!')
        elif guess > random_number:
            print('Die Zahl ist zu gross')
            versuche=versuche+1
        else:
            print('Die Zahl ist zu klein')
            versuche=versuche+1'''

    


def check_raw(guessnumber):
    """Gets the string, raw_input should print, checks and returns the input."""
    return checked_int


def evaluate_my_number(guess, random_number):
    """Is the guess to high or to low? Guess again!"""
   


def demo_a_number():
    """The computer tries to guess the number"""
    random_number=randint(0,100)
    number=randint(0,100)
    print (random_number)
    print (number)
    if number == random_number:
        print('correct number')
    while number!=random_number:
        if number >random_number:
            print('number too high')
            number=randint(0,number)
            print(number)
        else:
            print('number too low')
            number=randint(number,100)
            print(number)
    print ('correct number: ')
    print(number)

    
#guess_a_number()
demo_a_number()
