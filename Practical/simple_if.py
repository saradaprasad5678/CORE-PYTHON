#simple-if  program

x=int(input('enter age:'))
if x>18:
    print('eligible for voting')
print(' not eligible for voting')    
    
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
