str = 'this 4 is 5 string 6'

for elem in str:
    if elem >= '0' and elem <= '9':
        print(f'{elem} is numeric')
    else:
        print(f'{elem} is not numeric')
