#крестики нолики
#импорт
import random
#import sys

#глобальные константы
CROSS = "X"
ZERO = "0"
EMPTY = " "
TIE = "Ничья"
SQUARE_STEP = 3
NUM_SQUARES = SQUARE_STEP * SQUARE_STEP
WINNING_SEQ = "PW"
DANGEROUS_SEQ = "PD"
USELESS_SEQ = "US"
UNCLASSIFIED_SEQ = "UN"

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
#возвращает памятку по клеткам    
def short_instructions():
    print(
    """
    Числа соответсвуют полям, как показано а рисунке ниже.
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8\n
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

#принимает на вход доску и типфишк игрока
#возвращает доску, на которой сделан ход игрока
def human_move(board, human):
    #выводит памятку
    short_instructions()
    while True:
    #спрашивает у игрока номер, куда походить
        human_input = ask_number("Введите число, которое соответсвует клетке, куда вы хотите пойти.", 0, NUM_SQUARES - 1)
        #если игрок выбрал не занятую клетку, возвращаем обновлённую доску, иначе - спрашиваем опять
        if board[human_input] == EMPTY:
            board[human_input] = human
            return board
        print("Вы выбрали уже занятую клетку. Пожалуйста, выберите пустую клетку")

#вспомогательная функция для функции computer_move
#классифицирует последовательности на выигрышные, опасные, безполезные (нельзя не проиграть не победить)
#принимает на вход последовательность, её длину, ходы компьютера и человека
#возвращает тип строки - WINNING_SEQ, DANGEROUS_SEQ, USELESS_SEQ, UNCLASSIFIED_SEQ
def classify_sequnce(seq, seq_len, computer, human):
    computer_signs = 0
    human_signs = 0
    for i in range(0, seq_len):
        if seq[i] == computer:
            computer_signs+=1
        if seq[i] == human:
            human_signs+=1
    #предвыигрышная ситуация
    if computer_signs == SQUARE_STEP - 1:
        return WINNING_SEQ
    #опасная ситуация
    if human_signs == SQUARE_STEP - 1:
        return DANGEROUS_SEQ
    #безполезная строка
    if computer_signs > 0 and human_signs > 0:
        return USELESS_SEQ
    return UNCLASSIFIED_SEQ

#вспомогательная функция для функции computer_move
#принимает на вход доску, индекс пустого символа, результат классификации и символ хода компьютера
#возвращает доску с ходом, или None в случае если это не победа. В случае изьяна в логике возвращает AssertionError
def winning_move(board, empty_index, class_result, computer):
    if class_result == WINNING_SEQ:
        assert (empty_index >= 0), "Произошла ошибка в логике - empty_index равен " + str(empty_index) + " при результате классификации WINNING_SEQ"
        board[empty_index] = computer
        print("Компьютер походил в клетку " + str(empty_index))
        return board
    return None

#вспомогательная функция для функции computer_move
#принимает на вход dangerous_indicies, индекс пустого символа, результат классификации и символ хода компьютера
#возвращает dangerous_indicies, или None в случае если это не победа. В случае изьяна в логике возвращает AssertionError
def dangerous_move(dangerous_indicies, empty_index, class_result):
    if class_result == DANGEROUS_SEQ:
        assert (empty_index >= 0), "Произошла ошибка в логике - empty_index равен " + str(empty_index) + " при результате классификации DANGEROUS_SEQ"
        if not str(empty_index) in dangerous_indicies:
            dangerous_indicies[str(empty_index)] = 1       
    return dangerous_indicies

#принимает на вход доску, тип фишек игрока и компьютера
#возвращает доску, на которой сделан ход компьютера
def computer_move(board, computer, human):
    #plan
    #классифицируем все строки и диагональ
    #если можем выиграть где-то - выигрываем
    #если опасная ситуация - перекрываем проходы
    #если центр свободен - занимаем центр
    #если опасности нет и центр занят ходим в любую точку, где есть шанс победить

    #если есть опасная ситуация, складываем сюда индексы, которые нужно заполнить для избежания опасной ситуации - победы игрока
    dangerous_indicies = {}
    #главная диагональ md
    sequence = []
    empty_index = -1
    for i in range(0, SQUARE_STEP):
        sequence[i] = board[i + SQUARE_STEP*i]
        if sequence[i] == EMPTY:
            empty_index = i
    class_result_md = classify_sequnce(sequence, SQUARE_STEP, computer, human)
    win_brd = winning_move(board, empty_index, class_result_md, computer)
    if win_brd:
        return win_brd    
    dangerous_indicies = dangerous_move(dangerous_indicies, empty_index, class_result_md)

    #обратная диагональ rd
    sequence = []
    empty_index = -1
    for i in range(0, SQUARE_STEP):
        sequence[i] = board[(i + 1) * (SQUARE_STEP - 1)]
        if sequence[i] == EMPTY:
            empty_index = i
    class_result_rd = classify_sequnce(sequence, SQUARE_STEP, computer, human)
    win_brd = winning_move(board, empty_index, class_result_rd, computer)
    if win_brd:
        return win_brd    
    dangerous_indicies = dangerous_move(dangerous_indicies, empty_index, class_result_rd)

    #строки
    class_result_rows = []*SQUARE_STEP
    for j in range(0, SQUARE_STEP):
        sequence = []
        empty_index = -1
        for i in range(0, SQUARE_STEP):
            sequence[i] = board[SQUARE_STEP*j + i]
            if sequence[i] == EMPTY:
                empty_index = i
        class_result_rows[j] = classify_sequnce(sequence, SQUARE_STEP, computer, human)
        win_brd = winning_move(board, empty_index, class_result_rows[j], computer)
        if win_brd:
            return win_brd    
        dangerous_indicies = dangerous_move(dangerous_indicies, empty_index, class_result_rows[j])

    #столбцы
    class_result_cols = []*SQUARE_STEP
    for j in range(0, SQUARE_STEP):
        sequence = []
        empty_index = -1
        for i in range(0, SQUARE_STEP):
            sequence[i] = board[j + i*SQUARE_STEP]
            if sequence[i] == EMPTY:
                empty_index = i
        class_result_cols[j] = classify_sequnce(sequence, SQUARE_STEP, computer, human)
        win_brd = winning_move(board, empty_index, class_result_cols[j], computer)
        if win_brd:
            return win_brd    
        dangerous_indicies = dangerous_move(dangerous_indicies, empty_index, class_result_cols[j])

    #если есть опасный ход - выполнить первый
    if len(dangerous_indicies.keys()) > 0:
        assert (board[int(dangerous_indicies.keys()[0])] == EMPTY), "Произошла ошибка в логике программы - компьютер пытается сделать ход на уже занятую клетку"
        board[int(dangerous_indicies.keys()[0])] = computer
        return board

    #проверяем маршруты, по которым стоит 'ходить'. Предпочтение - в центр
    #главная диагональ
    if class_result_md == UNCLASSIFIED_SEQ:
        #если нечётное число клеток квадарта - то предпочтение в центр
        if SQUARE_STEP % 2 == 1:
            if board[(NUM_SQUARES // 2)] == EMPTY:
                board[(NUM_SQUARES // 2)] = computer
                return board
        #если чётное - то один из центральных диагональных квадратов
        else:
            if board[ ((SQUARE_STEP // 2) - 1) * (SQUARE_STEP + 1)  ] == EMPTY:
                board[ ((SQUARE_STEP // 2) - 1) * (SQUARE_STEP + 1)  ] = computer
                return board
            if board[ ((SQUARE_STEP // 2) + 1) * (SQUARE_STEP + 1)  ] == EMPTY:
                board[ ((SQUARE_STEP // 2) + 1) * (SQUARE_STEP + 1)  ] = computer
                return board
    #обртаная диагональ    
    if class_result_rd == UNCLASSIFIED_SEQ:  
        if SQUARE_STEP % 2 == 1:
            if board[(NUM_SQUARES // 2)] == EMPTY:
                board[(NUM_SQUARES // 2)] = computer
                return board
        else:
            if board[ ((SQUARE_STEP // 2) - 1) * (SQUARE_STEP + 1) + 1] == EMPTY:
                board[ ((SQUARE_STEP // 2) - 1) * (SQUARE_STEP + 1) + 1] = computer
                return board
            if board[ ((SQUARE_STEP // 2) + 1) * (SQUARE_STEP + 1) -  1] == EMPTY:
                board[ ((SQUARE_STEP // 2) + 1) * (SQUARE_STEP + 1) - 1] = computer
                return board
    #строки и столбцы
    
    
