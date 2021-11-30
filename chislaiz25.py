ch = input ()
dlina = len (ch)
ch = ch.replace ("2","0")
ch = ch.replace ("5","1")
x = int (ch, 2)
while dlina > 1:
    n = 2 ** (dlina-1)
    dlina  -= 1
    n = dlina + dlina + 1
ch = int(ch, 2)
a = n + 1 + ch
print (a)

    