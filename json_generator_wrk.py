#json generator
#generates sample json for uploading in Vertica
import random
import json
import datetime

TIME_OFFSET_MAX_SEC = 10000
RECORD_CLASSES = ("ABC", "XYZ", "LYC", "MSK")

def generateRecord():
    nowTime = datetime.datetime.now()
    timeOffset = random.randint(-TIME_OFFSET_MAX_SEC, TIME_OFFSET_MAX_SEC)
    randTime = datetime.datetime.fromtimestamp(nowTime + timeOffset)
    randClass = random.choice(RECORD_CLASSES)
    randInt = timeOffset
    return {"time_key": str(randTime), "class_key": randClass, "int_key": randInt}
    
if len(sys.argv < 3):
    print("На вход подаётся 2 аргумента - имя файла и количество строк!")
else:
    file = open(sys.argv[1], 'w', encoding='UTF8')
    linesNumber = int(sys.argv[2])
    if linesNumber <= 0:
        print("Кол-во строк дожно быть больше 0!")
    else:
        data = []
        for i in range(1, linesNumber):
            data.append(generateRecord())
        json.dump(data, file, ident=2)
        file.close()
