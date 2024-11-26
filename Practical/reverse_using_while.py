#Python program to print reverse of a number
rev=0
n=int(input('enter number:'))
while n!=0:
  rev=rev*10+n%10
  n=n//10
print(rev)
