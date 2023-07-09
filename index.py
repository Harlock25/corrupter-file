import tkinter as tk
from tkinter import *
from tkinter import messagebox
from start_window import StartWindow
from information import InformationWindow
from PIL import Image, ImageTk

class Fullscreen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("")
        self.window.resizable(True,True)
        self.window.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.config(background="red")

        self.label_title = Label(self.window, text="FILE CORRUPTOR", font=("Arial", 45, "bold"), bg="red", fg="white")
        self.label_title.pack(pady=50)

        self.start_button = Button(self.window, text="START", height=3, width=15, command=self.open_start_window, font=("Arial", 18), bg="blue", fg="white")
        self.start_button.pack(padx=40, pady=120)

        self.information_button = Button(self.window, text="INFORMATION", height=3, width=15, command=self.Information, font=("Arial", 18), bg="green", fg="white")
        self.information_button.pack(padx=40, pady=50)

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def open_start_window(self):
        start_window = StartWindow(self.window)

    def Information(self):
        information = InformationWindow(self.window)

if __name__ == '__main__':
    app = Fullscreen()
