import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()


def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)


myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='yellow', fg='black', font=10)
canvas.create_window(150, 150, window=myButton)

root.mainloop()