# Write a python program to print digit pattern
#1 2 3 
#4 5 6
#7 8 9
c=1
n=int(input("Enter: "))
for i in range(n):
  for j in range(n):
    print(c,end=' ')
    c=c+1
  print()
