import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Hello Tkinter")

# Créer un label
label = tk.Label(root, text="Hello")
label.pack(pady=20)

# Créer un bouton
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Lancer la boucle principale
root.mainloop()