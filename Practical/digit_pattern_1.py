# Write a python program to print digit pattern
#1 1 1
#2 2 2
#3 3 3
n=int(input("Enter: "))
for i in range(n):
  for j in range(n):
    print(i+1,end=' ')
  print()
