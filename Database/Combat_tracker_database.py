from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.geometry('100x100')

#Create a database or connect to onvalue
conn = sqlite3.connect('D:/Learning to code/Python/D&D Combat Tracker/Database/creatures.db')


#Create cursor
cursor = conn.cursor()

#Create player character table
cursor.execute('''CREATE TABLE players (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        hp INTEGER,
        ac INTEGER,
        dc INTEGER,
        spell_1 INTEGER,
        spell_2 INTEGER,
        spell_3 INTEGER,
        spell_4 INTEGER,
        spell_5 INTEGER,
        spell_6 INTEGER,
        spell_7 INTEGER,
        spell_8 INTEGER,
        spell_9 INTEGER,
        statblock TEXT
        )''')


#Create npc table
cursor.execute('''CREATE TABLE npcs
            (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            hp INTEGER,
            ac INTEGER,
            dc INTEGER,
            spell_1 INTEGER,
            spell_2 INTEGER,
            spell_3 INTEGER,
            spell_4 INTEGER,
            spell_5 INTEGER,
            spell_6 INTEGER,
            spell_7 INTEGER,
            spell_8 INTEGER,
            spell_9 INTEGER,
            statblock TEXT
            )''')
#

#Create penemies table
cursor.execute('''CREATE TABLE enemies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        hp INTEGER,
        ac INTEGER,
        dc INTEGER,
        spell_1 INTEGER,
        spell_2 INTEGER,
        spell_3 INTEGER,
        spell_4 INTEGER,
        spell_5 INTEGER,
        spell_6 INTEGER,
        spell_7 INTEGER,
        spell_8 INTEGER,
        spell_9 INTEGER,
        statblock TEXT
        )''')

#commit changes
conn.commit()



#Close connection
conn.close()
