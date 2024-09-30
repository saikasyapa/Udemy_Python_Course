import os
import tkinter



mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry("640x480-8-200")
mainwindow['padx'] = 8

label = tkinter.Label(mainwindow,text="Tkinter Grid Demo")
label.grid(row=0, column = 0, columnspan= 3)

mainwindow.columnconfigure(0,weight=1)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2,weight=3)
mainwindow.columnconfigure(3,weight=3)
mainwindow.columnconfigure(4,weight=3)

mainwindow.rowconfigure(0,weight=1)
mainwindow.rowconfigure(1,weight=10)
mainwindow.rowconfigure(2,weight=1)
mainwindow.rowconfigure(3,weight=3)
mainwindow.rowconfigure(4,weight=3)

fileList = tkinter.Listbox(mainwindow)
fileList.grid(row=1,column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('C:\Windows\System32'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row =1, column = 1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set


###Frame for radiobuttons

optionFrame = tkinter.LabelFrame(mainwindow, text = "File Details")
optionFrame.grid(row=1, column=2, sticky='ne')
optionFrame.config(border=3, relief='sunken')
rbValue = tkinter.IntVar()
rbValue.set(0)

radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

#### widget to display Result Label
resultLabel = tkinter.Label(mainwindow, text="Result")
resultLabel.grid(row=2, column = 2, sticky = 'nw')
result = tkinter.Entry(mainwindow)
result.grid(row=2, column = 2, sticky = 'sw')

#### Frame for the time spinners
timeFrame = tkinter.LabelFrame(mainwindow, text = "Time")
timeFrame.grid(row=3, column=0, sticky='new')
## Time spinners
hours_spinner = tkinter.Spinbox(timeFrame, width = 2, values=tuple(range(0,24)))
minutes_spinner = tkinter.Spinbox(timeFrame, width = 2, values=tuple(range(0,60)))
seconds_spinner = tkinter.Spinbox(timeFrame, width = 2, values=tuple(range(0,60)))
hours_spinner.grid(row=0, column = 0)
tkinter.Label(timeFrame, text=':').grid(row = 0, column=1)
minutes_spinner.grid(row=0, column = 2)
tkinter.Label(timeFrame, text=':').grid(row = 0, column=3)
seconds_spinner.grid(row=0, column = 4)
tkinter.Label(timeFrame, text=':').grid(row = 0, column=1)
timeFrame['padx'] = 36
timeFrame['pady'] = 10

# Frame for the date spinners

dateFrame = tkinter.Frame(mainwindow)
dateFrame.grid(row=4, column = 0, sticky = 'new')
#date labels
day_label = tkinter.Label(dateFrame, text='Day')
month_label = tkinter.Label(dateFrame, text='Month')
year_label = tkinter.Label(dateFrame, text='Year')
day_label.grid(row=0, column=0, sticky='w')
month_label.grid(row=0, column=1, sticky='w')
year_label.grid(row=0, column=2, sticky='w')
#Date spinners
date_spinner = tkinter.Spinbox(dateFrame, width=5, from_=1 , to=31 )
month_spinner = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May','Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov','Dec') )
year_spinner = tkinter.Spinbox(dateFrame, width=5, from_=2000 , to=3000 )
date_spinner.grid(row=1, column = 0)
month_spinner.grid(row=1, column = 1)
year_spinner.grid(row=1, column = 2)
dateFrame['padx'] = 36
dateFrame['pady'] = 10

#Buttons
ok_button = tkinter.Button(mainwindow, text="Ok")
cancel_button = tkinter.Button(mainwindow, text='Cancel', command=mainwindow.quit)
ok_button.grid(row=4, column = 3, sticky='e')
cancel_button.grid(row=4, column = 4, sticky='w')
mainwindow.mainloop()

print(rbValue.get())