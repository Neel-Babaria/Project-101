import random

while True:
    no = random.randint(1,6)
    none = '[     ]'
    center = '[  0  ]'
    left = '[0    ]'
    right = '[    0]'
    rl = '[0   0]'

    if (no == 1):
        print(none)
        print(center)
        print(none)

    elif (no == 2):
        print(left)
        print(none)
        print(right)

    elif (no == 3):
        print(left)
        print(center)
        print(right)

    elif (no == 4):
        print(rl)
        print(none)
        print(rl)

    elif (no == 5):
        print(rl)
        print(center)
        print(rl)

    elif (no == 6):
        print(rl)
        print(rl)
        print(rl)
    
    yn = input('Would you like to roll again? Enter y if yes or anything else if no: ')
    
    if (yn == 'y' or yn =='Y'):
        print('Rolling again')
    
    else:
        print('Thank you for playing!')
        break
    