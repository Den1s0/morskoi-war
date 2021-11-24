fraza = input ('Введите фразу')
fraza = fraza.upper ()
fraza = fraza.replace (' ','')
frazanaoborot = fraza [ : : -1]
if frazanaoborot == fraza:
    print ('Фраза является палендромом')
else:
    print ('Фраза не является палендромом')
