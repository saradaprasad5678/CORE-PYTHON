# write a python program to print sum of individual numbers
n=int(input('Enter the number:'))
sum=0
while n!=0:
  sum=sum+n%10
  n=n//10
print(sum,'is sum of individual numbers')
