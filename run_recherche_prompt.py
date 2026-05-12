import tkinter as tk
import threading
import os
import ttkbootstrap as ttk

from gui_funcs import fill_prompt, prompt_ausführen, lese_eingaben, save_filename, recherche

#----Konfig-------
PROMPT_FILE = "rechercheprompt.md"
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not API_KEY:
    raise ValueError("ANTHROPIC_API_KEY ist nicht gesetzt!")
MODEL = "claude-sonnet-4-20250511"
MAX_TOKENS = 8000

fields = "Unternehmen", "Branche(optional)", "Standorte(optional)", "Notizen(optional)"

entries = {}

eingabe = ttk.Window()
eingabe.geometry("400x600")

label = ttk.Label(eingabe, text = "Eingabefenster")
label.pack(pady = 30)
label.config(font=("Arial", 20, "bold"))

entry_frame = ttk.Frame(eingabe)
entry_frame.pack(pady = 15, padx = 10, fill = "x")

entry_frame.columnconfigure(1, weight=1)

for i, field in enumerate(fields):
    ttk.Label(entry_frame, text = field).grid(row = i, column = 0, padx = 5, pady = 15)

    entry = ttk.Entry(entry_frame)
    entry.grid(row = i, column = 1, sticky = "ew", padx = 5, pady = 15) 

    entries[field] = entry

button_frame = ttk.Frame(eingabe)
button_frame.pack(pady = 50, padx = 10, fill = "x")
#tk.Button(eingabe, text= "Anzeigen", command = anzeigen).grid(row = len(fields), column = 0)
ttk.Button(button_frame, text = "Prompt ausführen", command = recherche, bootstyle = "success").grid(row = len(fields), column = 0)
ttk.Button(button_frame, text = "Quit", command = eingabe.quit, bootstyle = "secondary").grid(row= len(fields), column = 1)
eingabe.mainloop()
