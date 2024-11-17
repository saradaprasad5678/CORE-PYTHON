# Write a python program to print taxi meter
#1-5km--->rs 50(bydefault)
#5-10km--->rs 12 per km
#10-15km--->rs 11 per km
#>15km--->rs 10 per km

km=int(input('enter the distance:'))
if km>=1 and km<=5:
    print('customer have to pay rs:50')
elif km>=6 and km<=10:
    fare=50+(km-5)*12
    print('customer has to pay:',fare)
elif km>=11 and km<=15:
    fare=50+60+(km-10)*11
    print('customer has to pay:',fare)
else:
    fare=50+60+55+(km-15)*10
    print('customer has to pay:',fare)
