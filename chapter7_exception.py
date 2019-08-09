#chapter7 - exeption example
print("Обработка исключений - пример")
try:
    #test = 0 / 0
    print(float("ahahahah"))
except ZeroDivisionError:
    print("Dividing by zero!")
except (TypeError, ValueError):
    print("Это не похоже на число")
