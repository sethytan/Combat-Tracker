from tkinter import *

class LevelSlots:
    """docstring for ."""

    def __init__(self, root, level, slots, row):
        self.frame = LabelFrame(root, bd=0)
        self.frame.grid(row=row, column=0, padx=(3), pady=3, sticky=N+W)
        self.button1 = Button(self.frame, text='lv '+str(level),
                              command=lambda: self.plus(slots), relief=GROOVE)
        self.button2 = Button(self.frame, text=slots,
                              command=self.minus, relief=GROOVE)
        self.label = Label(self.frame, text=':')

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=2)
        self.label.grid(row=0, column=1)

    def plus(self, slots):
        text = int(self.button2['text'])
        if text < slots:
            text += 1
        self.button2['text'] = str(text)

    def minus(self):
        text = int(self.button2['text'])
        if text > 0:
            text -= 1
        self.button2['text'] = str(text)
