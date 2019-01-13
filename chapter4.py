#Глава 4

#Функция range - сформировать массив элементов с заданным шагом
for i in range(78):
    print(i, end=", ")
print("\n-------")
for j in range(1, 10):
    print(j, end=" ")
print("\n-------")
for k in range(100, 0, -3):
    print(k, end=" ")

#Кортеж
inventory = ()
if not inventory:
    print("Вы безоружны!")
input("\nНажмите Enter, чтобы продолжить.")
inventory = ("топор", "копьё",
             "щит")
print("Содержимое инвентаря:")
print(inventory)
for item in inventory:
    print("Этот жалкий(ое) " + item + " вам не поможет!")
print("В вашем распоряжении ", len(inventory), " предмет(а/ов)")
chest = ("журнал для взрослых",)
print("Содержимое сундука:")
print(chest)
inventory += chest
print("Содержимое инвентаря:")
print(inventory)
input("\nНажмите Enter, чтобы выйти.")
