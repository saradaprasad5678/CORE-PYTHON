# Write a python program to print digit pattern
#1 2 3 
#1 2 3
#1 2 3
n=int(input("Enter: "))
for i in range(n):
  for j in range(n):
    print(j+1,end=' ')
  print()
