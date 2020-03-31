#json generator
#generates sample json for uploading in Vertica
#На вход подаётся минимум 2 аргумента - имя файла и количество строк
#ещё 1 аргумент - кол-во файлов
import sys
import random
import json
import datetime
import math

TIME_OFFSET_MAX_SEC = 10000
RECORD_CLASSES = ("ABC", "XYZ", "LYC", "MSK")

def generateRecord():
    nowTime = datetime.datetime.now().timestamp() 
    timeOffset = random.randint(-TIME_OFFSET_MAX_SEC, TIME_OFFSET_MAX_SEC)
    randTime = datetime.datetime.fromtimestamp(nowTime + timeOffset)
    randClass = random.choice(RECORD_CLASSES)
    randInt = timeOffset
    return {"time_key": str(randTime), "class_key": randClass, "int_key": randInt}

def generateFile(fileName, linesNumber):
    file = open(fileName, 'w', encoding='UTF8')
    data = []
    for i in range(1, linesNumber):
        data.append(generateRecord())
    json.dump(data, file, indent=2)
    file.close()

#-------BEGIN----------------    
if len(sys.argv) < 3:
    print("На вход подаётся минимум 2 аргумента - имя файла и количество строк!")
else:
    if len(sys.argv) = 3:
        generateFile(sys.argv[1], int(sys.argv[2]))
    else:
        filesAmount = int(sys.argv[3])
        stringsPerFile = math.ceil(int(sys.argv[2] / filesAmount))
        for j in range(filesAmount):
            generateFile(sys.argv[1].replace(".", "." + (j + 1)), stringsPerFile)
            
    
