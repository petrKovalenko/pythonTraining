#Ussless facts by PFK
name = input("Привет, как тебя зовут?: ")
age =  int(input("\nСколько Вам лет?: "))
weight = int(input("\nСколько Вы весите?: "))

print("Если бы трамвайный хам писал Вам в чате, \
он бы обратился так: " , name.lower())
print("А после небольшого спора так: ", name.upper())
fiveTimes = name * 5
print("Если бы маленький ребёнок решил привлечь ваше внимание, \
он произнёс бы Ваше имя так: " + fiveTimes)

age_seconds = age * 365 * 24 * 60 * 60
print("Возраст в секундах: ", age_seconds)

moon_weight = weight / 6
sun_weight = weight * 27.1
print("\nЗнaeтe ли вы. что на Луне вы весили бы всего", moon_weight, "кг?")
print( "\nА вот находясь на Солнце. вы бы весили", sun_weight, "кг. \
(Но. увы. это продолжалось бы недолго.)")

input("\n\nНажми Enter, чтобы выйти")
