"""Write a python program to print star pattern
* 
* * 
* * * """
n=int(input('enter'))
for i in range(n):
  for j in range(i+1):
    print('*',end=' ')
  print()
