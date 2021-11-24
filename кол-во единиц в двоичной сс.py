x = int (input ('Введите число в десятичной системе'))
counter = 0
while x>0:
    counter += x%2
    x = x//2
print (counter)
