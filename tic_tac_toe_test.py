#тест функций из tic_tac_toe.py

import tic_tac_toe
#определяем константами, какие функции тестить
TEST_INSTRUCT = 0
TEST_ASK_Y_N = 0
TEST_ASK_NUM = 1

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

input("/n/n Нажмите Enter, чтобы выйти!")
