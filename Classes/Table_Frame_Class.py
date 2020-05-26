from tkinter import *
import os
import sqlite3

from config import combatants

class TableFrame:

    def __init__(self, root):
        """Initialise new frame object.
            Arguments:
            -root: the window that the frame will be placed in
        """

        self.frame = LabelFrame(root)
        self.frame.grid(row=3, column=3, columnspan=3)
