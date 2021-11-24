a = input ("Введите число")
num = [0 for i in range (10)]
for l in a:
    num [int(l)] += 1
m = max (num)
print (num.index (m))
