from random import *
points = [6,7,8,9,10,2,3,4,11] * 4
playerpoints = 0
computerpoints = 0
while True:
    answer = input ('Ты будешь брать карту? (yes/no)')
    if answer == 'no':
        break
    shuffle(points)
    nowpoints=points.pop (0)
    playerpoints+=nowpoints
    print ('У тебя сейчас', nowpoints, 'очков.Всего', playerpoints,'очков')
    if playerpoints >=21:
        break
if playerpoints == 21:
    print ('Ты победил!')
if playerpoints > 21:
    print ('Ты проиграл!')
while computerpoints < playerpoints:
    if computerpoints == 21:
        break
    
    

