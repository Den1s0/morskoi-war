word = input ()
x = ''
k = 0
while k < len(word):
    if word.count (word[k]) >= 2:
        x = word [k] + x + word [k]
        word [k] + x + word [k]
        word.replace ( word [k] , '',2)
    else:
        k+=1
print (x)
