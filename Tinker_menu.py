import tkinter as tk
from tkinter import messagebox as mb
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

import os
import sys
from functools import partial

class UI(ThemedTk):

    def __init__(self):
        ThemedTk.__init__(self)

        #create menu
        menubar = tk.Menu(self) # assign SELF to the created menu

        #add menuitems 
        menus =[]
        for i in range(4):
            menu= tk.Menu(menubar, tearoff =0)
            menu.add_command(label = f"Command{i}.1=pass", command = None)
            menu.add_command(label = f"Command{i}.2=restartUI", command = partial(restart_UI, self))
            menus.append(menu)

            menubar.add_cascade(label = f"Menu{i+1}", menu=menus[-1])

        #add menubar to the tinker app
        self.config(menu = menubar) 
        return


def restart_UI(obj):
    python = sys.executable
    os.execl(python, python, * sys.argv)

app = UI()
app.mainloop()
