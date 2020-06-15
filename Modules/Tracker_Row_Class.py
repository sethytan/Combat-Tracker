from tkinter import *
import os
import sqlite3
from PIL import ImageTk,Image
from Modules.SpellSlot import LevelSlots
from Modules.Option_Window import OptionWindow
# from Modules.config import combatants

class Trow:

    def __init__(self, root, row, name, hp, ac, dc, sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, statblock, info):
        """Initialise new frame object.
            Arguments:
            -root: the window that the frame will be placed in
        """
        # self.delete_frame = LabelFrame(delete, bd=2, relief=FLAT, height=100, width=30)
        # self.delete_frame.grid(row=row, column=0, sticky=N+E+S+W)
        # self.delete_frame.grid_propagate(0)
        # self.delete_button = Button(self.delete_frame, text='X', command=self.delete_row, relief=FLAT)
        # self.delete_button.grid(row=0, column=0)
        # self.delete_frame.grid_rowconfigure(0, weight=1)
        # self.delete_frame.grid_columnconfigure(0, weight=1)
        self.root = root
        self.row = row
        self.name = name
        self.hp = hp
        self.ac = ac
        self.dc = dc
        self.sp1 = sp1
        self.sp2 = sp2
        self.sp3 = sp3
        self.sp4 = sp4
        self.sp5 = sp5
        self.sp6 = sp6
        self.sp7 = sp7
        self.sp8 = sp8
        self.sp9 = sp9
        self.statblock = statblock
        self.info = info

        self.name_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.name_frame.grid(row=self.row, column=1, sticky=N+E+S+W)
        self.name = Button(self.name_frame, text=name, relief=FLAT, command=lambda: self.show_statblock(statblock, info))
        self.name.grid(row=0, column=0, sticky=N+E+S+W)
        self.name_frame.grid_rowconfigure(0, weight=1)
        self.name_frame.grid_columnconfigure(0, weight=1)

        self.init_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.init_frame.grid(row=self.row, column=2, sticky=N+E+S+W)
        self.init = Entry(self.init_frame, width=3, justify=CENTER)
        self.init.grid(row=0, column=0)
        self.init_frame.grid_rowconfigure(0, weight=1)
        self.init_frame.grid_columnconfigure(0, weight=1)

        self.hp_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.hp_frame.grid(row=self.row, column=3, sticky=N+E+S+W)
        self.hp_subframe = LabelFrame(self.hp_frame, bd=0)
        self.hp_subframe.grid(row=0, column=0, pady=10)
        self.maxhp = Button(self.hp_subframe, text='Max: ' + str(hp), relief=GROOVE, command=lambda: self.option_change(row, 'maxhp', hp))
        self.maxhp.grid(row=0, column=0, columnspan=2)
        self.curhp_label = Label(self.hp_subframe, text='HP')
        self.curhp_label.grid(row=1, column=0)
        self.curhp_entry = Entry(self.hp_subframe, width=5, justify=CENTER)
        self.curhp_entry.grid(row=2, column=0)
        self.tmphp_label = Label(self.hp_subframe, text='Temp')
        self.tmphp_label.grid(row=1, column=1, sticky=E)
        self.tmphp_entry = Entry(self.hp_subframe, width=5, justify=CENTER)
        self.tmphp_entry.grid(row=2, column=1, sticky=E)
        self.hp_frame.grid_rowconfigure(0, weight=1)

        self.ac_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.ac_frame.grid(row=self.row, column=4, sticky=N+E+S+W)
        self.ac = Button(self.ac_frame, text=ac, relief=FLAT, command=lambda: self.option_change(row, 'ac', ac))
        self.ac.grid(row=0, column=0, sticky=N+E+S+W)
        self.ac_frame.grid_rowconfigure(0, weight=1)
        self.ac_frame.grid_columnconfigure(0, weight=1)

        self.dc_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.dc_frame.grid(row=self.row, column=6, sticky=N+E+S+W)
        self.dc = Button(self.dc_frame, text=dc, relief=FLAT, command=lambda: self.option_change(row, 'dc', dc))
        self.dc.grid(row=0, column=0, sticky=N+E+S+W)
        self.dc_frame.grid_rowconfigure(0, weight=1)
        self.dc_frame.grid_columnconfigure(0, weight=1)

        self.reaction_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.reaction_frame.grid(row=self.row, column=5, sticky=N+E+S+W)
        self.reaction = Button(self.reaction_frame, text='', relief=FLAT,
                               command=lambda: self.button_check(self.reaction))
        self.reaction.grid(row=0, column=0, sticky=N+E+S+W)
        self.reaction_frame.grid_rowconfigure(0, weight=1)
        self.reaction_frame.grid_columnconfigure(0, weight=1)

        self.concentration_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.concentration_frame.grid(row=self.row, column=7, sticky=N+E+S+W)
        self.concentration = Button(self.concentration_frame, text='', relief=FLAT,
                                    command=lambda: self.button_check(self.concentration))
        self.concentration.grid(row=0, column=0, sticky=N+E+S+W)
        self.concentration_frame.grid_rowconfigure(0, weight=1)
        self.concentration_frame.grid_columnconfigure(0, weight=1)

        # Conditions
        self.conditions_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.conditions_frame.grid(row=self.row, column=8, sticky=N+E+S+W)
        self.conditions = ('Blinded', 'Charmed', 'Deafened',
                           'Exhaustion', 'Frightened', 'Grappled',
                           'Incapacitated', 'Invisible', 'Paralyzed',
                           'Petrified', 'Poisoned', 'Prone',
                           'Restrained', 'Stunned', 'Unconscious',)
        self.condition = StringVar()
        self.condition.set('Condition')
        self.active_conditions = []
        self.active_con_labels = []
        self.con_label_frame = LabelFrame(self.conditions_frame, bd=0, width=152, height=63)
        self.con_label_frame.grid(row=0, column=0, columnspan=3, sticky=N+W)
        self.con_label_frame.grid_propagate(0)
        self.con_dropdown_frame = LabelFrame(self.conditions_frame, bd=0)
        self.con_dropdown_frame.grid(row=1, column=0, columnspan=3, sticky=W)
        self.con_dropdown = OptionMenu(self.con_dropdown_frame, self.condition, *self.conditions)
        self.con_dropdown.config(width=10)
        self.con_dropdown.grid(row=0, column=2)
        self.con_button = Button(self.con_dropdown_frame, text='+', command=self.add_condition, state=DISABLED)
        self.con_button.grid(row=0, column=0, ipadx=3, padx=(1, 0))
        self.con_remove = Button(self.con_dropdown_frame, text='-', command=self.remove_condition, state=DISABLED)
        self.con_remove.grid(row=0, column=1, ipadx=3)
        self.condition.trace('w', self.con_callback)
        self.conditions_frame.grid_rowconfigure(0, weight=1)
        # self.conditions_frame.grid_rowconfigure(7, weight=1)

        # Spell Slots
        self.spellslots_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.spellslots_frame.grid(row=self.row, column=9, sticky=N+E+S+W)
        self.spells = [[1, sp1],
                       [2, sp2],
                       [3, sp3],
                       [4, sp4],
                       [5, sp5],
                       [6, sp6],
                       [7, sp7],
                       [8, sp8],
                       [9, sp9],]
        self.slots = []
        self.spell_frame1 = LabelFrame(self.spellslots_frame, relief=SOLID, bd=0)
        self.spell_frame1.grid(row=0, column=0, sticky=N+W+S+E)
        self.spell_frame2 = LabelFrame(self.spellslots_frame, relief=SOLID, bd=0)
        self.spell_frame3 = LabelFrame(self.spellslots_frame, relief=SOLID, bd=0)

        for spell in self.spells:
            if spell[1]:
                if spell[1] > 0:
                    if spell[0] < 4:
                        self.spell_row = spell[0] - 1
                        self.slot = LevelSlots(self.spell_frame1,
                                               spell[0], spell[1],
                                               self.spell_row)
                        self.slots.append(self.slot)
                    elif spell[0] < 7:
                        self.spell_row = spell[0] - 4
                        self.slot = LevelSlots(self.spell_frame2,
                                               spell[0], spell[1],
                                               self.spell_row)
                        self.slots.append(self.slot)
                    else:
                        self.spell_row = spell[0] - 7
                        self.slot = LevelSlots(self.spell_frame3,
                                               spell[0], spell[1],
                                               self.spell_row)
                        self.slots.append(self.slot)
        if len(self.slots) > 3:
            self.spell_frame1['bd'] = 1
            self.spell_frame2['bd'] = 1
            self.spell_frame2.grid(row=0, column=1, sticky=N+W+S+E)
            if len(self.slots) > 6:
                self.spell_frame3['bd'] = 1
                self.spell_frame3.grid(row=0, column=2, sticky=N+W+S+E)
        self.spellslots_frame.grid_rowconfigure(0, weight=1)

        # Death Saves
        self.deathsaves_frame = LabelFrame(root, bd=2, relief=SOLID)
        self.deathsaves_frame.grid(row=self.row, column=10, sticky=N+E+S+W)
        self.deathsaves_subframe = LabelFrame(self.deathsaves_frame, bd=0)
        self.deathsaves_subframe.grid(row=0, column=0)
        self.death_stable = NONE
        self.death_dead = NONE
        self.death_fails_label = LabelFrame(self.deathsaves_subframe, text='Fails', bd=1, relief=RIDGE)
        self.death_fails_label.grid(row=0, column=0)
        self.death_saves_label = LabelFrame(self.deathsaves_subframe, text='Saves', bd=1, relief=RIDGE)
        self.death_saves_label.grid(row=0, column=1)

        self.fail_check1 = Button(self.death_fails_label, text='', width=2, height=1, relief=RIDGE,
                                  command=lambda: self.button_check(self.fail_check1))
        self.fail_check2 = Button(self.death_fails_label, text='', width=2, height=1, relief=RIDGE,
                                  command=lambda: self.button_check(self.fail_check2))
        self.fail_check3 = Button(self.death_fails_label, text='', width=2, height=1, relief=RIDGE,
                                  command=lambda: self.button_check(self.fail_check3))
        self.succ_check1 = Button(self.death_saves_label, text='', width=2, height=1, relief=RIDGE,
                                  command=lambda: self.button_check(self.succ_check1))
        self.succ_check2 = Button(self.death_saves_label, text='', width=2, height=1, relief=RIDGE,
                                  command=lambda: self.button_check(self.succ_check2))
        self.succ_check3 = Button(self.death_saves_label, text='', width=2, height=1, relief=RIDGE,
                                  command=lambda: self.button_check(self.succ_check3))
        self.fail_check1.grid(row=0, column=0, columnspan=2)
        self.fail_check2.grid(row=1, column=0, padx=(5,0), pady=(0,5))
        self.fail_check3.grid(row=1, column=1, padx=(0,5), pady=(0,5))
        self.succ_check1.grid(row=0, column=0, columnspan=2)
        self.succ_check2.grid(row=1, column=0, padx=(5,0), pady=(0,5))
        self.succ_check3.grid(row=1, column=1, padx=(0,5), pady=(0,5))
        self.death_status = Button(self.deathsaves_subframe, text='', relief=FLAT,
                                   command=lambda: self.button_check(self.death_status))
        self.death_status.grid(row=2, column=0, columnspan=2)
        self.deathsaves_frame.grid_rowconfigure(0, weight=1)


    def call_row(self):
        self.name_frame.grid_configure(row=self.row)
        self.init_frame.grid_configure(row=self.row)
        self.hp_frame.grid_configure(row=self.row)
        self.ac_frame.grid_configure(row=self.row)
        self.dc_frame.grid_configure(row=self.row)
        self.reaction_frame.grid_configure(row=self.row)
        self.concentration_frame.grid_configure(row=self.row)
        self.conditions_frame.grid_configure(row=self.row)
        self.spellslots_frame.grid_configure(row=self.row)
        self.deathsaves_frame.grid_configure(row=self.row)


    def del_row(self):
        self.name_frame.grid_forget()
        self.init_frame.grid_forget()
        self.hp_frame.grid_forget()
        self.ac_frame.grid_forget()
        self.dc_frame.grid_forget()
        self.reaction_frame.grid_forget()
        self.concentration_frame.grid_forget()
        self.conditions_frame.grid_forget()
        self.spellslots_frame.grid_forget()
        self.deathsaves_frame.grid_forget()


    def show_statblock(self, statblock, info):
        self.statblock_image = ImageTk.PhotoImage(Image.open(statblock))
        self.statblock_label = Label(info, image=self.statblock_image)
        self.statblock_label.grid(row=0, column=0)

    def option_change(self, row, stat, hp):
        self.Option = OptionWindow(row-1, stat, hp)


    def remove_condition(self):
        if self.condition.get() == 'Exhaustion':
            for label in (self.active_con_labels or []):
                if label.cget('text') == 'Exhaustion 6':
                    label['text'] = 'Exhaustion 5'
                    self.con_callback()
                    break
                elif label.cget('text') == 'Exhaustion 5':
                    label['text'] = 'Exhaustion 4'
                    break
                elif label.cget('text') == 'Exhaustion 4':
                    label['text'] = 'Exhaustion 3'
                    break
                elif label.cget('text') == 'Exhaustion 3':
                    label['text'] = 'Exhaustion 2'
                    break
                elif label.cget('text') == 'Exhaustion 2':
                    label['text'] = 'Exhaustion 1'
                    break
                elif label.cget('text') == 'Exhaustion 1':
                    self.con_i = self.active_con_labels.index(label)
                    self.active_con_labels.remove(label)
                    label.grid_forget()
                    for label in self.active_con_labels:
                        if self.active_con_labels.index(label) >= self.con_i:
                            if (self.active_con_labels.index(label) == 2 or
                                self.active_con_labels.index(label) == 5 or
                                self.active_con_labels.index(label) == 8 or
                                self.active_con_labels.index(label) == 11):
                                if self.active_con_labels.index(label) == 2:
                                    label.grid(row=2, column=0)
                                elif self.active_con_labels.index(label) == 5:
                                    label.grid(row=2, column=1)
                                elif self.active_con_labels.index(label) == 8:
                                    label.grid(row=2, column=2)
                                else:
                                    label.grid(row=2, column=3)
                            elif (self.active_con_labels.index(label) == 0 or
                                  self.active_con_labels.index(label) == 3 or
                                  self.active_con_labels.index(label) == 6 or
                                  self.active_con_labels.index(label) == 9 or
                                  self.active_con_labels.index(label) == 12):
                                label.grid_configure(row=0)
                            else:
                                label.grid_configure(row=1)
                    self.active_conditions.remove(self.condition.get())
                    self.con_callback()
        else:
            for label in (self.active_con_labels or []):
                if label.cget('text') == self.condition.get():
                    self.con_i = self.active_con_labels.index(label)
                    self.active_con_labels.remove(label)
                    label.grid_forget()
                    for label in self.active_con_labels:
                        if self.active_con_labels.index(label) >= self.con_i:
                            if (self.active_con_labels.index(label) == 2 or
                                self.active_con_labels.index(label) == 5 or
                                self.active_con_labels.index(label) == 8 or
                                self.active_con_labels.index(label) == 11):
                                if self.active_con_labels.index(label) == 2:
                                    label.grid(row=2, column=0)
                                elif self.active_con_labels.index(label) == 5:
                                    label.grid(row=2, column=1)
                                elif self.active_con_labels.index(label) == 8:
                                    label.grid(row=2, column=2)
                                else:
                                    label.grid(row=2, column=3)
                            elif (self.active_con_labels.index(label) == 0 or
                                  self.active_con_labels.index(label) == 3 or
                                  self.active_con_labels.index(label) == 6 or
                                  self.active_con_labels.index(label) == 9 or
                                  self.active_con_labels.index(label) == 12):
                                label.grid_configure(row=0)
                            else:
                                label.grid_configure(row=1)
                    self.active_conditions.remove(self.condition.get())
                    self.con_callback()
        self.condition.set('Condition')


    def add_condition(self):
        self.con_i = len(self.active_con_labels)
        if (self.con_i == 0 or
            self.con_i == 3 or
            self.con_i == 6 or
            self.con_i == 9 or
            self.con_i == 12):
            self.con_row = 0
        elif (self.con_i == 1 or
            self.con_i == 4 or
            self.con_i == 7 or
            self.con_i == 10 or
            self.con_i == 13):
            self.con_row = 1
        else:
            self.con_row = 2

        if self.con_i < 3:
            self.con_col = 0
        elif self.con_i < 6:
            self.con_col = 1
        elif self.con_i < 9:
            self.con_col = 2
        elif self.con_i < 12:
            self.con_col = 3
        else:
            self.con_col = 4

        if self.condition.get() == 'Exhaustion':
            for label in (self.active_con_labels or []):
                if label.cget('text') == 'Exhaustion 1':
                    label['text'] = 'Exhaustion 2'
                    break
                elif label.cget('text') == 'Exhaustion 2':
                    label['text'] = 'Exhaustion 3'
                    break
                elif label.cget('text') == 'Exhaustion 3':
                    label['text'] = 'Exhaustion 4'
                    break
                elif label.cget('text') == 'Exhaustion 4':
                    label['text'] = 'Exhaustion 5'
                    break
                elif label.cget('text') == 'Exhaustion 5':
                    label['text'] = 'Exhaustion 6'
                    self.con_callback()
                    break
            else:
                self.con_text = 'Exhaustion 1'
                self.con_label = Label(self.con_label_frame, text=self.con_text)
                self.con_label.grid(row=self.con_row, column=self.con_col, sticky=W)

                self.active_conditions.append(self.condition.get())
                self.active_con_labels.append(self.con_label)
                self.con_callback()
        else:
            self.con_text = self.condition.get()
            self.con_label = Label(self.con_label_frame, text=self.con_text)
            self.con_label.grid(row=self.con_row, column=self.con_col, sticky=W)

            self.active_conditions.append(self.condition.get())
            self.active_con_labels.append(self.con_label)
            self.con_callback()
        self.condition.set('Condition')


    def con_callback(self, *args):
        if self.active_conditions:
            for active in (self.active_conditions or []):
                if active == self.condition.get() and active != 'Exhaustion':
                    self.con_button['state'] = DISABLED
                    break
                elif active == 'Exhaustion':
                    for label in (self.active_con_labels or []):
                        if label.cget('text') == 'Exhaustion 6':
                            self.con_button['state'] = DISABLED
                            break
                    else:
                        self.con_button['state'] = NORMAL
                else:
                    self.con_button['state'] = NORMAL
        else:
            self.con_button['state'] = NORMAL

        if self.active_conditions:
            for active in (self.active_conditions or []):
                if active == self.condition.get():
                    self.con_remove['state'] = NORMAL
                    break
                else:
                    self.con_remove['state'] = DISABLED
        else:
            self.con_remove['state'] = DISABLED

        if len(self.active_con_labels) > 3:
            self.con_label_frame.grid_propagate(1)
        else:
            self.con_label_frame.grid_propagate(0)

    def button_check(self, button):
        text = button['text']
        if text == '':
            text = 'X'
        else:
            text = ''
        button['text'] = text


        if (self.fail_check1['text'] == 'X'
            and self.fail_check2['text'] == 'X'
            and self.fail_check3['text'] == 'X'):
            self.fail_check1['text'] = ''
            self.fail_check2['text'] = ''
            self.fail_check3['text'] = ''
            self.succ_check1['text'] = ''
            self.succ_check2['text'] = ''
            self.succ_check3['text'] = ''
            self.death_status['text'] = 'Dead'
        elif (self.succ_check1['text'] == 'X'
              and self.succ_check2['text'] == 'X'
              and self.succ_check3['text'] == 'X'):
            self.fail_check1['text'] = ''
            self.fail_check2['text'] = ''
            self.fail_check3['text'] = ''
            self.succ_check1['text'] = ''
            self.succ_check2['text'] = ''
            self.succ_check3['text'] = ''
            self.death_status['text'] = 'Stable'
