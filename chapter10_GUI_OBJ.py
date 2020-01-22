#chapter 10 - object GUI
from tkinter import *
import random

class Application(Frame):
    """ Пример использования ООП и графического убогонького интерфейса - но дальше больше"""
    #статический параметр с фразочками
    label_prhases = ["Ну что ты щёлкаешь, как дятел!", "Щелчок мышью - минус одна секунда твоей жизни.",
                     "Энергия, потраченная на щелчок, могла пойти на достижение прогресса, развитие цивилизации. Эххх...",
                     "Чего тут думать - тут щёлкать надо.", "Щёлкнешь ещё раз - словишь BSOD. Да знаешь ли ты что это..."]    
    def __init__(self, window):
        super(Application, self).__init__(window)
        self.grid()
        self.create_scenery()

    def create_scenery(self):
        self.label = Label(self, text="Я милый и пушистый.")
        self.label.grid(columnspan = 4)
        self.btn = Button(self, text = "Щёлкните для изменения текста", command = self.labelChange)
        self.btn.grid()
        #grid example (задаёт размещение объекта)
        self.btn2 = Button(self, text = "Щёлкните для отображения списка вариантов", command = self.showVList)
        self.btn2.grid(row = 1, column = 2, sticky = E)
        self.txt1 = Text(self, width = 40, heigh = 10, wrap = WORD)
        self.txt1.grid(row = 2, column = 0, columnspan = 4, rowspan = 4)

    def labelChange(self):
        rnd_num = random.randint(0, len(Application.label_prhases) - 1)
        self.btn["text"] = "Щёлкните для изменения текста " + str(rnd_num)
        self.label["text"] =  Application.label_prhases[rnd_num]

    def showVList(self):
        self.txt1.delete(0.0, END)
        self.txt1.insert(0.0, str(Application.label_prhases))
        

root_window = Tk()
root_window.title("Окошко в колпаке:)")
root_window.geometry("700x350")
app = Application(root_window)
root_window.mainloop()
