n = 19006100
while n<19007200:
    d=0
    x=1
    while x<=n:
        if n%x == 0 and n%2 == 1:
            d+=1
            x+=1
 if d==4:
     print (n)
 n+=1
