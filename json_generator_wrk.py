#json generator
#generates sample json for uploading in Vertica
#На вход подаётся минимум 2 аргумента - имя файла и количество строк
#ещё 1 аргумент - кол-во файлов
import sys
import random
import json
import datetime
import math
import string
import copy

TIME_OFFSET_MAX_SEC = 100000
RECORD_CLASSES = ("ABC", "XYZ", "LYC", "MSK")
RECORD_MODEL = {
    "time_key": "DATETIME",
    "class_key":"CLASS",
    "int_key":"INT",
    "str_key1":"STR",
    "str_key2":"STR",
    "str_key3":"STR",
    "str_key4":"STR",
    "str_key5":"STR",
    "str_key6":"STR",
    "int_key2":"INT",
    "int_key3":"INT",
    "int_key4":"INT",
    "int_key5":"INT",
    "int_key6":"INT",
    "time_key2": "DATETIME",
    "time_key3": "DATETIME",
    "time_key4": "DATETIME",
    "time_key5": "DATETIME",
    "time_key6": "DATETIME",
    "again_time_key": "DATETIME",
    "again_class_key":"CLASS",
    "again_int_key":"INT",
    "again_str_key1":"STR",
    "again_str_key2":"STR",
    "again_str_key3":"STR",
    "again_str_key4":"STR",
    "again_str_key5":"STR",
    "again_str_key6":"STR",
    "again_int_key2":"INT",
    "again_int_key3":"INT",
    "again_int_key4":"INT",
    "again_int_key5":"INT",
    "again_int_key6":"INT",
    "again_time_key2": "DATETIME",
    "again_time_key3": "DATETIME",
    "again_time_key4": "DATETIME",
    "again_time_key5": "DATETIME",
    "again_time_key6": "DATETIME",
    "and_again_time_key": "DATETIME",
    "and_again_class_key":"CLASS",
    "and_again_int_key":"INT",
    "and_again_str_key1":"STR",
    "and_again_str_key2":"STR",
    "and_again_str_key3":"STR",
    "and_again_str_key4":"STR",
    "and_again_str_key5":"STR",
    "and_again_str_key6":"STR",
    "and_again_int_key2":"INT",
    "and_again_int_key3":"INT",
    "and_again_int_key4":"INT",
    "and_again_int_key5":"INT",
    "and_again_int_key6":"INT",
    "and_again_time_key2": "DATETIME",
    "and_again_time_key3": "DATETIME",
    "and_again_time_key4": "DATETIME",
    "and_again_time_key5": "DATETIME",
    "and_again_time_key6": "DATETIME"
    }
STR_LEN_MIN = 3
STR_LEN_MAX = 40

def generateDatetime():
    return datetime.datetime.fromtimestamp( datetime.datetime.now().timestamp() +  random.randint(-TIME_OFFSET_MAX_SEC, TIME_OFFSET_MAX_SEC))

def generateInt():
    return random.randint(-TIME_OFFSET_MAX_SEC, TIME_OFFSET_MAX_SEC)

def generateClass():
    return random.choice(RECORD_CLASSES)

def generateString():
    strLen = random.randint(STR_LEN_MIN, STR_LEN_MAX)
    return ''.join(random.choice(string.ascii_lowercase) for i in range(strLen))        

##def generateRecord():
##    nowTime = datetime.datetime.now().timestamp() 
##    timeOffset = random.randint(-TIME_OFFSET_MAX_SEC, TIME_OFFSET_MAX_SEC)
##    randTime = datetime.datetime.fromtimestamp(nowTime + timeOffset)
##    randClass = random.choice(RECORD_CLASSES)
##    randInt = timeOffset
##    return {"time_key": str(randTime), "class_key": randClass, "int_key": randInt}

def generateRecord():
    curRecord = copy.deepcopy(RECORD_MODEL)
    for key in curRecord.keys():
        if curRecord[key] == "DATETIME":
           curRecord[key] = str(generateDatetime());
           continue;
        if curRecord[key] == "CLASS":
            curRecord[key] = generateClass();
            continue;
        if curRecord[key] == "INT":
            curRecord[key] = generateInt();
            continue;
        if curRecord[key] == "STR":
            curRecord[key] = generateString();
            continue;
        #if nothing mathced, place UNKNOWN_TYPE
        curRecord[key] == "UNKNOWN TYPE, NO MATHED VALUE"
    return curRecord

def generateFile(fileName, linesNumber):
    file = open(fileName, 'w', encoding='UTF8')
    data = []
    for i in range(1, linesNumber+1):
        data.append(generateRecord())
    json.dump(data, file, indent=2)
    file.close()

#-------BEGIN----------------    
if len(sys.argv) < 3:
    print("На вход подаётся минимум 2 аргумента - имя файла и количество строк!")
else:
    if len(sys.argv) == 3:
        generateFile(sys.argv[1], int(sys.argv[2]))
    else:
        filesAmount = int(sys.argv[3])
        stringsPerFile = math.ceil(int(sys.argv[2]) / filesAmount)
        for j in range(filesAmount):
            generateFile(sys.argv[1].replace(".", str(j + 1) + "."), stringsPerFile)
            
    
