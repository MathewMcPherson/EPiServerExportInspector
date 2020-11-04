import tkinter
from tkinter import filedialog
class DisplayWorker(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.MenuDisplay()
        
    def MenuDisplay(self):
        self.selectFileButton = tkinter.Button(self, text="Select File", command=self.selectFile)
        
    def selectFile(self):
        file = tkinter.filedialog.askopenfile(more="r")
        print(file)
