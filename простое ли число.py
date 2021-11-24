x = int (input('Vvedite chislo'))
y=2
otvet = True
while (y<x):
    if x % y == 0:
        otvet = False
        break
    y+=1
if otvet:
    print ('Prostoe')
else:
    print ('Ne prostoe')
     
    

