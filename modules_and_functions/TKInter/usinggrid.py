import tkinter



mainwindow = tkinter.Tk()
mainwindow.title("hello World")
mainwindow.geometry('640x480-8-400')

label = tkinter.Label(mainwindow, text = "hello world!, How are you")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainwindow)
leftFrame.grid(row=1,column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=5)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainwindow)
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button4 = tkinter.Button(rightFrame, text="button4")

button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)
button4.grid(row=3,column=0)

mainwindow.columnconfigure(0,weight=2)
mainwindow.columnconfigure(1,weight=2)
mainwindow.columnconfigure(2,weight=2)
mainwindow.columnconfigure(3,weight=2)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky = 'ns')
rightFrame.grid(sticky = 'new')

rightFrame.columnconfigure(0,weight = 1)
button2.grid(sticky='ew')
mainwindow.mainloop()



