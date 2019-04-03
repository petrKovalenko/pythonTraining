#крестики нолики
#глобальные константы
CROSS = "X"
ZERO = "0"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

#функция пытается преобразовать аргумент в int, если не может - возвращает null
def intParser(num):
    try:
        x = int(num)
        return x
    except ValueError:
        return None

#возвращает инструкцию
def instructions():
    """ Выводит на экран инструкцию для игрока """
    print(
    """
    Добро пожаловать в игру крестики-нолики.
    Чтобы сделать ход, ввели числа от 1 до 8.
    Числа соответсвуют полям, как показано а рисунке ниже.
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    Да начнётся игра!\n
    """
    )
#спрашивает вопрос, дожидаясь ответа y или n
#возвращает y или n
def ask_yes_no(question):
    answer = input(question)
    while True:
        if answer.lower() == "y"  or answer.lower() == "да" :
            return "y"
        if answer.lower() == "n"  or answer.lower() == "нет" :
            return "n"
        print("Ответ должен быть y,Y,да или n,N,нет")
        answer = input(question)

#Спрашивает вопрос question, дожидаясь ответа из указанного диапазона
#возвращает число от low до high или None в случае ошибки
def ask_number(question, low = 0, high = 8):
    if low > high:
        print("Low не может быть больше high!")
        return None
    num = intParser(input(question))
    while num is None or num < low or num > high:
        print("Введите число от " + str(low) + " до " + str(high) + " включительно.")
        num = intParser(input(question))
    return num

    


    
