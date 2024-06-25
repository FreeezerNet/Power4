import tkinter as tk
from game.connect_four import ConnectFour

def main():
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()

if __name__ == "__main__":
    main()
