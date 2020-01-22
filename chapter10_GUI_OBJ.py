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
        self.listButtonPushed = False

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
        #переключатель
        #переменная, которая будет связана с переключателем
        self.listLike = BooleanVar()
        self.listLike.set(1)
        #создание переключателя (не присваиваем его переменной класса)
        Checkbutton(self, text = "Отображать как список", variable = self.listLike, command = self.updateTxt).grid(row = 7, column = 1)
        #Radiobutton
        #variable to collect radiobutton values
        self.theme = StringVar()
        self.theme.set("main")
        #several radiobuttons
        Radiobutton(self,
                    text = "Основная тема",
                    variable = self.theme,
                    value = "main",
                    command = self.updateTheme).grid(row = 8, column = 0)
        Radiobutton(self,
                    text = "Зелёная тема",
                    value = "green",
                    variable = self.theme,
                    command = self.updateTheme).grid(row = 8, column = 1)
        Radiobutton(self,
                    text = "Красная тема",
                    value = "red",
                    variable = self.theme,
                    command = self.updateTheme).grid(row = 9, column = 0)

    def labelChange(self):
        rnd_num = random.randint(0, len(Application.label_prhases) - 1)
        self.btn["text"] = "Щёлкните для изменения текста " + str(rnd_num)
        self.label["text"] =  Application.label_prhases[rnd_num]

    def showVList(self):
        self.listButtonPushed = True
        self.txt1.delete(0.0, END)
        #if representation should be like list
        if self.listLike.get():
            self.txt1.insert(0.0, str(Application.label_prhases))
        else:
            for phrase in Application.label_prhases:
               self.txt1.insert(END, " '" + phrase + "'") 

    def updateTxt(self):
        if self.listButtonPushed:
            self.showVList()

    def updateTheme(self):
        val = self.theme.get()
        if val == "main":
            self.txt1["bg"] = "white"
            self.txt1.configure(fg = "black")
        if val == "green":
            self.txt1["bg"] = "yellow"
            self.txt1.configure(fg = "green")
        if val == "red":
            self.txt1["bg"] = "black"
            self.txt1.configure(fg = "red")

root_window = Tk()
root_window.title("Окошко в колпаке:)")
root_window.geometry("700x350")
app = Application(root_window)
root_window.mainloop()
