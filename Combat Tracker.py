from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

from Classes.Window_Class import NewWindow


root = Tk()
root.title('Combat Tracker')
root.iconbitmap('Statblocks/Icon.ico')
root.geometry('1000x600')

def open_players():
    Players_window = NewWindow('Players', 'Player', 'players')

def open_enemies():
    enemies_window = NewWindow('Enemies', 'Enemy', 'enemies')

def open_npcs():
    npc_window = NewWindow('NPCs', 'NPC', 'npcs')

database_frame = LabelFrame(root)
database_frame.grid(row=0, column=0)

p_database = Button(database_frame, text='Players', command=open_players)
p_database.grid(row=0, column=0)

e_database = Button(database_frame, text='Enemies', command=open_enemies)
e_database.grid(row=0, column=1)

n_database = Button(database_frame, text='NPCs', command=open_npcs)
n_database.grid(row=0, column=2)




root.mainloop()
