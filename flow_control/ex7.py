def integer_message(i):
    if i > 100:
        print(f'{i} is greater than 100')
    elif i >= 51:
        print(f'{i} is between 51 and 100')
    elif i >= 0:
        print(f'{i} is between 0 and 50')
    else:
        print(f'{i} is less than 0')

integer_message(-1)