from tkinter import *
import os
import sqlite3

class NewWindow:

    def __init__(self, title, type, table, dropdowns):
        """Initialise new window object.
            Arguments:
            -title: the window's title, also used to locate a folder
            -type: used to show the right word on buttons
            -table: used to specify the Database table to edit
        """
        self.window = Toplevel()
        self.window.title(title)
        self.window.iconbitmap('Statblocks/Icon.ico')
        self.window.geometry('430x240')
        self.window.focus_force()

        self.statblock_file_l = NONE

        #create the frames
        self.input_frame = LabelFrame(self.window)
        self.input_frame.grid(row=0, column=0,
                              columnspan=8, ipadx=2)

        self.button_frame = LabelFrame(self.window, bd=0)
        self.button_frame.grid(row=1, column=0,
                               columnspan=8, rowspan=2,
                               ipadx=2, sticky=W)

        self.list_frame = LabelFrame(self.window, text=title)
        self.list_frame.grid(row=1, column=5,
                             columnspan=4, rowspan=4,
                             padx=(10,0), sticky=N)

        self.spell_frame = LabelFrame(self.input_frame, text='Spell Slots')
        self.spell_frame.grid(row=0, column=7,
                              rowspan=3, columnspan=3,
                              pady=(10, 5), padx=5)

        # create the entry boxes
        self.name = Entry(self.input_frame, width=33)
        self.name.grid(row=0, column=2,
                       padx=(10, 0), pady=(10, 0),
                       columnspan=5, sticky=W)
        self.hp = Entry(self.input_frame, width=5)
        self.hp.grid(row=1, column=2,
                     padx=(10, 0), sticky=W)
        self.ac = Entry(self.input_frame, width=3)
        self.ac.grid(row=1, column=4, sticky=W)
        self.dc = Entry(self.input_frame, width=3)
        self.dc.grid(row=1, column=6)
        self.id = Entry(self.input_frame, width=2)
        self.id.grid(row=2, column=6)
        self.spell_1 = Entry(self.spell_frame, width=3)
        self.spell_1.grid(row=0, column=1)
        self.spell_2 = Entry(self.spell_frame, width=3)
        self.spell_2.grid(row=0, column=3)
        self.spell_3 = Entry(self.spell_frame, width=3)
        self.spell_3.grid(row=0, column=5, padx=(0,5))
        self.spell_4 = Entry(self.spell_frame, width=3)
        self.spell_4.grid(row=1, column=1)
        self.spell_5 = Entry(self.spell_frame, width=3)
        self.spell_5.grid(row=1, column=3)
        self.spell_6 = Entry(self.spell_frame, width=3)
        self.spell_6.grid(row=1, column=5, padx=(0,5))
        self.spell_7 = Entry(self.spell_frame, width=3)
        self.spell_7.grid(row=2, column=1, pady=(0,5))
        self.spell_8 = Entry(self.spell_frame, width=3)
        self.spell_8.grid(row=2, column=3, pady=(0,5))
        self.spell_9 = Entry(self.spell_frame, width=3)
        self.spell_9.grid(row=2, column=5,
                          padx=(0,5), pady=(0,5))

        # Create the Entry labels
        self.name_label = Label(self.input_frame, text='Name:')
        self.name_label.grid(row=0, column=0,
                             columnspan=2, pady=(10,0),
                             padx=(10, 0), sticky=W)
        self.hp_label = Label(self.input_frame, text='Health: ')
        self.hp_label.grid(row=1, column=0, columnspan=2,
                           padx=(10, 0), sticky=W)
        self.ac_label = Label(self.input_frame, text='AC:')
        self.ac_label.grid(row=1, column=3)
        self.dc_label = Label(self.input_frame, text='Save DC:')
        self.dc_label.grid(row=1, column=5)
        self.id_label = Label(self.input_frame, text='ID:')
        self.id_label.grid(row=2, column=5, sticky=E)
        self.spell_1_label = Label(self.spell_frame, text='1st')
        self.spell_1_label.grid(row=0, column=0)
        self.spell_2_label = Label(self.spell_frame, text='2nd')
        self.spell_2_label.grid(row=0, column=2)
        self.spell_3_label = Label(self.spell_frame, text='3rd')
        self.spell_3_label.grid(row=0, column=4)
        self.spell_4_label = Label(self.spell_frame, text='4th')
        self.spell_4_label.grid(row=1, column=0)
        self.spell_5_label = Label(self.spell_frame, text='5th')
        self.spell_5_label.grid(row=1, column=2)
        self.spell_6_label = Label(self.spell_frame, text='6th')
        self.spell_6_label.grid(row=1, column=4)
        self.spell_7_label = Label(self.spell_frame, text='7th')
        self.spell_7_label.grid(row=2, column=0, pady=(0,5))
        self.spell_8_label = Label(self.spell_frame, text='8th')
        self.spell_8_label.grid(row=2, column=2, pady=(0,5))
        self.spell_9_label = Label(self.spell_frame, text='9th')
        self.spell_9_label.grid(row=2, column=4, pady=(0,5))

        # create list labels
        self.list_name_l = Label(self.list_frame, text='Name')
        self.list_name_l.grid(row=0, column=0, padx=(0, 50))
        self.list_id_l = Label(self.list_frame, text='ID')
        self.list_id_l.grid(row=0, column=1)

        # create buttons
        self.statblock_b = Button(self.input_frame,
                                text='statblock',
                                command=lambda: self.call_statblock(title))
        self.statblock_b.grid(row=2, column=0,
                            columnspan=3, padx=(10, 0),
                            pady=(0, 5), ipadx=15)

        self.add_b = Button(self.button_frame,
                          text='Add ' + type + ' to Database',
                          command=lambda: self.submit(table, dropdowns, type))
        self.add_b.grid(row=0, column=0,
                      columnspan=2, rowspan=2,
                      padx=(5, 5), pady=5,
                      ipady=15, ipadx=13, sticky=W)

        self.list_b = Button(self.button_frame,
                           text='Show ' + type + ' list',
                           command=lambda: self.call_list(table))
        self.list_b.grid(row=0, column=2,
                       columnspan=4, pady=(5, 0),
                       ipadx=5, sticky=N)

        self.delete_b = Button(self.button_frame,
                             text='Delete ' + type + ' from Database',
                             command=lambda: self.delete(table, dropdowns, type))
        self.delete_b.grid(row=2, column=0,
                         columnspan=2, rowspan=2,
                         padx=(5, 5), ipady=15, sticky=W)

        self.edit_b = Button(self.button_frame,
                           text='Edit ' + type,
                           command=lambda: self.edit(table))
        self.edit_b.grid(row=1, column=2, columnspan=2,
                       ipadx=19, pady=(0, 5))

        self.save_b = Button(self.button_frame,
                           text='Save Changes',
                           command=lambda: self.save(table, dropdowns, type),
                           state=DISABLED)
        self.save_b.grid(row=2, column=2,
                       columnspan=2, ipadx=10)

        self.cancel_b = Button(self.button_frame,
                             text='Cancel Changes',
                             command=self.cancel,
                             state=DISABLED)
        self.cancel_b.grid(row=3, column=2,
                         columnspan=2, ipadx=4)

        self.window.mainloop()


    def call_statblock(self, title):
        if  self.statblock_file_l is not NONE:
            self.statblock_file_l.grid_forget()
            self.statblock_file_l = NONE

        self.statblock_file = filedialog.askopenfilename(initialdir='Statblocks/' + title,
                                                         title='select a file',
                                                         filetypes=(('png files', '*.png'),
                                                                    ('all files', '*.*')))
        self.window.lift()
        self.path = os.path.relpath(self.statblock_file, os.getcwd())
        self.statblock_file_l = Label(self.input_frame,
                                      text=os.path.basename(self.path))
        self.statblock_file_l.grid(row=2, column=3, columnspan=3,
                                   padx=(0, 15), pady=(0, 5))


    def call_list(self, table):
        for label in self.list_frame.grid_slaves():
            if int(label.grid_info()['row']) == 1:
                label.grid_forget()

        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()
        cursor.execute('Select * FROM ' + table)
        self.records = cursor.fetchall()

        self.list_name_str = ''
        self.list_id_str = ''
        for record in self.records:
            self.list_name_str += str(record[1]) + '\n'
            self.list_id_str += str(record[0]) + '\n'

        self.list_name = Label(self.list_frame, text=self.list_name_str)
        self.list_name.grid(row=1, column=0, sticky=W)
        self.list_id = Label(self.list_frame, text=self.list_id_str)
        self.list_id.grid(row=1, column=1)
        # conn.commit()
        conn.close()


    def submit(self, table, dropdowns, type):
        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ' + table + ' VALUES' + '(:id,'
                                                          + ':name,'
                                                          + ':hp,'
                                                          + ':ac,'
                                                          + ':dc,'
                                                          + ':spell_1,'
                                                          + ':spell_2,'
                                                          + ':spell_3,'
                                                          + ':spell_4,'
                                                          + ':spell_5,'
                                                          + ':spell_6,'
                                                          + ':spell_7,'
                                                          + ':spell_8,'
                                                          + ':spell_9,'
                                                          + ':statblock)',
                {
                    'id': self.id.get(),
                    'name': self.name.get(),
                    'hp': self.hp.get(),
                    'ac': self.ac.get(),
                    'dc': self.dc.get(),
                    'spell_1': self.spell_1.get(),
                    'spell_2': self.spell_2.get(),
                    'spell_3': self.spell_3.get(),
                    'spell_4': self.spell_4.get(),
                    'spell_5': self.spell_5.get(),
                    'spell_6': self.spell_6.get(),
                    'spell_7': self.spell_7.get(),
                    'spell_8': self.spell_8.get(),
                    'spell_9': self.spell_9.get(),
                    'statblock': self.path
                })

        conn.commit()
        conn.close()
        self.wipe_entry()
        for dropdown in dropdowns:
            print(dropdown.table)
            if dropdown.table == table:
                dropdown.call_creatures(table, type)
                dropdown.callback()


    def delete(self, table, dropdowns, type):
        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()

        cursor.execute('DELETE from ' + table + ' WHERE rowid = ' + self.id.get())

        conn.commit()
        conn.close()
        self.id.delete(0, END)
        for dropdown in dropdowns:
            if dropdown.table == table:
                dropdown.call_creatures(table, type)
                dropdown.callback()


    def edit(self, table):
        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ' + table + ' WHERE rowid = ' + self.id.get())
        self.records = cursor.fetchall()
        self.wipe_entry()

        for record in self.records:
            self.name.insert(0, record[1])
            self.hp.insert(0, record[2])
            self.ac.insert(0, record[3])
            self.dc.insert(0, record[4])
            self.id.insert(0, record[0])
            self.spell_1.insert(0, record[5])
            self.spell_2.insert(0, record[6])
            self.spell_3.insert(0, record[7])
            self.spell_4.insert(0, record[8])
            self.spell_5.insert(0, record[9])
            self.spell_6.insert(0, record[10])
            self.spell_7.insert(0, record[11])
            self.spell_8.insert(0, record[12])
            self.spell_9.insert(0, record[13])

            self.path = record[14]
            self.statblock_file_l = Label(self.input_frame, text=os.path.basename(self.path))
            self.statblock_file_l.grid(row=2, column=3, columnspan=3,
                                       padx=(0, 15), pady=(0, 5))

        if self.save_b['state'] == DISABLED:
            self.cancel_b['state'] = NORMAL
            self.save_b['state'] = NORMAL
            self.id['state'] = DISABLED
            self.add_b['state'] = DISABLED
            self.delete_b['state'] = DISABLED
            self.edit_b['state'] = DISABLED
        conn.commit()
        conn.close()


    def save(self, table, dropdowns, type):
        conn = sqlite3.connect('Database/creatures.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE ' + table + ' SET ' + '''id = :id,
                                                       name = :name,
                                                       hp = :hp,
                                                       ac = :ac,
                                                       dc = :dc,
                                                       spell_1 = :spell_1,
                                                       spell_2 = :spell_2,
                                                       spell_3 = :spell_3,
                                                       spell_4 = :spell_4,
                                                       spell_5 = :spell_5,
                                                       spell_6 = :spell_6,
                                                       spell_7 = :spell_7,
                                                       spell_8 = :spell_8,
                                                       spell_9 = :spell_9,
                                                       statblock = :statblock

                                                       WHERE rowid = :id''',
            {
                'id': self.id.get(),
                'name': self.name.get(),
                'hp': self.hp.get(),
                'ac': self.ac.get(),
                'dc': self.dc.get(),
                'spell_1': self.spell_1.get(),
                'spell_2': self.spell_2.get(),
                'spell_3': self.spell_3.get(),
                'spell_4': self.spell_4.get(),
                'spell_5': self.spell_5.get(),
                'spell_6': self.spell_6.get(),
                'spell_7': self.spell_7.get(),
                'spell_8': self.spell_8.get(),
                'spell_9': self.spell_9.get(),
                'statblock': self.path

            })
        conn.commit()
        conn.close()

        if self.save_b['state'] == NORMAL:
            self.cancel_b['state'] = DISABLED
            self.save_b['state'] = DISABLED
            self.id['state'] = NORMAL
            self.add_b['state'] = NORMAL
            self.delete_b['state'] = NORMAL
            self.edit_b['state'] = NORMAL
        self.wipe_entry()
        for dropdown in dropdowns:
            if dropdown.table == table:
                dropdown.call_creatures(table, type)
                dropdown.callback()


    def cancel(self):
        if self.save_b['state'] == NORMAL:
            self.cancel_b['state'] = DISABLED
            self.save_b['state'] = DISABLED
            self.id['state'] = NORMAL
            self.add_b['state'] = NORMAL
            self.delete_b['state'] = NORMAL
            self.edit_b['state'] = NORMAL
        self.wipe_entry()

    def wipe_entry(self):
        self.name.delete(0, END)
        self.hp.delete(0, END)
        self.ac.delete(0, END)
        self.dc.delete(0, END)
        self.id.delete(0, END)
        self.spell_1.delete(0, END)
        self.spell_2.delete(0, END)
        self.spell_3.delete(0, END)
        self.spell_4.delete(0, END)
        self.spell_5.delete(0, END)
        self.spell_6.delete(0, END)
        self.spell_7.delete(0, END)
        self.spell_8.delete(0, END)
        self.spell_9.delete(0, END)
        if  self.statblock_file_l is not NONE:
            self.statblock_file_l.grid_forget()
            self.statblock_file_l = NONE


if __name__ == '__main__':
    from PIL import ImageTk,Image
    from tkinter import messagebox
    from tkinter import filedialog
    player_window = NewWindow('Players', 'Player', 'players')
    enemy_window = NewWindow('Enemies', 'Enemy', 'enemies')
    npc_window = NewWindow('NPCs', 'NPC', 'npcs')
