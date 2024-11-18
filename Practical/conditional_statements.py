#simple-if  program

x=int(input('enter age:'))
if x>18:
    print('eligible for voting')
print(' not eligible for voting')    
    

#if-else program
age=int(input('enter age:'))
if age>18:
    print('eligible for voting')
else:
    print('pehele bada hoja')
    
    
#to check even number
x=int(input('enter number:'))
if x%2==0:
    print('even')
else:
    print('not even')
    
    
#using logic operators
#and
a=int(input('enter number:'))
if a%2==0 and a%3==0:
    print('divisible')
else:
    print('not divisible')
    
#or
a=int(input('enter number:'))
if a%2==0 or a%3==0:
    print('divisible')
else:
    print('not divisible')
    
#to check odd number
x=int(input('enter number:'))
if x%2!=0:
    print('odd')
else:
    print('even')
    
#not
a=int(input('enter number:'))
if  not (a%2==0 or a%3==0):
    print('not divisible')
else:
    print('divisible')
    
#not-in
if 'h' not in 'hello':
    print('not divisible')
else:
    print('available')

#nested-if
#largest of three numbers
a=int(input('enter number:'))
b=int(input('enter number:'))
c=int(input('enter number:'))
if a>b:
    if a>c:
        print('a is big')
    else:
        print('c is big')
else:
    if b>c:
        print('b is big')
    else:
        print('c is big')
