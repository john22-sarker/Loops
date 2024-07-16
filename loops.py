h = int(input('Enter any Number in (6,7,8,9,10):'))
if h<6:
    print('Please enter a right number!')
else:
 for o in range(h, 0, -1):
        if o == 2:
            break
        if o == 5:
            continue
        print(f'{o} + Congratulation!')
    
i = 1
while i<= 10:
    print(f'2*{i} = {i*2}')
    i+= 1


i = 1
x = 0
while i<=10:
      print(x)
      x = i+x
      print(x)
     i+=1
print(f'The T Number is:- {x}')

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
