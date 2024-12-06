# Write a python program to print digit pattern
#    1 
#  1 2 
#1 2 3
n=int(input('enter:'))
for i in range(n):
  for j in range(n-i-1):
    print(' ',end=' ')
  for j in range(i+1):
    print(j+1,end=' ')
  print()
