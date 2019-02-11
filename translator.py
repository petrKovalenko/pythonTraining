#переводчик
trans = { "хрустобулочник" : "Чувак, фанатеющий от \
Российской Империи, и с тоской вспоминающий 'хруст французской булки'",
          "бандерлог" : "Чувак, любящий/восхваляющий Степана Бандеру",
          "соловьиный помёт" : "Шоу с Владимиром Соловьёвым" }
print("Весь словарь: ", end="\t")
print(trans)
print("Например, определение хрустобулочника:", end='\t')
print(trans["хрустобулочник"])
print("Определение либераста:", end='\t')
print(trans.get("либераст", "Такого понятия нет. Вы можете добавить его в словарь."))


choice = None
while choice != '0':
    print(
        """
Переводчик политического жаргона
0 - Выйти
1 - Найти описание термина
2 - Добавить термин
3 - Изменить описание термина
4 - Удалить термин
5 - Вывести все термины
"""
        )
    choice = input("Ваш выбор: ")
    if choice == "1":
        item_descr = input("Введите термин для истолкования:")
        print(trans.get(item_descr, "Такого понятия нет. Вы можете добавить его в словарь."))
    elif choice == "2":
        item_key = input("Введите термин")        
        if not item_key:
            print("Термин не может быть пустым")
            continue
        if item_key in  trans:
            print("Термин уже существует!")
        item_val = input("Введите описание термина")
        if not item_val:
            print("Термин не может быть пустым")
            continue
        trans[item_key] = item_val
        print("Термин " + item_key + " добавлен в словарь!")
    elif choice == "3":
        item_key = input("Введите термин, у которого нужно изменить описание.")
        if item_key in trans:
            item_val = input("Введите описание термина")
            if not item_val:
                trans[item_key] = item_val
                print("У термина " + item_key + " изменено описание: '" + item_val + "'" )
            else:
                print("Описание не может быть пустым")
        else:            
            print("Термина '" + item_key + "' нет в словаре!")
    elif choice == "4":
        item_key = input("Введите термин, который нужно удалить.")
        if not item_key  in trans:
            print("Термина '" + item_key + "' нет в словаре!")
            continue
        del trans[item_key]
        print("Термин '" + item_key + "'удалён!")
    elif choice == "5":
        print(trans.keys())
            



input("/n/nНажмите Enter чтобы выйти.")
