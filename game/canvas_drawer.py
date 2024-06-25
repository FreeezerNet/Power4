import tkinter as tk

ROWS = 6
COLS = 7
OUTLAYER = 200
ANIMATION_SPEED = 10  # Speed of the drop animation in milliseconds
PLAYER_COLORS = {1: 'red', 2: 'yellow'}

class ConnectFourCanvas:
    def __init__(self, root, board, drop_disc_callback):
        self.root = root
        self.board = board
        self.drop_disc_callback = drop_disc_callback
        self.canvas = tk.Canvas(self.root, width=COLS*100+OUTLAYER*2, height=ROWS*100+OUTLAYER, bg='white')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()

    def draw_board(self):
        # Draw the blue board area
        self.canvas.create_rectangle(OUTLAYER, OUTLAYER / 2, COLS * 100 + OUTLAYER, ROWS * 100 + OUTLAYER / 2, fill='blue', outline='blue')
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * 100 + 5 + OUTLAYER
                y1 = row * 100 + 5 + OUTLAYER / 2
                x2 = x1 + 90
                y2 = y1 + 90
                self.canvas.create_oval(x1, y1, x2, y2, fill='white', outline='black')

    def handle_click(self, event):
        col = (event.x - OUTLAYER) // 100
        if 0 <= col < COLS:
            self.drop_disc_callback(col)

    def animate_drop(self, col, row, color):
        x1 = col * 100 + 5 + OUTLAYER
        x2 = x1 + 90
        y1 = 5 + OUTLAYER / 2
        y2 = y1 + 90

        oval = self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline='black')

        def step_animation(current_y):
            if current_y < row * 100 + 5 + OUTLAYER / 2:
                self.canvas.move(oval, 0, 10)
                self.root.after(ANIMATION_SPEED, step_animation, current_y + 10)
            else:
                self.canvas.move(oval, 0, row * 100 + 5 + OUTLAYER / 2 - current_y)  # Correct position if overshoot

        step_animation(y1)
    
    def reset(self):
        self.canvas.delete("all")
        self.draw_board()
