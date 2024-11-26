#write python program for Armstrong number
n=int(input('enter number:'))
n1=n
sum_of_powers=0
last_digit=0
number_of_digits=len(str(n))
while n!=0:
  lastdidgit=n%10
  sum_of_powers=sum_of_powers+last_digit**number_of_digits
  n=n//10
print(sum_of_powers)
if sum_of_powers==n1:
  print('yes an armstrong number')
else:
  print('no not an armstrong number')
