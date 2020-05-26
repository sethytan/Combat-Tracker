from tkinter import *
import os
import sqlite3

class DropDown:

    def __init__(self, place, row, column, type, table):
        """Initialise new drop down object.
            Arguments:
            -place: used to indicate the window or frame it's located
            -type: used to show the right word on buttons
            -table: used to specify the Database table to edit
        """
        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()
        cursor.execute('Select * FROM ' + table)
        self.records = cursor.fetchall()

        self.creatures = []

        for record in self.records:
            self.creatures.append(record[1])

        print(self.creatures)

        self.frame = LabelFrame(place, bd=0)
        self.frame.grid(row=row, column=column)

        self.creature = StringVar()
        self.creature.set(type)
        print(self.creature)


        self.dropdown = OptionMenu(self.frame, self.creature, *self.creatures)
        self.dropdown.grid(row=0, column=0)

        self.button = Button(self.frame, text='Add ' + type, command=self.add_creature, state=DISABLED)
        self.button.grid(row=0, column=1)

        self.creature.trace('w', self.callback)

        conn.close()

    def callback(self, *args):
        if combatants:
            for combatant in (combatants or []):
                if combatant == self.creature.get():
                    self.button['state'] = DISABLED
                    break
                else:
                    self.button['state'] = NORMAL
        else:
            self.button['state'] = NORMAL


    def add_creature(self):
        combatants.append(self.creature.get())
        print(combatants)
        self.callback()



if __name__ == '__main__':
    root = Tk()
    root.geometry('200x200')
    combatants = []
    active = BooleanVar()
    active = False
    dd = DropDown(root, 1, 1, 'Player', 'players')


    root.mainloop()
