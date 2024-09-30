import tkinter

from PIL.ImageOps import expand

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# # tkinter._test()
mainwindow = tkinter.Tk()
#
mainwindow.title("hello World")
mainwindow.geometry('400x400+8+400')
# mainwindow.mainloop()

label = tkinter.Label(mainwindow, text = "hello world!, How are you")
label.pack(side ='top')

leftFrame = tkinter.Frame(mainwindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand = False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainwindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button4 = tkinter.Button(rightFrame, text="button4")
# button1.pack(side='right')
# button2.pack(side='top')
# button3.pack(side='bottom')
# button4.pack(side='left')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
button4.pack(side='top')

mainwindow.mainloop()



