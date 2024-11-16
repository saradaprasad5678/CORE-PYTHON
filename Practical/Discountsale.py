#Discount sale program
shirtq=int(input('enter qunatity:'))
price=int(input('enter price:'))
amt=shirtq*price  #10*200=2000
disperc=int(input('enter disperc:'))
disamt=amt*disperc//100  #200
total=amt-disamt
print('total:',total)
