import tkinter as tk
from tkinter import *


class InformationWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("information")
        self.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)
        self.config(background="red")
        self.label_title = Label(self, text="FILE CORRUPTOR", font=("Arial",45, "bold"), bg="red", fg="white")
        self.label_title.pack(pady=50)

        self.quote = """
        Welcome to the File Corruptor program! This program allows you to create files in different formats and corrupt them. Here's how you can use the program:

        In the main window of the program, enter the desired file name and extension in the provided fields.
        Click the "CREATE FILE" button.
        The program will create a new file with the specified name and extension in the designated directory.
        Depending on the file extension, the program will create a file in the corresponding format (e.g., PowerPoint, Word, Excel, or text).
        Corrupting an existing file:

        In the main window of the program, click the "OPEN" button.
        Select one or more existing files using the file dialog.
        Choose the file you want to corrupt.
        The program will rename the file and move it to the designated directory.
        The renamed file will be opened, read as text, and rewritten to corrupt its content.
        The corrupted file will be saved with the new encoding.
        Closing the program:

        You can close the program by clicking the "X" in the main window or using the window's close button.
        Enjoy creating and corrupting your files with the File Corruptor program!
        """
        self.label_information = Label(self, text=self.quote, font=("Arial", 16,"italic"), justify="left")
        self.label_information.pack()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)