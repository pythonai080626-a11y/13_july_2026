
# START

a = int(input('enter 2 digit number'))

if a >= 10 and a <= 99:
    ahadot = a % 10
    asarot = a // 10
    if ahadot == asarot:
        print('equal digits')
    else:
        print('NOT equal digits')
else:
    print('number should be between 10-99')

# STOP