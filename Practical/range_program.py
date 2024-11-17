# write a python program to print range of the given numbers(100-400)
a=int(input('enter the number:'))
if a>0 and a<100:
    print('a is in range 0-100')
elif a>100 and a<200:
    print('a is in range 100-200')
elif a>200 and a<300:
    print('a is in range 200-300')
elif a>300 and a<400:
    print('a is in range 300-400')
else:
    print('a is out of range')

