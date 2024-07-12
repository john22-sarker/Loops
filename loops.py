# i = 1
# while i<= 10:
#     print(f'5*{i} = {i*5}')
#     i+= 1


# i = 1
# x = 0
# while i<=10:
#     print(x)
#     x = i+x
#     # print(x)
#     i+=1
#
# print(f'The T Number is:- {x}')

# Clculator
firstNumber = float(input('Enter the first number:-'))
Opt= (input('Enter a operator From here( +, -, *, / ):- '))
SecNumber = float(input('Enter the 2nd number:-'))

if Opt == '+':
    print(firstNumber + SecNumber)
elif Opt == '-':
    print(firstNumber - SecNumber)
elif Opt == '*':
    print(firstNumber * SecNumber1)
elif Opt == '/':
    print(firstNumber / SecNumber1)
else:
    print('please Input a valid Number')
