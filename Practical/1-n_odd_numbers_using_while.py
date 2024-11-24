# Write a python program to print 1-n odd numbers
i=1
n=int(input('enter range'))
while i<=n:
  if i%2!=0:
    print(i)
  i=i+1
