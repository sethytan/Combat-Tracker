from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from Modules.Window_Class import NewWindow
from Modules.Tracker_Row_Class import Trow
from Modules.add_combatant_Class import DropDown
from Modules.config import combatants
from Modules.Sort_Button import SortButton

root = Tk()
root.title('Combat Tracker')
root.iconbitmap('Statblocks/Icon.ico')
root.minsize(905, 600)
root.state('zoomed')
root.grid_columnconfigure(0, weight=1)

# background_image = ImageTk.PhotoImage(Image.open('Statblocks/papyr.png'))
# background = Label(image=background_image)
# background.grid(row=0, column=0, rowspan=20, columnspan=20)

combatants = []
def open_players():
    Players_window = NewWindow('Players', 'Player', 'players', dropdowns)

def open_enemies():
    enemies_window = NewWindow('Enemies', 'Enemy', 'enemies', dropdowns)

def open_npcs():
    npc_window = NewWindow('NPCs', 'NPC', 'npcs', dropdowns)

mainframe = LabelFrame(root, bd=0)
mainframe.grid(row=0, column=0, sticky=W+N)
database_frame = LabelFrame(mainframe, relief=SOLID)
database_frame.grid(row=0, column=0, padx=32, sticky=W+N)
table_root = LabelFrame(mainframe, bd=2, relief=FLAT)
table_root.grid(row=1, column=0, sticky=W+N)
table_frame = LabelFrame(table_root, bd=0, relief=SOLID)
table_frame.grid(row=0, column=0)
# table_frame.grid_rowconfigure(1, weight=1)
info_frame = LabelFrame(root, bd=0)
info_frame.grid(row=0, column=2, sticky=E+N, pady=(61, 0))

p_frame = LabelFrame(database_frame, bd=0)
p_frame.grid(row=0, column=0, padx=10, sticky=W)
e_frame = LabelFrame(database_frame, bd=0)
e_frame.grid(row=0, column=1, sticky=W)
n_frame = LabelFrame(database_frame, bd=0)
n_frame.grid(row=0, column=2, padx=10, sticky=W)

p_database = Button(p_frame, text='Players', command=open_players)
p_database.grid(row=0, column=0)
e_database = Button(e_frame, text='Enemies', command=open_enemies)
e_database.grid(row=0, column=0)
n_database = Button(n_frame, text='NPCs', command=open_npcs)
n_database.grid(row=0, column=0)
p_dropdown = DropDown(p_frame, 1, 0, 1, 'Player', 'players', table_frame, info_frame, table_root)
e_dropdown = DropDown(e_frame, 1, 0, 1, 'Enemy', 'enemies', table_frame, info_frame, table_root)
n_dropdown = DropDown(n_frame, 1, 0, 1, 'NPC', 'npcs', table_frame, info_frame, table_root)

dropdowns = (p_dropdown,
             e_dropdown,
             n_dropdown)

th_del_frame = LabelFrame(table_frame, bd=2, height=25, width=30, relief=FLAT)
th_del_frame.grid(row=0, column=0, sticky=N+E+S+W)
th_del_frame.grid_propagate(0)
th_del = Label(th_del_frame, text='', height=1)
th_del.grid(row=0, column=0)
th_name_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_name_frame.grid(row=0, column=1, sticky=N+E+S+W)
th_name = Label(th_name_frame, text='Name', width=6)
th_name.grid(row=0, column=0)
th_init_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_init_frame.grid(row=0, column=2, sticky=N+E+S+W)
th_init = SortButton(th_init_frame, 'Initiative')
th_hp_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_hp_frame.grid(row=0, column=3, sticky=N+E+S+W)
th_hp = Label(th_hp_frame, text='Health')
th_hp.pack()
th_ac_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_ac_frame.grid(row=0, column=4, sticky=N+E+S+W)
th_ac = Label(th_ac_frame, text='Armor')
th_ac.pack()
th_dc_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_dc_frame.grid(row=0, column=6, sticky=N+E+S+W)
th_dc = Label(th_dc_frame, text='Save DC')
th_dc.pack()
th_reaction_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_reaction_frame.grid(row=0, column=5, sticky=N+E+S+W)
th_reaction = Label(th_reaction_frame, text='Reaction')
th_reaction.pack()
th_concentration_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_concentration_frame.grid(row=0, column=7, sticky=N+E+S+W)
th_concentration = Label(th_concentration_frame, text='Concentration')
th_concentration.pack()
th_conditions_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_conditions_frame.grid(row=0, column=8, sticky=N+E+S+W)
th_conditions = Label(th_conditions_frame, text='Conditions')
th_conditions.pack()
th_spellslots_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_spellslots_frame.grid(row=0, column=9, sticky=N+E+S+W)
th_spellslots = Label(th_spellslots_frame, text='Spell Slots')
th_spellslots.pack()
th_deathsaves_frame = LabelFrame(table_frame, bd=2, relief=SOLID)
th_deathsaves_frame.grid(row=0, column=10, sticky=N+E+S+W)
th_deathsaves = Label(th_deathsaves_frame, text='Death Saves')
th_deathsaves.pack()








root.mainloop()
