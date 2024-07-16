i = 1
while i<4:
    print('Hi')
    i = i+1

x = 1
y = 2
while x<=10:
    print(x*y)
    x = x+1
d = 'John','sarker'
for i in d:
    print(d)

for k in range(1,17,2):
    print(k)

h = int(input('Enter any Number:'))
for o in range(h,0,-1):
    if o == 2:
        break
    print(o)
    
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
