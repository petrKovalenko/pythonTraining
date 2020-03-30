#json generator
#generates sample json for uploading in Vertica
if len(sys.argv < 3):
    print("На вход подаётся 2 аргумента - имя файла и количество строк!")
else:
    file = open(sys.argv[1], 'w', encoding='UTF8')
    linesNumber = int(sys.argv[2])
