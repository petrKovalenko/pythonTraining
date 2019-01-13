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

#случайный выбор слова
word = random.choice(words)
#correct = word
t_word = tuple(word)
numbers = []
t_w_len = len(t_word)
#заполняем массив случайных нмоеров, по которым потом будем строить
#анаграмму
while len(numbers) < t_w_len :
    index = random.randint(0, t_w_len-1)
    if index in numbers:
        index_rigth = index
        found = False
        while index_rigth < t_w_len:
            index_rigth++            
            if not index_rigth in numbers:
                found = True
                break
        if not found:
            while index > 0:
                index--
                if not index in numbers:
                    break
        else
            index = index_rigth
    numbers.push(index)
print("Number list:")
print(numbers)

#формируем новое слово
jumble = ""
for num in numbers:
    jumble += word[num]
print("ОТгадайте слово: " + jumble)

input("\n\nНажмите Enter, чтобы выйти.")
