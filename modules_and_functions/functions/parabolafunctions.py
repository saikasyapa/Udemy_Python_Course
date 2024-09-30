import tkinter

def parabola(x):
    y = x * x / 100
    return y


def draw_axis(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.config(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin,0,x_origin,0, fill='sky blue', width=2)
    canvas.create_line(0,y_origin,0,-y_origin, fill='sky blue', width=2)
    print(locals())


def plot(canvas,x,y):
    canvas.create_line(x,y,x+1,y+1, fill='green', width=3)



mainwindow = tkinter.Tk()
mainwindow.title("Parabola")
mainwindow.geometry('640x480')

canvas = tkinter.Canvas(mainwindow, width=320, height=480)
canvas.grid(row = 0, column = 0)

canvas1 = tkinter.Canvas(mainwindow, width=320, height=480, background='light yellow')
canvas1.grid(row = 0, column = 1)

draw_axis(canvas)
draw_axis(canvas1)

for x in range(-100,100):
    y = parabola(x)
    plot(canvas,x,-y)

mainwindow.mainloop()