#анаграммы
import random

#берём слова из файла
file = open('anagram.txt', 'r', encoding='UTF8')
text = file.read()
print("Содержимое файла: " + text)
#преобразование в кортеж
words = tuple(text.split(" "))
print("Кортеж:")
print(words)

input("\n\nНажмите Enter, чтобы выйти.")
