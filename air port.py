a={'1':'Air india','2':'jet airway','3':'name soen','4':'scrad airways'}
b={'1':'4.00am','2':'11.30am','3':'6.00pm','4':'10.00pm'}
fc=50000
sc=35000
tc=10000
print('welcome to national airport')
c=input('name:')
d=input('home address:')
e=input('from place')
f=input('to place:')
print('1:first class=rs',fc)
print('2:second class=rs',sc)
print('3:third class=rs',tc)
i=int(input('ticket class:'))
j=int(input('no.of ticket:'))
print('avalibe airlince:',a)
g=int(input('enter you need airline number'))
print('avalibe times:',b)
h=int(input('enter the time number eg:3'))
if i==1:
    print("cost for ticket",j*fc)
if i==2:
    print('cost for ticket',j*sc)
if i==3:
    print('cost for ticket',j*tc)
print('your ticket conformed')
