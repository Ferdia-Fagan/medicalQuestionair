from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
from tkinter import filedialog

import tkinter.font as tkfont

from windows.QuestionaireGeneratorWindow import QuestionaireGeneratorWindow
from windows.WindowBase import WindowBase


class CreateQuestionairPopup(Frame,WindowBase):

    def __init__(self,parent):
        self.parent = parent
        # self.app_contr=app_contr
        super().__init__(self.parent, bg="red")
        self.pack(expand=True)
        # self.place(relx=.5, rely=.5)  # center

        # self.pack_propagate(0)
        # self.pack(fill="none", expand=True)

        explore_files = Button(self,
                                text="Browse for folder",
                                command=self.browseFiles)
        explore_files.pack(pady=25)

        parent_folder_frame = Frame(self)
        parent_folder_frame.pack(in_=self,pady=25)

        parent_folder_label = Label(parent_folder_frame, text="Parent folder path:")
        parent_folder_label.pack(side=LEFT)

        xscrollbar = Scrollbar(parent_folder_frame, orient=HORIZONTAL)
        xscrollbar.pack(side=BOTTOM, fill=X)
        # self.font = tkfont.Font(family="Consolas", size=10, weight="normal")
        self.parent_folder_text=Text(parent_folder_frame, height=2,width=30, wrap=NONE,
                                     xscrollcommand=xscrollbar.set)
        self.parent_folder_text.pack(expand=True,fill='both')
        self.parent_folder_text.insert(tk.END, "?")
        xscrollbar.config(command=self.parent_folder_text.xview)

        file_name_frame = Frame(self)
        file_name_frame.pack(in_=self,pady=25)

        file_name_label = Label(file_name_frame, text="File name")
        file_name_label.pack(side=LEFT)
        self.file_name_entry = Entry(file_name_frame)
        self.file_name_entry.pack(side=LEFT)

        create_btn=Button(self,text="Create",command=self.create_questionair)
        create_btn.pack()

        self.pack(expand=True)

    def changed_parent_folder(self, parent_foldr_path):
        """
        Set view of questionair parent folder path
        :param parent_foldr_path:
        :return:
        """
        self.parent_folder_text.delete("1.0", tk.END)
        self.parent_folder_text.insert(tk.END, parent_foldr_path)


    def browseFiles(self):
        """
        Opens filesystem browser.
        Used to select parent folder, were will create questionair json file.
        :return:
        """
        self.parent_foldr_path = filedialog.askdirectory() + "/"
        self.changed_parent_folder(self.parent_foldr_path)

    def create_questionair(self):
        """
        creates questionair with
        self.parent_foldr_path and  self.file_name_entry value.
        Questionair is a json file.
        :return:
        """
        # create = open(self.parent_foldr_path + self.file_name_entry.get() + ".json", "w+")
        # create.close()
        self.change_state(QuestionaireGeneratorWindow)


