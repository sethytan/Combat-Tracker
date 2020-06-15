from tkinter import *
from Modules.config import combatants

class SortButton:
    def __init__(self, root, text):
        self.button = Button(root, text=text, command=self.sort)
        self.button.pack()

    def sort(self):
        combatants.sort(key=self.get_value, reverse=True)
        for combatant in combatants:
            combatant[0].row = combatants.index(combatant) + 1
            combatant[1].row = combatants.index(combatant) + 1
            combatant[0].call_row()
            combatant[1].call_row()


    def get_value(self, combatant):
        return combatant[0].init.get()
