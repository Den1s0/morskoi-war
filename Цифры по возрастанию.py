num=int(input("Введите число"))
f= True
while num>9:
 d=num%10
 num//=10
 d1=num%10
 if d<d1:
  f=False
  break
if f:
 print ("Да")
else:
    print ("Net")
