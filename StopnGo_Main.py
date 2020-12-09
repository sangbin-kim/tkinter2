from tkinter import *
from tkinter import filedialog
import RunProgram

window = Tk()
window.title('StopnGo Analysis App')
window.geometry('300x100')

def open():
	window.filename = filedialog.askopenfilename(title="Select A File", filetypes=(("CSV files", "*.csv"),))

def Runn():
    RunProgram.runapp(window.filename)

dialog_btn = Button(window, text = "Import Recipe", command = open)
dialog_btn.grid(column = 1, row =1, padx = 0.5, pady = 10)
dialog_btn.place(relx=0.5, rely=0.5,  anchor='s')
run_btn = Button(window, text = "Run", command = Runn)
run_btn.grid(column = 1, row =2, padx = 0.5, pady = 10)
run_btn.place(relx=0.5, rely=0.5, anchor='n')
window.mainloop()