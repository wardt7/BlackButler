from tkinter import *
from tkinter import ttk
from tkinter import font

class Inter():
    def __init__(self):
        self.root = Tk()
        self.list = ["hello"]

    def command(self, e):
        print("hello")

    def main(self):
        listbox = Listbox(height=3)
        listbox.grid(column=0, row=0)
        for item in self.list:
            listbox.insert(END,item)
        listbox.bind("<<ListboxSelect>>", self.command)
        self.root.mainloop()

root = Inter()
root.main()


