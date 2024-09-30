import tkinter

keys = [[('C', 1), ('CE' , 1)],
        [('7',1), ('8', 1), ('9' , 1), ('+', 1)],
        [('4' , 1), ('5' , 1), ('6' , 1), ('-', 1)],
        [('1' , 1), ('2' , 1), ('3' , 1), ('*', 1)],
        [('0' , 1), ('=' , 1),('/', 1)],
        ]


mainwindowpadding= 8
mainwindow=tkinter.Tk()
mainwindow.title("Calculator")
mainwindow.geometry('640x480-8-200')
mainwindow['padx'] = mainwindowpadding

result = tkinter.Entry(mainwindow)
label = tkinter.Label(text="Result")
result.grid(row=0, column=3, sticky='nsew')
label.grid(row=0, column=2, sticky='nsew')

keypad = tkinter.Frame(mainwindow)
keypad.grid(row=1, column=0, sticky = 'nsew')

row=0
for key_row in keys:
    col=0
    for key in key_row:
        tkinter.Button(keypad, text=key[0]).grid(row=row, column = col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col = col +key[1]
    row = row + 1
mainwindow.update()
mainwindow.minsize(keypad.winfo_width() + mainwindowpadding, result.winfo_height() + keypad.winfo_height())
mainwindow.maxsize(keypad.winfo_width() + mainwindowpadding, result.winfo_height() + keypad.winfo_height())
mainwindow.mainloop()