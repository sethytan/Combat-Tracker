from tkinter import *
import os
import sqlite3
from Modules.config import combatants

class DelRow:

    def __init__(self, root, row):
        self.row = row
        print(self.row)
        self.delete_frame = LabelFrame(root, bd=2, relief=FLAT, padx=5)
        self.delete_frame.grid(row=row, column=0, sticky=N+E+S+W)
        self.delete_button = Button(self.delete_frame, text='X', command=self.delete_row, relief=FLAT)
        self.delete_button.grid(row=0, column=0, sticky=N+E+S+W)
        self.delete_frame.grid_rowconfigure(0, weight=1)
        self.delete_frame.grid_columnconfigure(0, weight=1)

    def call_row(self):
        self.delete_frame.grid_configure(row=self.row)

    def del_row(self):
        self.delete_button.grid_forget()
        self.delete_frame.grid_forget()

    def delete_row(self):
        for combatant in combatants:
            if combatant[0].row == self.row:
                self.i = combatants.index(combatant)
                combatant[0].del_row()
                combatant[1].del_row()
                del combatants[self.i]
                for combatant in combatants:
                    if combatants.index(combatant) >= self.i:
                        combatant[0].row -= 1
                        combatant[0].call_row()
                        combatant[1].row -= 1
                        combatant[1].call_row()
