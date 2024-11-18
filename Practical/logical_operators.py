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
