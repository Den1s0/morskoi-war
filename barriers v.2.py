def ris_pole():
    c = 1
    for i in pole:
        if i == "P" or i < 10 :
            print(i, end="  ")
        else:
            print(i, end=" ")
            
        if c % 8 == 0:
            print("")
        c += 1
        
nachalo = input("Привет! Это игра Заграждения. Сыграем? (напиши да/нет)\n")
nachalo = nachalo.upper ()
if nachalo == "ДА":
    print ('Отлично! Давай начнем.')
    print ("Правила игры: Игроки по очереди ставят 'заграждения', выбрав по две соседние клетки поля (по диагонали ставить НЕЛЬЗЯ). Проигрывает тот игрок, который уже не может поставить на поле заграждение. P - обозначение твоих заграждений, C - заграждения компьютера.")
    pole = []
    for l in range(1, 65):
        pole.append(l)
        
    ris_pole()
    while 64 - (len ("P") + len ("C")) >= 2:
        for g in pole: 
            x = int (input ("Тебе нужно выбрать 2 клетки поля, стоящие рядом. Выбери первый номер клетки поля.\n"))
            y = int (input ("Теперь выбери второй номер клетки поля (они обязательно должны быть соседними).\n"))
            if x+1 == y or y+1 == x or x+8 == y or y+8 == x:
                x = x - 1
                y = y - 1
                pole [x] = "P"
                pole [y] = "P"
                ris_pole()
                
            else:
                print ("Неправильно введены числа. Попробуй еще раз.")
    else:
        print ("Ты проиграл!")
elif nachalo == "НЕТ":
    print ("До встречи!")
else:
    print ("Я тебя не понимаю! Запусти программу еще раз.")

