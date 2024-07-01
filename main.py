import tkinter as tk
from game.connect_four_app import ConnectFourApp

def main():
    root = tk.Tk()
    app = ConnectFourApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
