from math import log2, ceil
from random import randint

def count_try(n):
    '''Возвращает количество попыток угадать число от 1 до n бинарным поиском'''
    result = ceil(log2(n))
    return result

def is_valid(n):
    '''Возвращает True, если n - число от 1 до 100, и False в противном случае'''
    if not n.isdigit():
        return False
    else:
        if 1 <= int(n) <= 100:
            return True
        else:
            return False
        
print('Добро пожаловать в числовую угадайку! \n')

hidden_number = randint(1, 100)

print("Введите число от 1 до 100.") 
while True:
    number = input()
    if is_valid(number): #Проверка на корректность введенных данных
        number = int(number)
        if number == hidden_number:
            print("Вы угадали, ура!\n")
            break
        elif number < hidden_number:
            print("Ваше число меньше загаданного, попробуйте еще раз!")
        else:
            print("Ваше число больше загаданного, попробуйте еще раз!")
    else:
        print("Неверный ввод. Введите число от 1 до 100.")

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

