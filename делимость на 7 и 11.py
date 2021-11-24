x = 100000
while x<100739:
 if (x%7+x%11==0) and (x%17*x%19*x%23)!=0:
     print (x)
 x+=1
