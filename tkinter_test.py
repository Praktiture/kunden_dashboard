import ttkbootstrap as ttk

app = ttk.Window()
app.geometry("600x500")

label = ttk.Label(app, text = "Eingabefenster")
label.pack(pady = 30)
label.config(font=("Arial", 20, "bold"))

entry_frame = ttk.Frame(app)
entry_frame.pack(pady = 15, padx = 10, fill = "x")

entry_frame.columnconfigure(1, weight=1)
ttk.Label(entry_frame, text = "Firmenname").grid(row = 0, column = 0, padx = 5, pady = 15)
ttk.Entry(entry_frame).grid(row = 0, column = 1, sticky = "ew", padx = 5, pady = 15)
ttk.Label(entry_frame, text = "Branche").grid(row = 1, column = 0, padx = 5, pady = 15)
ttk.Entry(entry_frame).grid(row = 1, column = 1, sticky = "ew", padx = 5, pady = 15)

button_frame = ttk.Frame(app)
button_frame.pack(pady = 50, padx = 10, fill = "x")
ttk.Button(button_frame, text = "Submit", bootstyle="success").pack(side="left", padx = 10)
ttk.Button(button_frame, text = "Cancel", command = app.quit, bootstyle="secondary").pack(side="left", padx = 10)


app.mainloop()