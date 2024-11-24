#Write a python program to check whether given number is prime or not 
fact=0
i=1
n=int(input('enter number:'))
while i<=n:
  if n%i==0:
    fact=fact+1
  i=i+1
if fact==2:
  print(n,'is prime number')
else:
  print(n,'is not a prime number')
