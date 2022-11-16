from tkinter import *

window = Tk()
window.resizable(False, False)

frame1 = Frame(window)

label1 = Label(frame1, text='My Tic Tac Toe', fg='red', font=("Arial", 15))
label1.pack()


def btn_clicked(value):
	pass

frame2 = Frame(window)
btn1 = Button(frame2, text='X', height=8, width=11, command=Lambda:btn_clicked(1))
btn2 = Button(frame2, text='X', height=8, width=11, command=btn_clicked(2))
btn3 = Button(frame2, text='X', height=8, width=11)
btn4 = Button(frame2, text='X', height=8, width=11)
btn5 = Button(frame2, text='X', height=8, width=11)
btn6 = Button(frame2, text='X', height=8, width=11)
btn7 = Button(frame2, text='X', height=8, width=11)
btn8 = Button(frame2, text='X', height=8, width=11)
btn9 = Button(frame2, text='X', height=8, width=11)

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)


window.mainloop()