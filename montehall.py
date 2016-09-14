import random

while True:
    switch = raw_input('Welcome to the Monty Hall simulation. Would '
                       'you like to simulate the "switching" or '
                       '"non-switching" strategy? ')

    if switch != 'switching' and switch != 'non-switching':
        print "\nPlease enter 'switching' or 'non-switching'.\n"
    else: break 

while True: 
    n = raw_input('\nHow many iterations of the simulation would you '
                  'like to run? ')
    
    try:
        int(n)
        if int(n) < 10:
            print "\nPlease enter an integer greater than 9."
        else: 
            print ('\nThank you. We will run the %s strategy for %d'
                  ' iterations.\n') % (switch, int(n))
            break
    except: 
        print "\nPlease enter an integer greater than 9."
        continue

win = 0.0

for i in range(0, int(n)):
    car = random.randrange(0, 3)
    choice = random.randrange(0,3)
    reveal = random.randrange(0,3)
    while reveal == choice or reveal == car:
        reveal = random.randrange(0,3)

    if switch == 'switching': 
        choice = 1 + 2 - reveal - choice 

    if choice == car:
        win += 1

    i += 1

print ('Your win percentage with the %s strategy is: %.4f') % \
        (switch, win/int(n))

print ("\nThank you for running the Monte Hall simulation."
      "See you next time.\n")
