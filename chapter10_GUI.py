#chapter 10 - simple GUI
from tkinter import *
#creation and starting window
root_window = Tk()
root_window.title("Окошко в кокошнике:)")
root_window.geometry("444x333")
#creationg frame and objects
main_frame = Frame(root_window)
main_frame.grid() #менеджер размещения, без него не выводится на экран
btn1 = Button(main_frame, text="Кнопка1")
btn1.grid()
lb = Label(main_frame, text="Просто метка, ничего больше")
lb.grid()
btn2 = Button(main_frame)
btn2.configure(text="AHAHAHAHAH!")
btn2.grid()
btn3 = Button(main_frame)
btn3["text"] = "Я помню чудное...."
btn3.grid()
btn2.grid()
#starting mainloop - execute window and do smthng
root_window.mainloop()
