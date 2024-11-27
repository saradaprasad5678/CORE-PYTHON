# write a python program to print fibonacci series
n=int(input('Enter range:'))
i=0
a,b=0,1
while i<n:
  print(a,end=' ')
  a,b=b,a+b
  i=i+1
