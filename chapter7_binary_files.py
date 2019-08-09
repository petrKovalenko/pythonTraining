#Запись и чтение данных в бинарный файл
import pickle, shelve
#консервация - pickle
numb = 17
strange_string = "achtung zog!"
cortage = ("A tebe", "есть", 18)
my_list = [1, 2, 3, "druga"]
my_dict = {"kill" : ["Bill", "Bob", "Quentin"], "mein" : ("teil", "hertz")}

#writing
file = open("pickle.dat", "wb")
file_text = open("pickle_txt.dat", "wb")

pickle.dump(numb, file, True)
pickle.dump(strange_string, file, True)
pickle.dump(cortage, file, True)
pickle.dump(my_list, file, True)
pickle.dump(my_dict, file, True)

pickle.dump(numb, file_text, False)
pickle.dump(strange_string, file_text, False)
pickle.dump(cortage, file_text, False)
pickle.dump(my_list, file_text, False)
pickle.dump(my_dict, file_text, False)

file.close()
file_text.close()

#reading
file_r = open("pickle.dat", "rb")
file_text_r = open("pickle_txt.dat", "rb")

print("Читаем из файлов:")
print(pickle.load(file_r))
print(pickle.load(file_text_r))
print(pickle.load(file_r))
print(pickle.load(file_text_r))
print(pickle.load(file_r))
print(pickle.load(file_text_r))
print(pickle.load(file_r))
print(pickle.load(file_text_r))
print(pickle.load(file_r))
print(pickle.load(file_text_r))

#shelve
print("\nПомещение списков на полку.")
s = shelve.open("pickles2.dat")
s['Moscow'] = ("red square", 'mausoleum', 'MSU')
s['StPetersburg'] = ["Nevsky", "Kronshtadt"]
s.sync()
s.close()

s = shelve.open("pickles2.dat", 'r')
print(s['StPetersburg'])
s.close()
