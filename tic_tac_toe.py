#крестики нолики
#импорт
import random

#глобальные константы
CROSS = "X"
ZERO = "0"
EMPTY = " "
TIE = "Ничья"
SQUARE_STEP = 3
NUM_SQUARES = SQUARE_STEP * SQUARE_STEP


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

#Определяет случайно, кто первый ходит, человке или компьютер,
#и возвращает сответсвующие фишки обоим сторонам. У кого крестик, тот и первый.
#первый вывод - фишка пользователя, второй - компьютера
def first_turn():
    if(random.randint(1, 2) == 1):
        print("Право первого хода - у Вас.")
        return CROSS, ZERO
    else:
        print("право первого хода - у компьютера.")
        return ZERO,CROSS

#создаёт и возвращает список из элементов с пустыми занчениями,
#представляющий из себя игровую доску
def new_board():
    return [EMPTY] * NUM_SQUARES

#выводит доску на экран
def display_board(board):
    if board is None or len(board) < NUM_SQUARES:
        print("При передачи параметра доски произошла ошибка!")
        return None
    for i in range(0, 3):
        print("\t" + board[3*i] + " | " + board[3*i+1] + " | " + board[3*i+2])

#принимает на вход доску, возвращает список доступных ходов
def legal_moves(board):
    if board is None:
        print("При передачи параметра доски произошла ошибка - доска пуста!")
        return None
    if len(board) != NUM_SQUARES:
        print("При передачи параметра доски произошла ошибка - доска не той длины!")
        return None
    availableMoves = []
    for i in range(0,NUM_SQUARES):
        if(board[i] == EMPTY):
           availableMoves.append(i)
    return availableMoves

#определяет победителя, и возвращает фишук победителя
#если ничья - возвращает TIE
#если не все клетки заполнены - возвращает None
def winner(board):
    if board is None:
        print("При передачи параметра доски произошла ошибка - доска пуста!")
        return None
    if len(board) != NUM_SQUARES:
        print("При передачи параметра доски произошла ошибка - доска не той длины!")
        return None
    #победитель по горизонтали
    for i in range(0, SQUARE_STEP):
        if board[i*SQUARE_STEP] == EMPTY:
            continue
        winning = True
        for j in range(1, SQUARE_STEP):
            if board[i*SQUARE_STEP] != board[i*SQUARE_STEP + j]:
                winning = False
                break
        if winning:
            return board[i*SQUARE_STEP]
    #победитель по вертикали
    for i in range(0, SQUARE_STEP):
        if board[i] == EMPTY:
            continue
        winning = True
        for j in range(1, SQUARE_STEP):
            if board[i] != board[i + j*SQUARE_STEP]:
                winning = False
                break
        if winning:
            return board[i]
    #победитель по диагонали
    if board[0] != EMPTY:
        winning = True
        for i in range(1, SQUARE_STEP):
            if board[0] != board[i * (SQUARE_STEP + 1)]:
                winning = False
                break
        if winning:
            return board[0]
    if board[SQUARE_STEP -1] != EMPTY:
        winning = True
        for i in range(1, SQUARE_STEP):
            if board[SQUARE_STEP -1] != board[(i + 1) * (SQUARE_STEP - 1)]:
                winning = False
                break
        if winning:
            return board[SQUARE_STEP -1]
    #если нет победителя, смотрим, остались ли пустые клетки
    #если пустых клеток не остальосб - тогда ничья
    for i in range(0,NUM_SQUARES):
        if board[i] == EMPTY:
            return None
    return TIE


            



    


    
