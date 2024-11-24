# Write a python program to print sum of 1-n odd numbers
i=1
n=int(input('enter range:'))
sum=0
while i<=n:
  if i%2!=0:
    sum=sum+i
  i=i+1
print(sum)
