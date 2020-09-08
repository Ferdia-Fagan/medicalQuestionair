from tkinter import *

from windows.MenuWindow import MenuWindow
from windows.WindowBase import WindowBase


class ApplicationState:

    def __init__(self, starting_state):
        self.root = Tk()

        self.root.geometry("1280x850")
        self.root.title("Application")

        WindowBase.set_application_controller(self)

        self.current_state = starting_state(self.root)
        self.root.mainloop()

    def change_state(self, new_state, **state_args):
        # for el in self.current_state.winfo_children():
        #     el.destroy()
        self.current_state.destroy()
        self.current_state = new_state(self.root, *state_args)
        self.root.mainloop()


if __name__ == '__main__':
    inst = ApplicationState(MenuWindow)

    # main_frame = Frame(root,bg="red", width=1000, height=600)

    # root.pack()
    # label = Label(inst, text="Label", justify=LEFT)
    # label.pack(side=LEFT)

    # root.mainloop()
