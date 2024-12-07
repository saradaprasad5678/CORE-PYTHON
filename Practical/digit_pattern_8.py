#Write a python program to print digit pattern
#3 3 3
#  2 2
#    1
n=int(input('Enter: '))
for i in range(n):
  for j in range(i):
    print(' ',end=' ')
  for j in range(n-i):
    print(n-i,end=' ')
  print()
