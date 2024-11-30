#nested For loop
"""Write a python program to print star pattern
* * *
* * *
* * * """
n=int(input('enter:'))
for i in range(n):
  for j in range(n):
    print('*',end=' ')
  print()
