#тест функций из tic_tac_toe.py

import tic_tac_toe
#примеры досок
#выигрыш по диагонали
BOARD_ONE = [tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.EMPTY,
                                              tic_tac_toe.CROSS, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.CROSS]
#нет выигрыша
BOARD_TWO = [tic_tac_toe.ZERO, tic_tac_toe.ZERO, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.CROSS]
#выигрыш по обратной диагонали
BOARD_THREE = [tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.ZERO,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.ZERO,
                                              tic_tac_toe.ZERO, tic_tac_toe.ZERO, tic_tac_toe.CROSS]
#win upper row
BOARD_FOUR = [tic_tac_toe.CROSS, tic_tac_toe.CROSS, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.CROSS]
#win middle row
BOARD_FIVE = [tic_tac_toe.ZERO, tic_tac_toe.ZERO, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.ZERO, tic_tac_toe.ZERO,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.CROSS]
#win bottom row
BOARD_SIX = [tic_tac_toe.ZERO, tic_tac_toe.ZERO, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.CROSS, tic_tac_toe.CROSS, tic_tac_toe.CROSS]
#win left column
BOARD_SEVEN = [tic_tac_toe.ZERO, tic_tac_toe.ZERO, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.ZERO, tic_tac_toe.ZERO, tic_tac_toe.CROSS]
#win middle column
BOARD_EIGHT = [tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.CROSS]
#win right column
BOARD_NINE = [tic_tac_toe.ZERO, tic_tac_toe.ZERO, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.CROSS]
#ничья!
BOARD_TIE = [tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.CROSS,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.CROSS]
#non filled diag
EMPTY_DIAG = [tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.CROSS,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.EMPTY]

#non filled reverse diag
EMPTY_RV_DIAG = [tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.EMPTY]

#partly filled second column
EMPTY_SECOND_COL = [tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY]

#partly filled third row
EMPTY_THIRD_ROW = [tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.ZERO]

#cross to win main diag
ABOUT_TO_WIN_MD = [tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.CROSS]

#cross to win main diag 2
ABOUT_TO_WIN_MD2 = [tic_tac_toe.CROSS, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.CROSS]

#cross to win main diag 3
ABOUT_TO_WIN_MD3 = [tic_tac_toe.CROSS, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.EMPTY]


#cross to win reverse diag 1
ABOUT_TO_WIN_RD1 = [tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.ZERO]

#cross to win reverse diag 2
ABOUT_TO_WIN_RD2 = [tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.EMPTY]

#cross to win reverse diag 3
ABOUT_TO_WIN_RD3 = [tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.CROSS,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.EMPTY]

#cross to win row 1
ABOUT_TO_WIN_ROW1 = [tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.CROSS,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.ZERO]

#cross to win row 2
ABOUT_TO_WIN_ROW2 = [tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.CROSS, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY]

#cross to win row 3
ABOUT_TO_WIN_ROW3 = [tic_tac_toe.ZERO, tic_tac_toe.CROSS, tic_tac_toe.ZERO,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.CROSS, tic_tac_toe.EMPTY, tic_tac_toe.CROSS]

#cross to win col 1
ABOUT_TO_WIN_COL1 = [tic_tac_toe.CROSS, tic_tac_toe.EMPTY, tic_tac_toe.ZERO,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.CROSS, tic_tac_toe.ZERO, tic_tac_toe.EMPTY]
#cross to win col 2
ABOUT_TO_WIN_COL2 = [tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.ZERO]
#cross to win col 3
ABOUT_TO_WIN_COL3 = [tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.CROSS,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.EMPTY]

#empty board
EMPTY_BOARD = [tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY]

#перспективная главная диагональ
PERSPECTOVE_MD = [tic_tac_toe.CROSS, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY]
#перспективная обратная диагональ
PERSPECTOVE_RD = [tic_tac_toe.CROSS, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.CROSS, tic_tac_toe.EMPTY, tic_tac_toe.ZERO]
#перспективная главная и обратная диагональ
PERSPECTOVE_MD_RD = [tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.EMPTY]

