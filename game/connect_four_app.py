import tkinter as tk
from tkinter import messagebox
from game.connect_four import ConnectFour, COLS, ROWS

OUTLAYER = 10
class ConnectFourApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.set_window_size(COLS * 100 + OUTLAYER * 2, ROWS * 100 + OUTLAYER)
        self.create_background()
        self.show_home_screen()

    def set_window_size(self, width, height):
        self.root.geometry(f"{width}x{height}")

    def create_background(self):
        background_color = "#3498db"  # Choisissez la couleur de fond que vous souhaitez
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height(), bg=background_color)
        self.canvas.pack(fill="both", expand=True)

    def show_home_screen(self):
        play_button = tk.Button(self.canvas, text="Jouer", command=self.start_game, width=20, height=2)
        play_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        quit_button = tk.Button(self.canvas, text="Quitter", command=self.root.quit, width=20, height=2)
        quit_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def start_game(self):
        self.clear_window()
        ConnectFour(self.root)
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    