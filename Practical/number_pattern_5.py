# Write a python program to print digit pattern
#1 
#2 2 
#3 3 3
n=int(input('enter: '))
for i in range(n):
  for j in range(i+1):
    print(i+1,end=' ')
  print()
