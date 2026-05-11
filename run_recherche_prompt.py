import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
import os
import anthropic

eingabe = tk.Tk()

fields = "Unternehmen", "Branche", "Standorte", "Notizen"

e = []
for i, field in enumerate(fields):
    tk.Label(eingabe, text = field).grid(row = i)
    entry= tk.Entry(eingabe)
    entry.grid(row = i, column = 1)

    e.append(entry)

def anzeigen():
    for i, field in enumerate(fields):
        print(field + ":" + e[i].get())#

def speichern():
    eingabewerte = e
    print("Die übergebenen Werte wurden gespeichert!")
    

#tk.Button(eingabe, text= "Anzeigen", command = anzeigen).grid(row = len(fields), column = 0)
tk.Button(eingabe, text = "Speichern", command = speichern).grid(row = len(fields), column = 0)
tk.Button(eingabe, text = "Quit", command = eingabe.quit).grid(row= len(fields), column = 1)
eingabe.mainloop()

print(eingabewerte)