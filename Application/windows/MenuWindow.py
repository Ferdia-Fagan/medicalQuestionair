
from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
from tkinter import filedialog

from Application.windows.popups.CreateQuestionairPopup import CreateQuestionairPopup
from Application.windows.WindowBase import WindowBase


class MenuWindow(Frame,WindowBase):

    def __init__(self,parent):
        menu_options = [("Create", self.create),
                        ("List Library", self.list_library)
                        ]
        self.parent=parent
        # self.app_contr=app_contr
        # Set up menu frame
        # self.bigFrame = Frame(parent)
        super().__init__(parent,bg="blue",width=500,height=500)
        self.pack_propagate(0)
        self.pack(fill="none", expand=True)

        for menu_opt,x in menu_options:
            button = Button(self, text=menu_opt,command=x)
            button.pack(pady=30)

        self.pack()

    def create(self):
        print("create")
        popup = CreateQuestionairPopup(self.parent)
        # popup.pack(expand=True)
        popup.place(relx=.5, rely=.5, relheight=0.5,relwidth=0.5,anchor="center")  # center
        self.pack()

    def list_library(self):
        print("list library")
        pass


def browseFiles():
    # filename = filedialog.askopenfilename(initialdir="/",
    #                                       title="Select a File",
    #                                       filetypes=(("Text files",
    #                                                   "*.txt*"),
    #                                                  ("all files",
    #                                                   "*.*")))
    foldername = filedialog.askdirectory() + "/"

    print("the file name is ", foldername)

    # Change label contents
    # label_file_explorer.configure(text="File Opened: " + foldername)
