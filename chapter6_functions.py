#chapter 6
#functions
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
# пример функции со множеством входов и множеством выходов
def oneTwoOutputs(one, two):
    return two,one
# функция с именоваными параметрами
def iAmAlcoholic(firstMsg, name = "Михалыч", status = "шопоголик"):
    print(firstMsg + " Меня зовут " + name + " и я " + status + ".")
#main
print("Инструкция к игре:")
instructions()
first = input("\nВведите превое значение!")
second = input("\nВведите второе значение!")
firstRet, secondRet = oneTwoOutputs(first, second)
print("Первое значение:" + firstRet)
print("Второе значение:" + secondRet)

iAmAlcoholic("Здравствуйте!")
iAmAlcoholic("Здорово", status = "алкоголик")
iAmAlcoholic("Приветик", "Света", "нимфоманка")
iAmAlcoholic("Хай!", name = "ЛСДУЗ")
iAmAlcoholic("Добрый вечер", status = "трудоголик", name ="Гоша")
input("\n\n Нажмите Enter чтобы выйти!")

    
