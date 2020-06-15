from tkinter import *
from Modules.config import combatants

class OptionWindow:

    def __init__(self, combatant, stat, default):
        self.window = Toplevel()
        self.window.title('Change Value')
        self.window.iconbitmap('Statblocks/Icon.ico')
        self.window.geometry('100x100')
        self.window.attributes('-topmost', 1)

        self.radiovar = IntVar()
        self.frame = LabelFrame(self.window, bd=0)
        self.frame.grid(row=0, column=0)
        self.add_button = Radiobutton(self.frame, text='Add', variable=self.radiovar, value=1)
        self.add_button.grid(row=0, column=0, sticky=W)
        self.subtract_button = Radiobutton(self.frame, text='Subtract', variable=self.radiovar, value=2)
        self.subtract_button.grid(row=1, column=0, columnspan=2, sticky=W)
        self.default = Radiobutton(self.frame, text='Set to Default', variable=self.radiovar, value=3)
        self.default.grid(row=2, column=0, columnspan=3, sticky=W)

        self.add = Entry(self.frame, width=3, justify=CENTER, state=DISABLED)
        self.add.grid(row=0, column=1, sticky=W)
        self.subtract = Entry(self.frame, width=3, justify=CENTER, state=DISABLED)
        self.subtract.grid(row=1, column=1, sticky=W, padx=(20,0))

        self.ok = Button(self.frame, text='Ok', command=lambda: self.change(combatant, stat, default), state=DISABLED)
        self.ok.grid(row=3, column=0, sticky=E, ipadx=7)
        self.cancel = Button(self.frame, text='cancel', command=self.cancel_change)
        self.cancel.grid(row=3, column=1, sticky=W)

        self.window.grid_columnconfigure(0, weight=1)

        self.radiovar.trace('w', self.callback)

    def callback(self, *args):
        self.var = self.radiovar.get()
        if self.var > 0 and self.var < 4:
            self.ok['state'] = NORMAL
            if self.var == 1:
                self.subtract.delete(0, END)
                self.add['state'] = NORMAL
                self.subtract['state'] = DISABLED
            elif self.var == 2:
                self.add.delete(0, END)
                self.subtract['state'] = NORMAL
                self.add['state'] = DISABLED
            else:
                self.add.delete(0, END)
                self.subtract.delete(0, END)
                self.add['state'] = DISABLED
                self.subtract['state'] = DISABLED
        else:
            self.add.delete(0, END)
            self.subtract.delete(0, END)
            self.ok['state'] = DISABLED
            self.add['state'] = DISABLED
            self.subtract['state'] = DISABLED


    def change(self, combatant, stat, default):
        if self.var == 1:
            if stat == 'maxhp':
                self.text = combatants[combatant][0].maxhp['text'].split()
                print(self.text)
                self.num_1 = int(self.text[1])
                self.num_2 = int(self.add.get())
                combatants[combatant][0].maxhp['text'] = 'Max: ' + str(self.num_1 + self.num_2)
            elif stat == 'ac':
                self.num_1 = int(combatants[combatant][0].ac['text'])
                self.num_2 = int(self.add.get())
                combatants[combatant][0].ac['text'] = str(self.num_1 + self.num_2)
            else:
                if combatants[combatant][0].dc['text']:
                    self.num_1 = int(combatants[combatant][0].dc['text'])
                else:
                    self.num_1 = 0
                self.num_2 = int(self.add.get())
                combatants[combatant][0].dc['text'] = str(self.num_1 + self.num_2)

        elif self.var == 2:
            if stat == 'maxhp':
                self.text = combatants[combatant][0].maxhp['text'].split()
                print(self.text)
                self.num_1 = int(self.text[1])
                print(self.num_1)
                self.num_2 = int(self.subtract.get())
                combatants[combatant][0].maxhp['text'] = 'Max: ' + str(self.num_1 - self.num_2)
            elif stat == 'ac':
                self.num_1 = int(combatants[combatant][0].ac['text'])
                self.num_2 = int(self.subtract.get())
                combatants[combatant][0].ac['text'] = str(self.num_1 - self.num_2)
            else:
                self.num_1 = int(combatants[combatant][0].dc['text'])
                self.num_2 = int(self.subtract.get())
                combatants[combatant][0].dc['text'] = str(self.num_1 - self.num_2)

        else:
            if stat == 'maxhp':
                combatants[combatant][0].maxhp['text'] = 'Max: ' + str(default)
            elif stat == 'ac':
                combatants[combatant][0].ac['text'] = str(default)
            else:
                combatants[combatant][0].dc['text'] = str(default)

        self.radiovar.set(0)
        self.window.destroy()


    def cancel_change(self):
        self.window.destroy()
