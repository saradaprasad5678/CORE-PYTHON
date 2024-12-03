"""Write a python program to print star pattern
* 
* * 
* * *
  * *
    * """
n=int(input('Enter:'))
for i in range(n):
  for j in range(i+1):
    print('*',end=' ')
for i in range(n-i+1):
  for j in range(i+1):
    print(' ',end=' ')
  for j in range(n-i-1):
    print('*',end=' ')
  print()
