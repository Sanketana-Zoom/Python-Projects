from tkinter import *

window = Tk()

# Change Window Title
window.title("Formatting Widget Application")

# Change Window Height and Width
window.geometry("650x500")

# Change the background color of window
window.configure(bg='white')

label1 = Label(window, text='Label with Padx and PadY', bg='black', fg='white', padx = 20, pady = 20)

button1 = Button(window, text='Click Me!')

label2 = Label(window, text='Label with iPadx, iPady', bg='blue', fg='red')

label1.pack(fill = X)
button1.pack(pady = 20)
label2.pack(ipadx=50, ipady=50)



window.mainloop()