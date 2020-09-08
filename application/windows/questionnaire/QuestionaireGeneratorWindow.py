from tkinter import *
from tkinter import Tk, ttk

from application.windows.questionnaire.QuestionaireTab import QuestionaireTab

class QuestionaireGeneratorWindow(Frame):

    def __init__(self,parent):
        self.parent=parent
        super().__init__(parent, bg="blue")

        header = Frame(self,height=70, bg="red")
        header.pack_propagate(0)
        header.pack(fill=X, pady=(0, 20))

        menu_btn = Button(header,bg="blue", text="menu")
        menu_btn.pack(side=LEFT,fill=BOTH,padx=5,pady=5,expand=True)

        add_tab_btn = Button(header,bg="blue", text="add tab", command=self.create_new_tab)
        add_tab_btn.pack(side=LEFT,fill=BOTH,padx=5,pady=5,expand=True)

        exit_btn = Button(header,bg="blue", text="exit")
        exit_btn.pack(side=LEFT,fill=BOTH,padx=5,pady=5,expand=True)

        # header2 = Frame(self, bg="purple")
        # header2.pack(fill=BOTH, expand=True,pady=80)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(side=BOTTOM)
        self.frame1 = QuestionaireTab(self.notebook)
        self.notebook.add(self.frame1, text = 'One')
        self.notebook.pack(fill=BOTH, expand=1)

        self.tab_menu=Button(self,bg="pink", text="menu")
        # self.tab_menu.pack(side=BOTTOM, padx=5, pady=5)
        self.tab_menu.place(relx=1, rely=1,anchor="se")

        self.pack(fill=BOTH, expand=True)

    def create_new_tab(self):
        self.popup=Frame(self,bg="blue",width=100,height=100)
        self.popup.pack()
        self.popup.place(relx=.5, rely=.5,anchor="center")  # center

        self.l=Label(self.popup,text="Name of new tab?")
        self.l.pack()
        self.e=Entry(self.popup)
        self.e.pack()

        def create_tab():
            if (tab_name:=self.e.get()) is not '':
                print(tab_name)
                self.create_tab(tab_name)
            self.popup.destroy()

        self.b=Button(self.popup,text='Ok',command=create_tab)
        self.b.pack()


    def create_tab(self, new_tab_name):
        new_tab=QuestionaireTab(self.notebook)
        self.notebook.add(new_tab, text=new_tab_name)