str = 'this 4 is 5 string 6'

for elem in str:
    if ord(elem) >= 48 and ord(elem) <= 57:
        print(f'{elem} is numeric')
    else:
        print(f'{elem} is not numeric')