#perspective moves 1
P_MV_1 = [tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY]
#perspective moves 2
P_MV_2 = [tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.CROSS, tic_tac_toe.EMPTY,
                                              tic_tac_toe.ZERO, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY]
#perspective moves 3
P_MV_3= [tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.CROSS,
                                              tic_tac_toe.EMPTY, tic_tac_toe.ZERO, tic_tac_toe.EMPTY,
                                              tic_tac_toe.EMPTY, tic_tac_toe.EMPTY, tic_tac_toe.EMPTY]

#определяем константами, какие функции тестить
TEST_INSTRUCT = 0
TEST_ASK_Y_N = 0
TEST_ASK_NUM = 0
TEST_IS_FIRST_TURN = 0
TEST_NEWBOARD = 0
TEST_DISPLAYBOARD = 0
TEST_LEGEL_MOVES = 0
TEST_WINNING = 0
TEST_HUMAN_MOVE = 0
TEST_fill_random_empty_cell = 0
TEST_random_sequence = 0
TEST_computer_move = 1
TEST_computer_move_about_to_win = 0
TEST_computer_move_about_to_loose = 0
TEST_computer_move_diagonal_first = 0
TEST_computer_move_perspective_moves = 1

if TEST_random_sequence == 1:
    print("Тест функции tic_tac_toe.random_sequence")
    print("From -1 to 12 (3 times)")
    print(tic_tac_toe.random_sequence(-1, 12))
    print(tic_tac_toe.random_sequence(-1, 12))
    print(tic_tac_toe.random_sequence(-1, 12))

    print("From 0 to 3 (3 times)")
    print(tic_tac_toe.random_sequence(0, 3))
    print(tic_tac_toe.random_sequence(0, 3))
    print(tic_tac_toe.random_sequence(0, 3))

    print("From 8 to 16 (3 times)")
    print(tic_tac_toe.random_sequence(8, 16))
    print(tic_tac_toe.random_sequence(8, 16))
    print(tic_tac_toe.random_sequence(8, 16))

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
    print("Новая доска: " + str(newBoardList))

if TEST_DISPLAYBOARD == 1:
    print("Тест функции tic_tac_toe.display_board")
    tic_tac_toe.display_board(BOARD_ONE)
    tic_tac_toe.display_board([tic_tac_toe.CROSS])
    tic_tac_toe.display_board(None)

if TEST_LEGEL_MOVES == 1:
    print("Тест функции tic_tac_toe.legal_moves")
    legalMovesList = tic_tac_toe.legal_moves(BOARD_ONE)
    print("Легальные ходы: " + str(legalMovesList))
    legalMovesList = tic_tac_toe.legal_moves(BOARD_TWO)
    print("Легальные ходы 2: " + str(legalMovesList))
    legalMovesList = tic_tac_toe.legal_moves(None)
    legalMovesList = tic_tac_toe.legal_moves([tic_tac_toe.CROSS])
    legalMovesList = tic_tac_toe.legal_moves(["","","","","","","","","","","","","","","","","","","","",""])

if TEST_WINNING == 1:
    print("Тест функции tic_tac_toe.winner")
    tic_tac_toe.display_board(BOARD_ONE)
    isWinning1 = tic_tac_toe.winner(BOARD_ONE)
    print("Выигрыш: " + isWinning1)

    tic_tac_toe.display_board(BOARD_TWO)
    isWinning2 = tic_tac_toe.winner(BOARD_TWO)
    if not isWinning2:
        isWinning2 = "Нет выигрыша"
    print("Выигрыш: " + isWinning2)

    tic_tac_toe.display_board(BOARD_THREE)
    isWinning2 = tic_tac_toe.winner(BOARD_THREE)
    print("Выигрыш: " + isWinning2)

    tic_tac_toe.display_board(BOARD_FOUR)
    isWinning2 = tic_tac_toe.winner(BOARD_FOUR)
    print("Выигрыш: " + isWinning2)

    tic_tac_toe.display_board(BOARD_FIVE)
    isWinning2 = tic_tac_toe.winner(BOARD_FIVE)
    print("Выигрыш: " + isWinning2)

    tic_tac_toe.display_board(BOARD_SIX)
    isWinning2 = tic_tac_toe.winner(BOARD_SIX)
    print("Выигрыш: " + isWinning2)

    tic_tac_toe.display_board(BOARD_SEVEN)
    isWinning2 = tic_tac_toe.winner(BOARD_SEVEN)
    print("Выигрыш: " + isWinning2)

    tic_tac_toe.display_board(BOARD_EIGHT)
    isWinning2 = tic_tac_toe.winner(BOARD_EIGHT)
    print("Выигрыш: " + isWinning2)

    tic_tac_toe.display_board(BOARD_NINE)
    isWinning2 = tic_tac_toe.winner(BOARD_NINE)
    print("Выигрыш: " + isWinning2)

    tic_tac_toe.display_board(BOARD_TIE)
    isWinning2 = tic_tac_toe.winner(BOARD_TIE)
    print("Выигрыш: " + isWinning2)
    

