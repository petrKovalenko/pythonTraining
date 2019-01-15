#глава 5
#список - модифицируемый тип данных (в отличие от кортежа)
#длина кортежа и списка
arms_list = ["меч", "пилум", "щит_гоплон", "панцирь"]
arms_tuple = ("меч", "пилум", "щит_гоплон", "панцирь")
print("Размер списка", end=": ")
print(arms_list.__sizeof__())
print("Размер кортежа", end=": ")
print(arms_tuple.__sizeof__())

#присвоение срезу списка
print("Начальное снаряжение:")
print(arms_list)
print("После обмена на комплект гоплита.")
arms_list[0:3] = ["копьё", "большой щит"]
print("Снаряжение после изменения:")
print(arms_list)
print("После обмена на комплект лучника.")
arms_list[0:2] = ["лук", "колчан со стрелами", "нож", "щит - баклер"]
print("Снаряжение после изменения:")
print(arms_list)

#удаление из массива
print("После стрельбы вы выросили лук и колчан, чтобы уйти от атаки конницы.")
del arms_list[:2]
print(arms_list)
print("А потом какой-то варвар располовинил ваш щит топором.\
Хорошо, что вы его прирезали!")
del arms_list[1]
arms_list.append("Ухо варвара")
print(arms_list)

input("/n/nНажмите Enter чтобы выйти.")
