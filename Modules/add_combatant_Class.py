from tkinter import *
import os
import sqlite3
from Modules.config import combatants
from Modules.Tracker_Row_Class import Trow
from Modules.Delete_Row_Button import DelRow

class DropDown:

    def __init__(self, place, row, column, columnspan, type, table, master, info, delete):
        """Initialise new drop down object.
            Arguments:
            -place: used to indicate the window or frame it's located
            -type: used to show the right word on buttons
            -table: used to specify the Database table to edit
        """
        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()
        cursor.execute('Select * FROM ' + table)
        self.table = table
        self.records = cursor.fetchall()
        self.type = type
        self.creatures = [self.type]

        for record in self.records:
            self.creatures.append(record[1])
            if len(self.creatures) > 1 and self.creatures[0] == self.type:
                del self.creatures[0]

        print(self.creatures)

        self.frame = LabelFrame(place, bd=0)
        self.frame.grid(row=row, column=column, columnspan=columnspan)

        self.creature = StringVar()
        self.creature.set(type)
        print(self.creature)


        self.dropdown = OptionMenu(self.frame, self.creature, *self.creatures )
        self.dropdown.config(width=6)
        self.dropdown.grid(row=0, column=0)

        self.button = Button(self.frame, text='Add ' + type, command=lambda: self.add_creature(table, master, info, delete, type), state=DISABLED)
        self.button.grid(row=0, column=1)

        self.creature.trace('w', self.callback)

        conn.close()
        self.rowspan =  None

    def call_creatures(self, table, type):
        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()
        cursor.execute('Select * FROM ' + table)
        self.records = cursor.fetchall()
        conn.close()
        self.record_names = [record[1] for record in self.records]
        print(self.record_names)
        self.dropdown.grid_forget()
        for record in self.record_names:
            if record not in self.creatures:
                self.creatures.append(record)

        for creature in self.creatures:
            if creature not in self.record_names:
                self.creatures.remove(creature)

        if len(self.creatures) > 1 and self.creatures[0] == self.type:
            del self.creatures[0]

        self.creature.set(type)
        self.dropdown = OptionMenu(self.frame, self.creature, *self.creatures )
        self.dropdown.grid(row=0, column=0)


    def callback(self, *args):
        if combatants:
            for combatant in (combatants or []):
                if self.creature.get() == (combatant[0].name['text'] or self.type):
                    self.button['state'] = DISABLED
                    break
                else:
                    self.button['state'] = NORMAL
        else:
            if self.creature.get() == self.type:
                self.button['state'] = DISABLED
            else:
                self.button['state'] = NORMAL


    def add_creature(self, table, master, info, delete, type):
        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()
        cursor.execute('Select * FROM ' + table + ' WHERE name=?', (self.creature.get(),))
        self.table_records = cursor.fetchone()
        conn.close()
        print(self.table_records)
        if self.rowspan is not None:
            print('yes')
            self.rowspan += 1
        else:
            print('no')
            self.rowspan = 2

        master.grid_configure(rowspan=self.rowspan)

        tracker_row = len(combatants) +1
        row = Trow(master, tracker_row, self.table_records[1],
                   self.table_records[2], self.table_records[3],
                   self.table_records[4], self.table_records[5],
                   self.table_records[6], self.table_records[7],
                   self.table_records[8], self.table_records[9],
                   self.table_records[10], self.table_records[11],
                   self.table_records[12], self.table_records[13],
                   self.table_records[14], info)

        delete = DelRow(master, tracker_row)

        combatant = [row, delete]
        combatants.append(combatant)

        print(combatants)
        self.creature.set(type)
        self.callback()



if __name__ == '__main__':
    root = Tk()
    root.geometry('200x200')
    combatants = []
    active = BooleanVar()
    active = False
    dd = DropDown(root, 1, 1, 'Player', 'players')


    root.mainloop()
