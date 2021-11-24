otvet = input ("Выберите X или 0?")
pole = [" "] * 9
def print_pole ():
    print (pole [0:3])
    print (pole [3:6])
    print (pole [6:9])
if otvet == "X":
    print ('Выберите номер поля.')
    print_pole()
if otvet == "0":
    pole [2] = '0'
    print_pole()
print ('Выберите номер поля.')
def win ():
    
