#swapping using a temporary variable
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=a
a=b
b=c
print("after swapping a=",a,"b=",b)

#swapping without using a temporary variable
a=int(input("enter first number:"))
b=int(input("enter second number:"))
a=a+b
b=a-b
a=a-b
print("after swapping a=",a,"b=",b)
