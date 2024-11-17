# Write a python program to print ATM application for cash withdrawal

available=10000
pin=int(input('enter the pin:'))
if pin==1234:
    print('valid pin')
    t=int(input('select option\n 1.Withdraw\n 2.Banking\n 3.Balance\n enter :'))
    if t==1:
        amt=int(input('enter withdrawl amount:'))
        if amt<=available:
            print('collect cash')
        else:
            print('insufficient balance')
else:
    print('invalid pin')
  
