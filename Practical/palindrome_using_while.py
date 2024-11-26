# Python program to check whether the given number is palindrome or not
rev=0
n=int(input('enter number:'))
n1=n
while n!=0:
  rev=rev*10+n%10
  n=n//10
print(rev)
if rev==n1:
  print(rev,'is palindrome')
else:
  print(rev,'is not palindrome')
