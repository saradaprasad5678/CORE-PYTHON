# Try to buy them program to print alphabet pattern
#A B C
#D E F
#G H I
k=65
n=int(input('Enter: '))
for i in range(n):
  for j in range(n):
    print(chr(k),end=' ')
    k=k+1
  print()
