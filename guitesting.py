import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload File & read',width=30,font=my_font1)
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File',
   width=20,command = lambda:upload_file())
b1.grid(row=2, column=1)

def upload_file():
    file = filedialog.askopenfilename()
    fob=open(file,'r')
    print(fob.read())
    #file = filedialog.askopenfile()
    #print(file.read())
my_w.mainloop()  # Keep the window open