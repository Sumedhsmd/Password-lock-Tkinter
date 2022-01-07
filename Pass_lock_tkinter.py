from tkinter import *

window = Tk()
window.title('Password lock')
window.geometry("320x200")

password = 1729

input_label = Label(window, text=" Enter Pin :", font=("Arial ", 17))
input_label.grid(column=0, row=0)

input_pass = Entry(window, width=14)
input_pass.grid(column=1, row=0)

alert_label = Label(window, text="!Enter 4 digit Number", font=("Arial ", 7), fg='red')
alert_label.grid(column=1, row=1)

confirmation = Label(window, text="", font=("Arial ", 15))
confirmation.grid(column=0, row=3)


def clicked():
    pin = int(input_pass.get())
    if len(str(pin)) == 4:
        if pin == password:
            confirmation.config(text='Correct Pin ...')
        else:
            confirmation.config(text='"Incorrect Pin ...."')
    else:
        alert_label.config(text='Minimum 4 Numbers')


submit = Button(window, text='Enter', bg='white', fg='black', command=clicked)
submit.grid(column=1, row=2)


window.mainloop()