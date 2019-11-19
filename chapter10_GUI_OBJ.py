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
        self.label.grid()
        self.btn = Button(self, text = "Щёлкните для изменеия текста", command = self.labelChange)
        self.btn.grid()        

    def labelChange(self):
        rnd_num = random.randint(0, len(Application.label_prhases) - 1)
        self.btn["text"] = "Щёлкните для изменения текста " + str(rnd_num)
        self.label["text"] =  Application.label_prhases[rnd_num]
        

root_window = Tk()
root_window.title("Окошко в колпаке:)")
root_window.geometry("300x350")
app = Application(root_window)
root_window.mainloop()
