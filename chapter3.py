#Глава 3
#импортируем модулёк random
import random

userInput = 'n'

while(userInput.lower() != 'q'):
    dice1 = random.randint(1, 6)
    dice2 = random.randrange(6) + 1
    total = dice1 + dice2
    print("Первый бросок: ", dice1)
    print("Второй бросок: ", dice2)
    print("Всего: ", total)
    if total > 6:
        print("Удачный бросок!")
    else:
        print("Не очень удачный бросок :)")
    userInput = input("\n\nНажми q, чтобы выйти")