if TEST_HUMAN_MOVE == 1:
    print("Тест функции tic_tac_toe.human_move на первой доске")
    tic_tac_toe.display_board(BOARD_ONE)
    newboard = tic_tac_toe.human_move(BOARD_ONE, tic_tac_toe.CROSS)
    print("Доска полсе хода игрока")
    tic_tac_toe.display_board(newboard)

    print("Тест функции tic_tac_toe.human_move на второй доске")
    tic_tac_toe.display_board(BOARD_TWO)
    newboard = tic_tac_toe.human_move(BOARD_TWO, tic_tac_toe.ZERO)
    print("Доска после хода игрока")
    tic_tac_toe.display_board(newboard)

if TEST_fill_random_empty_cell == 1:
    print("Тест вспомогательной функции tic_tac_toe.fill_random_empty_cell с функцией выбора строки tic_tac_toe.main_diag")
    tic_tac_toe.display_board(EMPTY_DIAG)
    newboard = tic_tac_toe.fill_random_empty_cell(EMPTY_DIAG, -1, tic_tac_toe.main_diag, tic_tac_toe.CROSS)
    print("Доска после заполнения:")
    tic_tac_toe.display_board(newboard)

    print("Тест вспомогательной функции tic_tac_toe.fill_random_empty_cell с функцией выбора строки tic_tac_toe.reverse_diag")
    tic_tac_toe.display_board(EMPTY_RV_DIAG)
    newboard = tic_tac_toe.fill_random_empty_cell(EMPTY_RV_DIAG, -1, tic_tac_toe.reverse_diag, tic_tac_toe.CROSS)
    print("Доска после заполнения:")
    tic_tac_toe.display_board(newboard)

    print("Тест вспомогательной функции tic_tac_toe.fill_random_empty_cell с функцией выбора строки tic_tac_toe.column")
    tic_tac_toe.display_board(EMPTY_SECOND_COL)
    newboard = tic_tac_toe.fill_random_empty_cell(EMPTY_SECOND_COL, 1, tic_tac_toe.column, tic_tac_toe.CROSS)
    print("Доска после заполнения:")
    tic_tac_toe.display_board(newboard)

    print("Тест вспомогательной функции tic_tac_toe.fill_random_empty_cell с функцией выбора строки tic_tac_toe.row")
    tic_tac_toe.display_board(EMPTY_THIRD_ROW)
    newboard = tic_tac_toe.fill_random_empty_cell(EMPTY_THIRD_ROW, 2, tic_tac_toe.row, tic_tac_toe.CROSS)
    print("Доска после заполнения:")
    tic_tac_toe.display_board(newboard)

