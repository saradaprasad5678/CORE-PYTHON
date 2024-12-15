# Try to buy them program to print alphabet pattern
#A B C
#A B C
#A B C
k=65
n=int(input('Enter: '))
for i in range(n):
  for j in range(n):
    print(chr(k+j),end=' ')
  print()
