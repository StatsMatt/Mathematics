# simple #
def is_factor(a,b):
    if b%a==0:
        return True
    else:
        return False
    
def factor(b):
    for i in range(1,b+1):
        if b%i==0:
            print(i)

if __name__ == '__main__':
    b = input('Your Number Please: ')
    b = float(b)
    if b > 0 and b.is_integer():
        factor(int(b))
    else:
        print('Please enter a positive integer')

def km_miles():
    km = float(input('Input km: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Input miles: '))
    km = miles * 1.609
    print('Distance in km: {0}'.format(km))

def f_to_c():
    f=float(input('Input fahrenheit: '))
    c=(f-32)*(5/9)
    print('{0} fahrenheit is {1} celsius'.format(f,c))

def c_to_f():
    c=float(input('Input celsius: '))
    f=c*(9/5)+32
    print('{0} celsius is {1} fahrenheit'.format(c,f))

''' 
Quadratic EQ
'''

def roots(a,b,c):
    D=(b**2-4*a*c)**(1/2)
    x_1=(-b+D)/(2*a)
    x_2=(-b-D)/2*a
    print(f'The roots are {x_1} and {x_2}')

def even_odd(a):
    if a%2==0:
        print('Even')
    else:
        print('Odd')
    count=1
    while count<=9:
        a+=2
        print(a)
        count+=1
if __name__ == '__main__':
    try:
        num = float(input('Enter an integer: '))
        if num.is_integer():
            even_odd(int(num))
        else:
            print('{0} is not an integer'.format(num))            
    except ValueError:
        print('Please enter a number')

def multi_table(a, n):
    for i in range(1, n + 1):
        print('{0} x {1} = {2}'.format(a, i, a * i))

if __name__ == '__main__':
    try:
        a = float(input('Input a number: '))
        n = int(input('Input a multiple: '))
        if n < 1:  # Validate that n is positive
            print('The multiple must be a positive integer.')
        else:
            multi_table(a, n)
    except ValueError:
        print('Please input valid integers.')

'''
Fraction operations
'''
from fractions import Fraction
def add(a, b):
 print('Result of Addition: {0}'.format(a+b))
def subtract(a,b):
  print('Result of Subtraction: {0}'.format(a-b))
def multiply(a,b):
  print('Result of Multiply: {0}'.format(a*b))
def divide(a,b):
  print('Result of Divide: {0}'.format(a/b))
if __name__ == '__main__':
  a = Fraction(input('Enter first fraction: '))
  b = Fraction(input('Enter second fraction: '))
  op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
  if op == 'Add':
    add(a,b)
  if op == 'Subtract':
    subtract(a,b)
  if op == 'Multiply':
    multiply(a,b)
  if op == 'Divide':
    divide(a,b)