if TEST_computer_move == 1:
    print("Тест функции tic_tac_toe.computer_move на первой доске")
    tic_tac_toe.display_board(EMPTY_THIRD_ROW)
    newboard = tic_tac_toe.computer_move(EMPTY_THIRD_ROW, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
    print("Доска после хода компьютера:")
    tic_tac_toe.display_board(newboard)

#-------------------------------Tests about to win-----------------------------------------------------------------
    if TEST_computer_move_about_to_win == 1:
        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_MD")
        tic_tac_toe.display_board(ABOUT_TO_WIN_MD)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_MD, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_MD2")
        tic_tac_toe.display_board(ABOUT_TO_WIN_MD2)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_MD2, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        
        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_MD3")
        tic_tac_toe.display_board(ABOUT_TO_WIN_MD3)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_MD3, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard) 

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_RD1")
        tic_tac_toe.display_board(ABOUT_TO_WIN_RD1)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_RD1, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_RD2")
        tic_tac_toe.display_board(ABOUT_TO_WIN_RD2)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_RD2, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_RD3")
        tic_tac_toe.display_board(ABOUT_TO_WIN_RD3)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_RD3, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)
        

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_ROW1")
        tic_tac_toe.display_board(ABOUT_TO_WIN_ROW1)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_ROW1, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_ROW2")
        tic_tac_toe.display_board(ABOUT_TO_WIN_ROW2)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_ROW2, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_ROW3")
        tic_tac_toe.display_board(ABOUT_TO_WIN_ROW3)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_ROW3, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_COL1")
        tic_tac_toe.display_board(ABOUT_TO_WIN_COL1)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_COL1, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_COL2")
        tic_tac_toe.display_board(ABOUT_TO_WIN_COL2)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_COL2, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_COL3")
        tic_tac_toe.display_board(ABOUT_TO_WIN_COL3)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_COL3, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

#-------------------------------Tests about to loose (computer is ZERO)-----------------------------------------------------------------
    if TEST_computer_move_about_to_loose == 1:
        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_MD - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_MD)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_MD, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_MD2 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_MD2)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_MD2, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        
        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_MD3 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_MD3)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_MD3, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard) 

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_RD1 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_RD1)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_RD1, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_RD2 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_RD2)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_RD2, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_RD3 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_RD3)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_RD3, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)
        

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_ROW1 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_ROW1)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_ROW1, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_ROW2 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_ROW2)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_ROW2, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_ROW3 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_ROW3)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_ROW3, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_COL1 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_COL1)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_COL1, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_COL2 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_COL2)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_COL2, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске ABOUT_TO_WIN_COL3 - about to loose(comp is ZERO)")
        tic_tac_toe.display_board(ABOUT_TO_WIN_COL3)
        newboard = tic_tac_toe.computer_move(ABOUT_TO_WIN_COL3, tic_tac_toe.ZERO, tic_tac_toe.CROSS)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

#-------------------------------Tests perspective center-----------------------------------------------------------------

    if TEST_computer_move_diagonal_first == 1:
        print("Тест функции tic_tac_toe.computer_move на доске EMPTY_BOARD")
        tic_tac_toe.display_board(EMPTY_BOARD)
        newboard = tic_tac_toe.computer_move(EMPTY_BOARD, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске PERSPECTOVE_MD")
        tic_tac_toe.display_board(PERSPECTOVE_MD)
        newboard = tic_tac_toe.computer_move(PERSPECTOVE_MD, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске PERSPECTOVE_RD")
        tic_tac_toe.display_board(PERSPECTOVE_RD)
        newboard = tic_tac_toe.computer_move(PERSPECTOVE_RD, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске PERSPECTOVE_MD_RD")
        tic_tac_toe.display_board(PERSPECTOVE_MD_RD)
        newboard = tic_tac_toe.computer_move(PERSPECTOVE_MD_RD, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

#-------------------------------Tests perspective moves-----------------------------------------------------------------
    if TEST_computer_move_perspective_moves == 1:
        print("Тест функции tic_tac_toe.computer_move на доске P_MV_1")
        tic_tac_toe.display_board(P_MV_1)
        newboard = tic_tac_toe.computer_move(P_MV_1, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске P_MV_2")
        tic_tac_toe.display_board(P_MV_2)
        newboard = tic_tac_toe.computer_move(P_MV_2, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)

        print("Тест функции tic_tac_toe.computer_move на доске P_MV_3")
        tic_tac_toe.display_board(P_MV_3)
        newboard = tic_tac_toe.computer_move(P_MV_3, tic_tac_toe.CROSS, tic_tac_toe.ZERO)
        print("Доска после хода компьютера:")
        tic_tac_toe.display_board(newboard)
input("/n/n Нажмите Enter, чтобы выйти!")
