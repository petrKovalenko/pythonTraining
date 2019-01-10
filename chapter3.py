#Глава 3
#импортируем модулёк random
import random

userInput = 'n'
#введение имени
name = ""
while not name:
    name = input("Введите пожалуйста своё имя!")

while(userInput.lower() != 'q'):
    dice1 = random.randint(1, 6)
    dice2 = random.randrange(6) + 1
    total = dice1 + dice2
    print("Первый бросок: ", dice1)
    print("Второй бросок: ", dice2)
    print("Всего: ", total)
    if total > 10:
        print("Очень удачный бросок, "+name+"!")
    elif total > 8:
        print("Удачный бросок, "+name+"!")
    elif total > 6:
        print("Нормальный бросок, "+name+".")
    else:
        print("Не очень удачный бросок, "+name+" :)")
    userInput = input("\n\nНажми q, чтобы выйти")


