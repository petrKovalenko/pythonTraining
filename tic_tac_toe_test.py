#тест функций из tic_tac_toe.py

import tic_tac_toe
#определяем константами, какие функции тестить
TEST_INSTRUCT = 1
TEST_ASK_Y_N = 1
if TEST_INSTRUCT == 1:
    print("Тест функции tic_tac_toe.instructions")
    tic_tac_toe.instructions()

if TEST_ASK_Y_N == 1:
    print("Тест функции tic_tac_toe.ask_yes_no")
    answer  = tic_tac_toe.ask_yes_no("Вы когда-нибудь хотели стать фламинго?")
    print("В итоге Вы ответили: " + answer)

input("/n/n Нажмите Enter, чтобы выйти!")
