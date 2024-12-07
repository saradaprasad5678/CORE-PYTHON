# Write a python program to print alphabet pattern
#A A A
#B B B
#C C C
k=65
n=int(input('Enter: '))
for i in range(n):
  for j in range(n):
    print(k,end=' ')
  k=k+1
  print()
