#chapter7 - exeption example
print("Обработка исключений - пример")
try:
    #i = input("Введите что-нибудь кому-нибудь!")
    #test = 0 / 0
    print(float("ahahahah"))
except ZeroDivisionError:
    print("Dividing by zero!")
except (TypeError, ValueError) as ex:
    print("Это не похоже на число")
    print(ex)
else :
    print("Ошибок нет!")
