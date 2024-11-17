# Write a python program to print quiz application

score=0
n=int(input('who is pm of india? \n 1.modi\n 2.rahul\n 3.revanth\n 4.jagan\n'))
if n==1:
    print('valid answer',score+5)
else:
    print('invalid answer',score)
    
n1=int(input('who is cm of telangana? \n 1.modi\n 2.rahul\n 3.revanth\n 4.jagan\n'))
if n1==3:
    print('valid answer',score+5)
else:
    print('invalid answer',score)
