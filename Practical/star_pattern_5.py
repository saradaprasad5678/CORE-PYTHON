"""Write a python program to print star pattern    
* * *
  * *
    * """
n=int(input('Enter:'))
for i in range(n):
  for j in range(i):
    print(' ',end=' ')
  for j in range(n-i):
    print('*',)
