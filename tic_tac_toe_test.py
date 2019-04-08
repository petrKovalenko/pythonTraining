#тест функций из tic_tac_toe.py

import tic_tac_toe
#определяем константами, какие функции тестить
TEST_INSTRUCT = 0
TEST_ASK_Y_N = 0
TEST_ASK_NUM = 0
TEST_IS_FIRST_TURN = 0
TEST_NEWBOARD = 1
TEST_DISPLAYBOARD = 1

if TEST_INSTRUCT == 1:
    print("Тест функции tic_tac_toe.instructions")
    tic_tac_toe.instructions()

if TEST_ASK_Y_N == 1:
    print("Тест функции tic_tac_toe.ask_yes_no")
    answer  = tic_tac_toe.ask_yes_no("Вы когда-нибудь хотели стать фламинго?")
    print("В итоге Вы ответили: " + answer)

if TEST_ASK_NUM == 1:
    print("Тест функции tic_tac_toe.ask_number")
    number = tic_tac_toe.ask_number("Введите чисто от -1 до 15", low = -1, high = 15)
    print("В итоге Вы ввели: " + str(number))

if TEST_IS_FIRST_TURN == 1:
    print("Тест функции tic_tac_toe.first_turn")
    userSign,computerSign = tic_tac_toe.first_turn()
    print("Пользовательский знак: " + userSign)
    print("Знак компьютера: " + computerSign)

if TEST_NEWBOARD == 1:
    print("Тест функции tic_tac_toe.new_board")
    newBoardList = tic_tac_toe.new_board()
    print("Пользовательский знак: " + str(newBoardList))

if TEST_DISPLAYBOARD == 1:
    print("Тест функции tic_tac_toe.display_board")
    tic_tac_toe.display_board([tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.EMPTY,
                                              tic_tac_toe.CROSS, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.CROSS])
    tic_tac_toe.display_board([tic_tac_toe.CROSS])
    tic_tac_toe.display_board(None)

input("/n/n Нажмите Enter, чтобы выйти!")
